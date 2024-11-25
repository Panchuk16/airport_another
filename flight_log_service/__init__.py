from flask import Flask 
from flight_log_service.extensions import db
from flight_log_service.routes import main
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    
    app.config.from_prefixed_env()

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
    