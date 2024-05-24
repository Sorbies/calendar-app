from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
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
    CORS(app, supports_credentials=True)

    oauth = OAuth(app)

    google = oauth.register(
        name='google',
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        server_metadata_url=os.getenv("GOOGLE_META_URL"),
        access_token_url='https://oauth2.googleapis.com/token',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        authorize_access_token_params=None,
        authorize_redirect_uri=os.getenv("AUTH_REDIRECT_URI") or "http://127.0.0.1:5000/auth/google",
        response_type='code',
        client_kwargs={'scope': 'openid profile  https://www.googleapis.com/auth/user.email.read https://www.googleapis.com/auth/user.birthday.read'},
    )

   

    print("creating app")
    with app.app_context():
           # Ensure models are imported before db.create_all()
        from models.user import User
        from models.task import Task
        from models.calendar import Calendar
        from models.event import Event #RecurringEvent
        from models.notepad import Note
        from models.todo_list import TodoList
  
        # from models.password_reset_token import PasswordResetToken

        db.create_all()  # This will now be aware of the User model

    # Import blueprints after model and database initialization
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

