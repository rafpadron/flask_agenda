from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('contacts.index'))
        else:
            flash('Incorrect username or password')
            return render_template('login.html')
    else:
        return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], salt_length=5)
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!')
        return redirect(url_for('auth.login'))
    else:
        return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
