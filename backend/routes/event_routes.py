# routes/event_routes.py
from flask import Blueprint, jsonify, request
from models.event import Event, RecurringEvent
from models.calendar import Calendar
from app_init import db
from routes.auth_routes import token_required
from datetime import datetime

events_blueprint = Blueprint('events', __name__)

@events_blueprint.route('/events', methods=['POST'])
@token_required
def create_event(current_user):
    data = request.get_json()
    try:
        new_event = Event(
            calendar_id=data['calendar_id'],
            name=data['name'],
            description=data.get('description'),
            date_time=datetime.fromisoformat(data['date_time']),
            duration=data['duration']
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
        events = Event.query.filter_by(calendar_id=calendar_id).all()
    else:
        events = Event.query.join(Calendar).filter(Calendar.user_id == current_user.id).all()
    return jsonify([event.to_dict() for event in events])

@events_blueprint.route('/events/<int:id>', methods=['GET'])
@token_required
def get_event(current_user, id):
    event = Event.query.join(Calendar).filter(Event.id == id, Calendar.user_id == current_user.id).first()
    if event:
        return jsonify(event.to_dict())
    else:
        return jsonify({"error": "Event not found"}), 404

@events_blueprint.route('/events/<int:id>', methods=['PUT'])
@token_required
def update_event(current_user, id):
    data = request.get_json()
    event = Event.query.join(Calendar).filter(Event.id == id, Calendar.user_id == current_user.id).first()
    if event:
        event.name = data.get('name', event.name)
        event.description = data.get('description', event.description)
        event.date_time = datetime.fromisoformat(data.get('date_time', event.date_time.isoformat()))
        event.duration = data.get('duration', event.duration)
        db.session.commit()
        return jsonify(event.to_dict())
    else:
        return jsonify({"error": "Event not found"}), 404

@events_blueprint.route('/events/<int:id>', methods=['DELETE'])
@token_required
def delete_event(current_user, id):
    event = Event.query.join(Calendar).filter(Event.id == id, Calendar.user_id == current_user.id).first()
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted"}), 204
    else:
        return jsonify({"error": "Event not found"}), 404

@events_blueprint.route('/recurring_events', methods=['POST'])
@token_required
def create_recurring_event(current_user):
    data = request.get_json()
    try:
        new_recurring_event = RecurringEvent(
            calendar_id=data['calendar_id'],
            name=data['name'],
            description=data.get('description'),
            start_date_time=datetime.fromisoformat(data['start_date_time']),
            end_date_time=datetime.fromisoformat(data['end_date_time']),
            recurrence_rule=data['recurrence_rule']
        )
        db.session.add(new_recurring_event)
        db.session.commit()
        
        # Example: Generate the next 5 occurrences
        rrule = rrulestr(new_recurring_event.recurrence_rule, dtstart=new_recurring_event.start_date_time)
        occurrences = list(rrule)[:5]
        occurrences_str = [occurrence.isoformat() for occurrence in occurrences]

        return jsonify({
            "recurring_event": new_recurring_event.to_dict(),
            "occurrences": occurrences_str
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@events_blueprint.route('/recurring_events', methods=['GET'])
@token_required
def get_recurring_events(current_user):
    calendar_id = request.args.get('calendar_id')
    if calendar_id:
        recurring_events = RecurringEvent.query.filter_by(calendar_id=calendar_id).all()
    else:
        recurring_events = RecurringEvent.query.join(Calendar).filter(Calendar.user_id == current_user.id).all()
    return jsonify([recurring_event.to_dict() for recurring_event in recurring_events])

@events_blueprint.route('/recurring_events/<int:id>', methods=['GET'])
@token_required
def get_recurring_event(current_user, id):
    recurring_event = RecurringEvent.query.join(Calendar).filter(RecurringEvent.id == id, Calendar.user_id == current_user.id).first()
    if recurring_event:
        return jsonify(recurring_event.to_dict())
    else:
        return jsonify({"error": "Recurring event not found"}), 404

@events_blueprint.route('/recurring_events/<int:id>', methods=['PUT'])
@token_required
def update_recurring_event(current_user, id):
    data = request.get_json()
    recurring_event = RecurringEvent.query.join(Calendar).filter(RecurringEvent.id == id, Calendar.user_id == current_user.id).first()
    if recurring_event:
        recurring_event.name = data.get('name', recurring_event.name)
        recurring_event.description = data.get('description', recurring_event.description)
        recurring_event.start_date_time = datetime.fromisoformat(data.get('start_date_time', recurring_event.start_date_time.isoformat()))
        recurring_event.end_date_time = datetime.fromisoformat(data.get('end_date_time', recurring_event.end_date_time.isoformat()))
        recurring_event.recurrence_rule = data.get('recurrence_rule', recurring_event.recurrence_rule)
        db.session.commit()
        return jsonify(recurring_event.to_dict())
    else:
        return jsonify({"error": "Recurring event not found"}), 404

@events_blueprint.route('/recurring_events/<int:id>', methods=['DELETE'])
@token_required
def delete_recurring_event(current_user, id):
    recurring_event = RecurringEvent.query.join(Calendar).filter(RecurringEvent.id == id, Calendar.user_id == current_user.id).first()
    if recurring_event:
        db.session.delete(recurring_event)
        db.session.commit()
        return jsonify({"message": "Recurring event deleted"}), 204
    else:
        return jsonify({"error": "Recurring event not found"}), 404
