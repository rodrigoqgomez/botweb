from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
from app import db, Key  # importa tu modelo y DB
from app import db, Key, app
import random
import string

BOT_TOKEN = '7549342155:AAGTeGoCr6s56nckuq8KEDDB7aCKiU5BW3Y'
ADMIN_ID = 846983753  # Tu ID de Telegram

async def genkey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("No tienes permisos para generar keys.")
        return
    
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    # Aquí abrimos el contexto de Flask para la DB:
    with app.app_context():
        nueva_key = Key(key=key, used=False)
        db.session.add(nueva_key)
        db.session.commit()

    await update.message.reply_text(f"🔑 Key generada:\n`{key}`", parse_mode='Markdown')
async def start_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("genkey", genkey))

    # En lugar de app.run_polling(), usamos initialize() y start()
    await app.initialize()
    await app.start()
    print("Bot ejecutándose...")

    # NO cierres el loop, solo espera hasta que terminen
    await app.updater.start_polling()
