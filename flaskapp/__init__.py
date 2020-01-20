#Created by Matas Pieczulis for Michał Jurkun
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_caching import Cache

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Super Secret Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

cache = Cache(config={'CACHE_TYPE': 'simple', "CACHE_DEFAULT_TIMEOUT": 50})
cache.init_app(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskapp import routes
#TODO
    #rejestr2 to rejestr not found
    #notifications

    #RODO
    #Polityka prywartośni
    #login and register spolszczenie
    
    
