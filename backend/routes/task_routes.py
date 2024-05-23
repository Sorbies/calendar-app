from flask import Blueprint, jsonify, request
from models.task import Task
from models.user import User  # Ensure the User model is imported if needed
from app_init import db
from sqlalchemy.orm.exc import NoResultFound
from routes.auth_routes import token_required  # Import the token_required decorator

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    try:
        new_task = Task(
            title=data['title'],  # Add title to task creation
            content=data['content'],
            user_id=current_user.id,
            completed=data.get('completed', False)  # Default to False if not provided
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except Exception as e:
        print(f"Error creating task: {e}")  # Log the error
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@tasks_blueprint.route('/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.date_created).all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_blueprint.route('/tasks/<int:id>', methods=['GET'])
@token_required
def get_task(current_user, id):
    try:
        task = Task.query.filter_by(id=id, user_id=current_user.id).one()
        return jsonify(task.to_dict())
    except NoResultFound:
        return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks/<int:id>', methods=['PUT'])
@token_required
def update_task(current_user, id):
    data = request.get_json()
    try:
        task = Task.query.filter_by(id=id, user_id=current_user.id).one()
        task.title = data.get('title', task.title)  # Add title to task update
        task.content = data.get('content', task.content)
        task.completed = data.get('completed', task.completed)
        db.session.commit()
        return jsonify(task.to_dict())
    except NoResultFound:
        return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks/<int:id>', methods=['DELETE'])
@token_required
def delete_task(current_user, id):
    try:
        task = Task.query.filter_by(id=id, user_id=current_user.id).one()
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 204
    except NoResultFound:
        return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks', methods=['DELETE'])
@token_required
def delete_all_tasks(current_user):
    try:
        num_deleted = db.session.query(Task).filter_by(user_id=current_user.id).delete()
        db.session.commit()
        return jsonify({"message": f"{num_deleted} tasks deleted"}), 204
    except Exception as e:
        print(f"Error deleting all tasks: {e}")  # Log the error
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": f"Failed to delete tasks: {e}"}), 500

# Register error handlers within blueprint
@tasks_blueprint.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@tasks_blueprint.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500




