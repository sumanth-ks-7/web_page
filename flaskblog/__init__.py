from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fd8740f98ddd013ce021f5f2bde3c3d7'  # to get secret key in python console type --> import secrets --> secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


from flaskblog import routes

