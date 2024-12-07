# init.py

from flask import Flask
from airport_service.extensions import db
from airport_service.routes import main
from dotenv import load_dotenv
from airport_service.users import User
from airport_service.auth import auth_bp
from flask_jwt_extended import JWTManager

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = 'secret'

    JWTManager(app)

    app.config.from_prefixed_env()

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
