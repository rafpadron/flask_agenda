from flask_login import UserMixin
from utils.db import db
from werkzeug.security import check_password_hash
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(100))

    contacts = relationship('Contact', back_populates='user')
    
    def __init__(self, username, password, fullname=""):

        self.username = username
        self.password = password
        self.fullname = fullname
    
    @classmethod
    def check_password(self, hashed_password, password):
        ic('check_password')
        return check_password_hash(hashed_password, password)