from app_init import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    start_date_time = db.Column(db.DateTime, nullable=False)
    end_date_time = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref=db.backref('events', lazy=True))
    calendar = db.relationship('Calendar', back_populates='events')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "calendar_id": self.calendar_id,
            "name": self.name,
            "description": self.description,
            "start_date_time": self.start_date_time.isoformat(),
            "end_date_time": self.end_date_time.isoformat()
        }


