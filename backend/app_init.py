from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()  # Initialize here, but don't bind to an app yet.

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_fallback_secret_key')

    db.init_app(app)

    print("creating app")
    with app.app_context():
           # Ensure models are imported before db.create_all()
        from models.user import User
        from models.task import Task
        # from models.password_reset_token import PasswordResetToken

        db.create_all()  # This will now be aware of the User model

    # Import blueprints after model and database initialization
    from routes.task_routes import tasks_blueprint
    from routes.auth_routes import auth_blueprint
    app.register_blueprint(tasks_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

