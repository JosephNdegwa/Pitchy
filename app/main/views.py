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
def regiater():

    '''
    View root page function that returns the register page and its data
    '''
    
   
    
    return render_template('register.html')


@main.route('/login')
def login():

    '''
    View root page function that returns the login page and its data
    '''
    
   
    
    return render_template('login.html')
