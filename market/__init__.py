from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@localhost/website"
app.config['SECRET_KEY']= getenv('SECRET_KEY')
'''
app.config['SQLALCHEMY_DATABASE_URI'] =
engine:[//[user[:password]@][host]/[dbname]]
'''
db =  SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category="info"

from market import routes
