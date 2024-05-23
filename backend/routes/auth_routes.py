# routes/auth_routes.py
from flask import Blueprint, request, jsonify, current_app
from models.user import User
from app_init import db
from functools import wraps

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



# # routes/auth_routes.py
# from flask import Blueprint, request, jsonify, current_app
# from models.user import User
# from app_init import db
# from functools import wraps

# auth_blueprint = Blueprint('auth', __name__)

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 403
#         try:
#             token = token.split(" ")[1]  # Assuming token prefixed with "Bearer "
#             current_user = User.verify_token(token)
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 403
#         return f(current_user, *args, **kwargs)
#     return decorated

# @auth_blueprint.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
#         return jsonify({'error': 'Username or Email already in use'}), 409
#     user = User(username=data['username'], email=data['email'])
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({
#         'message': 'User registered successfully',
#         'user_id': user.id
#     }), 201

# @auth_blueprint.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.get_json()
#         user = User.query.filter_by(username=data['username']).first()
#         if user and user.check_password(data['password']):
#             token = user.generate_token()
#             return jsonify({'message': 'Login successful', 'token': token}), 200
#         return jsonify({'error': 'Invalid username or password'}), 401
#     except Exception as e:
#         return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

# @auth_blueprint.route('/secured_route')
# @token_required
# def secured_route(current_user):
#     return jsonify({
#         'message': 'Congratulations! You have accessed a protected route.',
#         'user': current_user.username
#     })




# # routes/auth_routes.py
# from flask import Blueprint, request, jsonify, current_app
# from models.user import User
# from app_init import db
# from functools import wraps

# auth_blueprint = Blueprint('auth', __name__)

# @auth_blueprint.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
#         return jsonify({'error': 'Username or Email already in use'}), 409
#     user = User(username=data['username'], email=data['email'])
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({
#         'message': 'User registered successfully',
#         'user_id': user.id
#     }), 201

# @auth_blueprint.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.get_json()
#         user = User.query.filter_by(username=data['username']).first()
#         if user and user.check_password(data['password']):
#             token = user.generate_token()
#             return jsonify({'message': 'Login successful', 'token': token}), 200
#         return jsonify({'error': 'Invalid username or password'}), 401
#     except Exception as e:
#         # Log the error and return a message
#         return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500






# # routes/auth_routes.py
# from flask import Blueprint, request, jsonify
# from models.user import User
# from app_init import db


# auth_blueprint = Blueprint('auth', __name__)

# @auth_blueprint.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     print("data:", data)
#     if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
#         return jsonify({'error': 'Username or Email already in use'}), 409
#     user = User(username=data['username'], email=data['email'])
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201

# @auth_blueprint.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(username=data['username']).first()
#     if user and user.check_password(data['password']):
#         return jsonify({'message': 'Login successful'}), 200
#     return jsonify({'error': 'Invalid username or password'}), 401
