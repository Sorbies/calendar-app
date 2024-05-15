# models/task.py
from app_init import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ForeignKey to the User model
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to User
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
            "date_created": self.date_created.isoformat()
        }






# # models/task.py
# from app_init import db
# from datetime import datetime

# class Task(db.Model):
#     #@authentication
#     #foreign key for all tables
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "content": self.content,
#             "date_created": self.date_created.isoformat()
#         }
