from flask import Flask 

from app.extensions import db
from app.routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
    