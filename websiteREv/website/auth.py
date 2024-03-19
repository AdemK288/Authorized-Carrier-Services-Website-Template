from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='Success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Email/Password does not match, please try again', category='Error')
        else:
            flash('Email does not exist, Would you like to create an account?', category='Error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if email == '':
            flash('Please fill in the required fields', category='Error')
        elif first_name == '':
            flash('Please fill in the required fields', category='Error')
        elif password1 == '':
            flash('Please fill in the required fields', category='Error')
        elif password2 == '':
            flash('Please fill in the required fields', category='Error')
        elif len(email) < 4:
            flash('Invalid Email', category='Error')
            if user:
                flash('Email already exists, please use a different email', category='Error')
        elif len(first_name) < 1:
            flash('First Name must be greater than one character', category='Error')
        elif len(password1) < 6:
            flash('Password must be greater than 6 characters', category='Error')
        elif password1 != password2:
            flash('Passwords do not match', category='Error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account successfully created!', category='Success')
            return redirect(url_for('views.home'))


            #send information to database
            
    return render_template("sign_up.html", user=current_user)