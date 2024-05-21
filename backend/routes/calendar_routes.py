# routes/calendar_routes.py
from flask import Blueprint, jsonify, request
from models.calendar import Calendar
from app_init import db
from routes.auth_routes import token_required

calendars_blueprint = Blueprint('calendars', __name__)

@calendars_blueprint.route('/calendars', methods=['POST'])
@token_required
def create_calendar(current_user):
    data = request.get_json()
    try:
        new_calendar = Calendar(
            name=data['name'],
            user_id=current_user.id,
            color=data.get('color')
        )
        db.session.add(new_calendar)
        db.session.commit()
        return jsonify(new_calendar.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@calendars_blueprint.route('/calendars', methods=['GET'])
@token_required
def get_calendars(current_user):
    calendars = Calendar.query.filter_by(user_id=current_user.id).all()
    return jsonify([calendar.to_dict() for calendar in calendars])

@calendars_blueprint.route('/calendars/<int:id>', methods=['GET'])
@token_required
def get_calendar(current_user, id):
    calendar = Calendar.query.filter_by(id=id, user_id=current_user.id).first()
    if calendar:
        return jsonify(calendar.to_dict())
    else:
        return jsonify({"error": "Calendar not found"}), 404

@calendars_blueprint.route('/calendars/<int:id>', methods=['PUT'])
@token_required
def update_calendar(current_user, id):
    data = request.get_json()
    calendar = Calendar.query.filter_by(id=id, user_id=current_user.id).first()
    if calendar:
        calendar.name = data.get('name', calendar.name)
        calendar.color = data.get('color', calendar.color)
        db.session.commit()
        return jsonify(calendar.to_dict())
    else:
        return jsonify({"error": "Calendar not found"}), 404

@calendars_blueprint.route('/calendars/<int:id>', methods=['DELETE'])
@token_required
def delete_calendar(current_user, id):
    calendar = Calendar.query.filter_by(id=id, user_id=current_user.id).first()
    if calendar:
        db.session.delete(calendar)
        db.session.commit()
        return jsonify({"message": "Calendar deleted"}), 204
    else:
        return jsonify({"error": "Calendar not found"}), 404
