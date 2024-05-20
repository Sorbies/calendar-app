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
    print(data['username'])
    print(User.query.filter_by(username = data['username']))
    print(current_user, '\n\n\n') # print statement
    new_task = Task(content=data['content'], user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

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
        task.content = data['content']
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
        return jsonify({"error": f"Failed to delete tasks: {e}"}), 500

# Register error handlers within blueprint
@tasks_blueprint.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@tasks_blueprint.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500




# # routes/task_routes.py
# from flask import Blueprint, jsonify, request
# from models.task import Task
# from app_init import db
# from sqlalchemy.orm.exc import NoResultFound

# tasks_blueprint = Blueprint('tasks', __name__)


# @tasks_blueprint.route('/tasks', methods=['POST'])
# def create_task():
#     data = request.get_json()
#     new_task = Task(content=data['content'])
#     db.session.add(new_task)
#     db.session.commit()
#     return jsonify(new_task.to_dict()), 201

# @tasks_blueprint.route('/tasks', methods=['GET'])
# def get_tasks():
#     tasks = Task.query.order_by(Task.date_created).all()
#     return jsonify([task.to_dict() for task in tasks])

# @tasks_blueprint.route('/tasks/<int:id>', methods=['GET'])
# def get_task(id):
#     try:
#         task = Task.query.filter_by(id=id).one()
#         return jsonify(task.to_dict())
#     except NoResultFound:
#         return jsonify({"error": "Task not found"}), 404

# @tasks_blueprint.route('/tasks/<int:id>', methods=['PUT'])
# def update_task(id):
#     data = request.get_json()
#     try:
#         task = Task.query.filter_by(id=id).one()
#         task.content = data['content']
#         db.session.commit()
#         return jsonify(task.to_dict())
#     except NoResultFound:
#         return jsonify({"error": "Task not found"}), 404

# @tasks_blueprint.route('/tasks/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     try:
#         task = Task.query.filter_by(id=id).one()
#         db.session.delete(task)
#         db.session.commit()
#         return jsonify({"message": "Task deleted"}), 204
#     except NoResultFound:
#         return jsonify({"error": "Task not found"}), 404

# @tasks_blueprint.route('/tasks', methods=['DELETE'])
# def delete_all_tasks():
#     try:
#         num_deleted = db.session.query(Task).delete()
#         db.session.commit()
#         return jsonify({"message": f"{num_deleted} tasks deleted"}), 204
#     except Exception as e:
#         return jsonify({"error": f"Failed to delete tasks: {e}"}), 500

# # Register error handlers within blueprint
# @tasks_blueprint.app_errorhandler(404)
# def not_found_error(error):
#     return jsonify({"error": "Not Found"}), 404

# @tasks_blueprint.app_errorhandler(500)
# def internal_error(error):
#     return jsonify({"error": "Internal Server Error"}), 500
