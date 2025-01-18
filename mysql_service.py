from models.user import User
from utils.db import db
from icecream import ic 

def insert_user(username, password, fullname):
    ic('insert')
    user = User(username, password, fullname)
    db.session.add(user)
    ic(user)
    db.session.commit()

def get_user(username):
    user = User.query.filter_by(username=username).first()
    ic(user)
    return user

def to_dict(obj):
    diccionario = [u.__dict__ for u in obj]
    return diccionario