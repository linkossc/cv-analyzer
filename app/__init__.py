from flask import Flask
from pymongo import MongoClient
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize MongoDB
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client[app.config['MONGO_DB']]

    # Register routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app