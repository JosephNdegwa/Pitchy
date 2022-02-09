import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.urandom(16)
    #config['SECRET_KEY'] = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kariuki_ndegwa:515021@localhost/pitchy'
    
class ProdConfig(Config):
            '''
        Production  configuration child class

        Args:
            Config: The parent configuration class with General configuration settings
            '''
pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}