from flask import render_template,url_for
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


@main.route('/register')
def register():

    '''
    View root page function that returns the register form page and its data
    '''
    form = RegistrationForm()
    
   
    
    return render_template('register.html', title = 'Register', form=form)


@main.route('/login')
def login():

    '''
    View root page function that returns the login form and its data
    '''
    form = LoginForm
    
   
    
    return render_template('login.html', title='Login', form=form)
