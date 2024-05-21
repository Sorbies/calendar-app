from app_init import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    date_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)  # Duration in minutes

    calendar = db.relationship('Calendar', backref=db.backref('events', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "calendar_id": self.calendar_id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.isoformat(),
            "duration": self.duration
        }

class RecurringEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    start_date_time = db.Column(db.DateTime, nullable=False)
    end_date_time = db.Column(db.DateTime, nullable=False)
    recurrence_rule = db.Column(db.String(200))  # e.g., "FREQ=DAILY;INTERVAL=1"

    # FREQ: Frequency of recurrence (e.g., DAILY, WEEKLY, MONTHLY, YEARLY).
    # INTERVAL: The interval between each occurrence (default is 1).
    # UNTIL: The end date of the recurrence (can also be specified by COUNT).
    # COUNT: The number of occurrences.
    # BYDAY: Specific days of the week (e.g., MO for Monday, TU for Tuesday).
    # BYMONTHDAY: Specific days of the month (e.g., 1 for the first day of the month).
    # BYYEARDAY: Specific days of the year (e.g., 1 for the first day of the year).

    calendar = db.relationship('Calendar', backref=db.backref('recurring_events', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "calendar_id": self.calendar_id,
            "name": self.name,
            "description": self.description,
            "start_date_time": self.start_date_time.isoformat(),
            "end_date_time": self.end_date_time.isoformat(),
            "recurrence_rule": self.recurrence_rule
        }
