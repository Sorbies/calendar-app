# routes/auth_routes.py
from flask import Blueprint, request, jsonify, current_app, redirect, url_for, session
from models.user import User
from app_init import db, oauth
from functools import wraps
import uuid


auth_blueprint = Blueprint('auth', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            token = token.split(" ")[1]  # Assuming token is prefixed with "Bearer "
            current_user = User.verify_token(token)
            if current_user is None:
                return jsonify({'message': 'Token is invalid'}), 403
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Username or Email already in use'}), 409
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'message': 'User registered successfully',
        'user_id': user.id
    }), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = user.generate_token()
            return jsonify({'message': 'Login successful', 'token': token}), 200
        return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@auth_blueprint.route('/secured_route')
@token_required
def secured_route(current_user):
    return jsonify({
        'message': 'Congratulations! You have accessed a protected route.',
        'user': current_user.username
    })

@auth_blueprint.route('/login/google')
def login_google():
    google = oauth.create_client('google')
    redirect_uri = url_for('auth.auth_google', _external=True)
    state = oauth.google.authorize_redirect(redirect_uri)
    current_app.logger.info(f"State sent: {state}")
    return state


@auth_blueprint.route('/google')
def auth_google():
    try:
        google = oauth.create_client('google')
        state = request.args.get('state')
        current_app.logger.info(f"State received: {state}")
        token = google.authorize_access_token()
        resp = google.get('https://www.googleapis.com/oauth2/v3/userinfo')
        user_info = resp.json()
        current_app.logger.info(f"User info received: {user_info}")

        if 'email' not in user_info:
            raise ValueError("Email not found in user info")

        session['email'] = user_info['email']

        # Handle user registration/login in your database
        user = User.query.filter_by(email=user_info['email']).first()
        if not user:
            user = User(username=user_info['email'], email=user_info['email'])
            db.session.add(user)
            db.session.commit()

        token = user.generate_token()
        return redirect(f'http://localhost:3000/dashboard?token={token}')
    except Exception as e:
        current_app.logger.error(f"Error in auth_google: {e}")
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@auth_blueprint.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@auth_blueprint.route('/google-callback')
def google_callback():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    
    # Fetch user data from Google People API
    resp = google.get('https://people.googleapis.com/v1/people/me?personFields=genders,birthdays', token=token)
    user_info = resp.json()
    
    session['user'] = {
        'token': token,
        'userinfo': user_info
    }
    
    return redirect(url_for('auth.home'))