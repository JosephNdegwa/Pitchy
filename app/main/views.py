from turtle import title
from flask import render_template,url_for,flash,redirect
from . import main
from app import db, bcrypt
from .forms import RegistrationForm, LoginForm
from ..models import User,Comment
from flask_login import login_user,current_user, logout_user,login_required


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
   
    
    return render_template('index.html')



@main.route('/about')
def about():

    '''
    View root page function that returns the index page and its data
    '''
    
   
    
    return render_template('about.html')


@main.route('/register', methods=['GET','POST'])
def register():

    '''
    View root page function that returns the register form page and its data
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index)'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('main.login'))

    
   
    
    return render_template('register.html', title = 'Register', form=form)


@main.route('/login', methods=['GET','POST'])
def login():

    '''
    View root page function that returns the login form and its data
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index)'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password!','danger')
        

    
   
    return render_template('login.html', title='Login', form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))



@main.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title='Profile')




@main.route("/comment/new")
@login_required
def logout():
    return render_template('pitch.html', title='New Pitch')

