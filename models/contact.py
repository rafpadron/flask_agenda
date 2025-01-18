from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utils.db import db

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)  # Asegúrate de que la clave foránea referencia la tabla 'user'

    user = relationship('User', back_populates='contacts')