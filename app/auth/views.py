from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import User
from ..auth import auth
from app.auth import forms
from app import db
from ..email import mail_message

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # go back to homepage if the user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    
    # create instance of login form to be passed in to template
    form = forms.LoginForm()

    # handle post response from form and do validation
    if form.validate_on_submit():
        # check users table for user with form username data 
        user = User.query.filter_by(username=form.username.data).first()
        
        # if there's no user in users table or the password is wrong
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        # if no problems then login in the user with remember data included
        login_user(user, remember=form.remember_me.data)

        # redirect to home - TODO - change to posts route
        return redirect(url_for('auth.index')) 

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    # go back to homepage if the user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = forms.SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are now signed up!")
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)

