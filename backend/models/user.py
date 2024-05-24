# models/user.py
from datetime import datetime, timedelta
from app_init import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ForeignKey to the User model
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_token(self, expires_in=86400):
        payload = {
            'id': self.id,
            'exp': datetime.utcnow() + timedelta(seconds=expires_in),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token  # Decode the token before returning


    def verify_token(token):
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            return User.query.get(payload['id'])
        except jwt.PyJWTError as e:
            return None

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }




