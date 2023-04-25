from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate, upgrade

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()





def create_app():
    """
    Function to initialize the Flask app
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.routes import bp as main_bp
    from app.routes_auth import bp as auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        upgrade()

    return app
