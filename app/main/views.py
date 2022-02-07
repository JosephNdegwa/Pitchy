from flask import render_template,url_for
from . import main 


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
