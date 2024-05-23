from flask import Blueprint, jsonify, request
from models.notepad import Note
from models.user import User
from app_init import db
from sqlalchemy.orm.exc import NoResultFound
from routes.auth_routes import token_required

notes_blueprint = Blueprint('notes', __name__)

@notes_blueprint.route('/notes', methods=['POST'])
@token_required
def create_note(current_user):
    data = request.get_json()
    try:
        new_note = Note(
            user_id=current_user.id,
            body=data['body']
        )
        db.session.add(new_note)
        db.session.commit()
        return jsonify(new_note.to_dict()), 201
    except Exception as e:
        print(f"Error creating note: {e}")
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@notes_blueprint.route('/notes', methods=['GET'])
@token_required
def get_notes(current_user):
    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date_created).all()
    return jsonify([note.to_dict() for note in notes])

@notes_blueprint.route('/notes/<int:id>', methods=['GET'])
@token_required
def get_note(current_user, id):
    try:
        note = Note.query.filter_by(id=id, user_id=current_user.id).one()
        return jsonify(note.to_dict())
    except NoResultFound:
        return jsonify({"error": "Note not found"}), 404

@notes_blueprint.route('/notes/<int:id>', methods=['PUT'])
@token_required
def update_note(current_user, id):
    data = request.get_json()
    try:
        note = Note.query.filter_by(id=id, user_id=current_user.id).one()
        note.body = data.get('body', note.body)
        db.session.commit()
        return jsonify(note.to_dict())
    except NoResultFound:
        return jsonify({"error": "Note not found"}), 404

@notes_blueprint.route('/notes/<int:id>', methods=['DELETE'])
@token_required
def delete_note(current_user, id):
    try:
        note = Note.query.filter_by(id=id, user_id=current_user.id).one()
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "Note deleted"}), 204
    except NoResultFound:
        return jsonify({"error": "Note not found"}), 404
