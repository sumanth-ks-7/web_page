import os


class Config:
    SECRET_KEY = 'fd8740f98ddd013ce021f5f2bde3c3d7'  # to get secret key in python console type --> import secrets --> secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

