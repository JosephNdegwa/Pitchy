from crypt import methods
from flask import render_template,url_for,flash,redirect
from . import main 
from .forms import RegistrationForm, LoginForm


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
    form = RegistrationForm()
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.index'))

    
   
    
    return render_template('register.html', title = 'Register', form=form)


@main.route('/login', methods=['GET','POST'])
def login():

    '''
    View root page function that returns the login form and its data
    '''
    form = LoginForm()
    if form.validate_on_submit():
        return

    
   
    
    return render_template('login.html', title='Login', form=form)
