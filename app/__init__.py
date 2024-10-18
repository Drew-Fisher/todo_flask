from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints (later, if you modularize your routes)
    from app.routes import main, board_blueprint
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(board_blueprint, url_prefix='/board')

    return app