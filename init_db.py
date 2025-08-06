from app import db, User, Key
from werkzeug.security import generate_password_hash

def init_db():
    print("🔄 Inicializando base de datos...")

    # Crear la key del owner si no existe
    owner_key = Key.query.filter_by(key='owner_key').first()
    if not owner_key:
        owner_key = Key(key='owner_key', used=True)
        db.session.add(owner_key)
        db.session.commit()
        print("✅ Key 'owner_key' creada.")
    else:
        print("ℹ️ Key 'owner_key' ya existe.")

    # Crear el usuario owner si no existe
    owner = User.query.filter_by(username='owner').first()
    if not owner:
        owner = User(username='owner', key='owner_key', role='owner', telegram_id='846983753')
        owner.password_hash = generate_password_hash('Saiper123')
        db.session.add(owner)
        db.session.commit()
        print("✅ Usuario 'owner' creado.")
    else:
        print("ℹ️ Usuario 'owner' ya existe.")

    print("🎉 Base de datos inicializada correctamente.")

if __name__ == '__main__':
    init_db()
