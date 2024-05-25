from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, session
from flask_session import Session  # Add Flask-Session if not already
import os


load_dotenv()
db = SQLAlchemy()  # Initialize here, but don't bind to an app yet.
oauth = OAuth()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_fallback_secret_key')
    app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem for sessions
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_KEY_PREFIX'] = 'flask_session:'

    db.init_app(app)
    CORS(app, supports_credentials=True)
    oauth.init_app(app)
    Session(app)  # Initialize session management

    google = oauth.register(
        name='google',
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        server_metadata_url=os.getenv("GOOGLE_META_URL"),
        access_token_url='https://oauth2.googleapis.com/token',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        authorize_access_token_params=None,
        authorize_redirect_uri=os.getenv("AUTH_REDIRECT_URI"),
        response_type='code',
        client_kwargs={'scope': 'openid profile email https://www.googleapis.com/auth/user.gender.read https://www.googleapis.com/auth/user.birthday.read'},
    )

    # client_kwargs={'scope': 'openid profile email https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/user.birthday.read'},


    print("creating app")
    with app.app_context():
        from models.user import User
        from models.task import Task
        from models.calendar import Calendar
        from models.event import Event
        from models.notepad import Note
        from models.todo_list import TodoList

        db.create_all()

    from routes.task_routes import tasks_blueprint
    from routes.auth_routes import auth_blueprint
    from routes.calendar_routes import calendars_blueprint
    from routes.event_routes import events_blueprint
    from routes.notepad_routes import notes_blueprint
    from routes.todo_list_routes import todo_lists_blueprint

    app.register_blueprint(tasks_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(calendars_blueprint)
    app.register_blueprint(events_blueprint)
    app.register_blueprint(notes_blueprint)
    app.register_blueprint(todo_lists_blueprint)

    return app