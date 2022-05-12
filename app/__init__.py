from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from forms import validators

app = Flask(__name__)

app.config['SECRET_KEY'] = '76bfd1aa0261f9781a899f00d901908c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes
