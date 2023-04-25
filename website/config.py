import os

class Config:
    # Secret key for generating secure cookies
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.getcwd(), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

