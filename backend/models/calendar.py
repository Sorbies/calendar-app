from app_init import db


class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50))

    user = db.relationship('User', backref=db.backref('calendars', lazy=True))
    # events = db.relationship('Event', backref='calendar', lazy=True)
    events = db.relationship('Event', back_populates='calendar', lazy=True)
    # recurring_events = db.relationship('RecurringEvent', backref='calendar', lazy=True)


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "color": self.color
        }
