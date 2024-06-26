# routes/task_routes.py
from flask import Blueprint, jsonify, request
from models.task import Task
from models.todo_list import TodoList
from models.user import User
from app_init import db
from sqlalchemy.orm.exc import NoResultFound
from routes.auth_routes import token_required
from datetime import datetime

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    try:
        start_date_time = datetime.fromisoformat(data['start_date_time'])
        end_date_time = datetime.fromisoformat(data['end_date_time'])
        todo_list = TodoList.query.filter_by(id=data['todo_list_id'], user_id=current_user.id).one()
        new_task = Task(
            title=data['title'],
            content=data['content'],
            user_id=current_user.id,
            todo_list_id=todo_list.id,
            completed=data.get('completed', False),
            start_date_time=start_date_time,
            end_date_time=end_date_time
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except NoResultFound:
        return jsonify({"error": "Todo list not found"}), 404
    except Exception as e:
        print(f"Error creating task: {e}")
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@tasks_blueprint.route('/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    tasks = Task.query.join(TodoList).filter(TodoList.user_id == current_user.id).order_by(Task.date_created).all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_blueprint.route('/tasks/<int:id>', methods=['GET'])
@token_required
def get_task(current_user, id):
    try:
        task = Task.query.join(TodoList).filter(Task.id == id, TodoList.user_id == current_user.id).one()
        return jsonify(task.to_dict())
    except NoResultFound:
        return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks/<int:id>', methods=['PUT'])
@token_required
def update_task(current_user, id):
    data = request.get_json()
    try:
        task = Task.query.join(TodoList).filter(Task.id == id, TodoList.user_id == current_user.id).one()
        task.title = data.get('title', task.title)
        task.content = data.get('content', task.content)
        task.completed = data.get('completed', task.completed)
        if 'start_date_time' in data:
            task.start_date_time = datetime.fromisoformat(data['start_date_time'])
        if 'end_date_time' in data:
            task.end_date_time = datetime.fromisoformat(data['end_date_time'])
        db.session.commit()
        return jsonify(task.to_dict())
    except NoResultFound:
        return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks/<int:id>', methods=['DELETE'])
@token_required
def delete_task(current_user, id):
    try:
        task = Task.query.join(TodoList).filter(Task.id == id, TodoList.user_id == current_user.id).one()
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 204
    except NoResultFound:
        return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks', methods=['DELETE'])
@token_required
def delete_all_tasks(current_user):
    try:
        num_deleted = Task.query.join(TodoList).filter(TodoList.user_id == current_user.id).delete()
        db.session.commit()
        return jsonify({"message": f"{num_deleted} tasks deleted"}), 204
    except Exception as e:
        print(f"Error deleting all tasks: {e}")
        db.session.rollback()
        return jsonify({"error": f"Failed to delete tasks: {e}"}), 500

# New route to get all tasks from a specific todo list
@tasks_blueprint.route('/todo_lists/<int:todo_list_id>/tasks', methods=['GET'])
@token_required
def get_tasks_by_todo_list(current_user, todo_list_id):
    try:
        todo_list = TodoList.query.filter_by(id=todo_list_id, user_id=current_user.id).one()
        tasks = Task.query.filter_by(todo_list_id=todo_list.id).order_by(Task.date_created).all()
        return jsonify([task.to_dict() for task in tasks])
    except NoResultFound:
        return jsonify({"error": "Todo list not found"}), 404

# Register error handlers within blueprint
@tasks_blueprint.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@tasks_blueprint.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500



