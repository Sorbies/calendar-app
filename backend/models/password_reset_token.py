# # models/password_reset_token.py
# from datetime import datetime, timedelta
# from app_init import db
# from werkzeug.security import generate_password_hash, check_password_hash


# class PasswordResetToken(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     token = db.Column(db.String(256), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

#     def hash_token(self, token):
#         self.token = generate_password_hash(token)

#     def check_token(self, token):
#         return check_password_hash(self.token, token)

#     # @property
#     # def is_expired(self):
#     #     return datetime.utcnow() > self.created_at + timedelta(seconds=600)  # 10 minutes

#     def save(self):
#         if self.token:
#             self.hash_token(self.token)
#         db.session.add(self)
#         db.session.commit()

#     def verify_token(self, token):
#         if not self.is_expired:
#             return self.check_token(token)
#         return False
