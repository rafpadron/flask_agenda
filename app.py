from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}/{database}'.format(
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    host=os.environ['MYSQL_HOST'],
    database=os.environ['MYSQL_DATABASE']
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

from utils.db import db  # Importa la instancia de db desde utils/db.py
db.init_app(app)  # Inicializa SQLAlchemy con la aplicación

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from models.user import User
from models.contact import Contact

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importa y registra tus Blueprints
from routes.contacts import contacts
from routes.auth import auth
app.register_blueprint(contacts)
app.register_blueprint(auth)

with app.app_context():
    #db.drop_all()  # Elimina todas las tablas (¡Cuidado! Esto eliminará todos los datos)
    db.create_all()  # Crea las tablas en la base de datos

if __name__ == "__main__":
    app.run(debug=True)