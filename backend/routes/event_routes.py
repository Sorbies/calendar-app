# routes/event_routes.py
from flask import Blueprint, jsonify, request
from models.event import Event
from models.calendar import Calendar
from app_init import db
from routes.auth_routes import token_required
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime

events_blueprint = Blueprint('events', __name__)

@events_blueprint.route('/events', methods=['POST'])
@token_required
def create_event(current_user):
    data = request.get_json()
    try:
        new_event = Event(
            user_id=current_user.id,
            calendar_id=data['calendar_id'],
            name=data['name'],
            description=data.get('description'),
            start_date_time=datetime.fromisoformat(data['start_date_time']),
            end_date_time=datetime.fromisoformat(data['end_date_time'])
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@events_blueprint.route('/events', methods=['GET'])
@token_required
def get_events(current_user):
    calendar_id = request.args.get('calendar_id')
    if calendar_id:
        events = Event.query.filter_by(calendar_id=calendar_id, user_id=current_user.id).all()
    else:
        events = Event.query.filter_by(user_id=current_user.id).all()
    return jsonify([event.to_dict() for event in events])

@events_blueprint.route('/events/<int:id>', methods=['GET'])
@token_required
def get_event(current_user, id):
    event = Event.query.filter_by(id=id, user_id=current_user.id).first()
    if event:
        return jsonify(event.to_dict())
    else:
        return jsonify({"error": "Event not found"}), 404

@events_blueprint.route('/events/<int:id>', methods=['PUT'])
@token_required
def update_event(current_user, id):
    data = request.get_json()
    event = Event.query.filter_by(id=id, user_id=current_user.id).first()
    if event:
        event.name = data.get('name', event.name)
        event.description = data.get('description', event.description)
        event.start_date_time = datetime.fromisoformat(data.get('start_date_time', event.start_date_time.isoformat()))
        event.end_date_time = datetime.fromisoformat(data.get('end_date_time', event.end_date_time.isoformat()))
        db.session.commit()
        return jsonify(event.to_dict())
    else:
        return jsonify({"error": "Event not found"}), 404

@events_blueprint.route('/events/<int:id>', methods=['DELETE'])
@token_required
def delete_event(current_user, id):
    event = Event.query.filter_by(id=id, user_id=current_user.id).first()
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted"}), 204
    else:
        return jsonify({"error": "Event not found"}), 404

# New route to get all events from a specific calendar
@events_blueprint.route('/calendars/<int:calendar_id>/events', methods=['GET'])
@token_required
def get_events_by_calendar(current_user, calendar_id):
    try:
        calendar = Calendar.query.filter_by(id=calendar_id, user_id=current_user.id).one()
        events = Event.query.filter_by(calendar_id=calendar.id, user_id=current_user.id).order_by(Event.start_date_time).all()
        return jsonify([event.to_dict() for event in events])
    except NoResultFound:
        return jsonify({"error": "Calendar not found"}), 404
