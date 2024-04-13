from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    # __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendars.id'))
    name = db.Column(db.String)
    description = db.Column(db.String)
    date_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

    # Define relationship to Calendar
    calendar = db.relationship("Calendar", back_populates="events")

# class Calendar(db.Model):
#     __tablename__ = 'calendars'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)

#     # Define relationship to Event
#     events = db.relationship("Event", back_populates="calendar")

