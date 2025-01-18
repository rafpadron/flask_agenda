from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from flask_login import current_user, login_required
from utils.db import db


contacts = Blueprint("contacts", __name__)


@contacts.route('/contacts')
@login_required
def index():
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    print(contacts)
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
@login_required
def add_contact():
    if request.method == 'POST':

        # receive data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # create a new Contact object
        new_contact = Contact(user_id=current_user.id, fullname=fullname, email=email, phone=phone)

        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))


@contacts.route("/update/<string:id>", methods=["GET", "POST"])
@login_required
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>", methods=["GET"])
@login_required
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))


@contacts.route("/about")
@login_required
def about():
    return render_template("about.html")