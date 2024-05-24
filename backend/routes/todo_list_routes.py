# routes/todo_list_routes.py
from flask import Blueprint, jsonify, request
from models.todo_list import TodoList
from models.user import User
from app_init import db
from sqlalchemy.orm.exc import NoResultFound
from routes.auth_routes import token_required
from datetime import datetime

todo_lists_blueprint = Blueprint('todo_lists', __name__)

@todo_lists_blueprint.route('/todo_lists', methods=['POST'])
@token_required
def create_todo_list(current_user):
    data = request.get_json()
    try:
        new_todo_list = TodoList(
            name=data['name'],
            user_id=current_user.id
        )
        db.session.add(new_todo_list)
        db.session.commit()
        return jsonify(new_todo_list.to_dict()), 201
    except Exception as e:
        print(f"Error creating todo list: {e}")
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@todo_lists_blueprint.route('/todo_lists', methods=['GET'])
@token_required
def get_todo_lists(current_user):
    todo_lists = TodoList.query.filter_by(user_id=current_user.id).order_by(TodoList.date_created).all()
    return jsonify([todo_list.to_dict() for todo_list in todo_lists])

@todo_lists_blueprint.route('/todo_lists/<int:id>', methods=['GET'])
@token_required
def get_todo_list(current_user, id):
    try:
        todo_list = TodoList.query.filter_by(id=id, user_id=current_user.id).one()
        return jsonify(todo_list.to_dict())
    except NoResultFound:
        return jsonify({"error": "Todo list not found"}), 404

@todo_lists_blueprint.route('/todo_lists/<int:id>', methods=['PUT'])
@token_required
def update_todo_list(current_user, id):
    data = request.get_json()
    try:
        todo_list = TodoList.query.filter_by(id=id, user_id=current_user.id).one()
        todo_list.name = data.get('name', todo_list.name)
        db.session.commit()
        return jsonify(todo_list.to_dict())
    except NoResultFound:
        return jsonify({"error": "Todo list not found"}), 404

@todo_lists_blueprint.route('/todo_lists/<int:id>', methods=['DELETE'])
@token_required
def delete_todo_list(current_user, id):
    try:
        todo_list = TodoList.query.filter_by(id=id, user_id=current_user.id).one()
        db.session.delete(todo_list)
        db.session.commit()
        return jsonify({"message": "Todo list deleted"}), 204
    except NoResultFound:
        return jsonify({"error": "Todo list not found"}), 404

@todo_lists_blueprint.route('/todo_lists', methods=['DELETE'])
@token_required
def delete_all_todo_lists(current_user):
    try:
        num_deleted = TodoList.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        return jsonify({"message": f"{num_deleted} todo lists deleted"}), 204
    except Exception as e:
        print(f"Error deleting all todo lists: {e}")
        db.session.rollback()
        return jsonify({"error": f"Failed to delete todo lists: {e}"}), 500

# Register error handlers within blueprint
@todo_lists_blueprint.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@todo_lists_blueprint.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500



# # routes/todo_list_routes.py
# from flask import Blueprint, jsonify, request
# from models.todo_list import TodoList
# from models.user import User
# from app_init import db
# from sqlalchemy.orm.exc import NoResultFound
# from routes.auth_routes import token_required
# from datetime import datetime

# todo_lists_blueprint = Blueprint('todo_lists', __name__)

# @todo_lists_blueprint.route('/todo_lists', methods=['POST'])
# @token_required
# def create_todo_list(current_user):
#     data = request.get_json()
#     try:
#         new_todo_list = TodoList(
#             name=data['name'],
#             user_id=current_user.id
#         )
#         db.session.add(new_todo_list)
#         db.session.commit()
#         return jsonify(new_todo_list.to_dict()), 201
#     except Exception as e:
#         print(f"Error creating todo list: {e}")
#         db.session.rollback()
#         return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# @todo_lists_blueprint.route('/todo_lists', methods=['GET'])
# @token_required
# def get_todo_lists(current_user):
#     todo_lists = TodoList.query.filter_by(user_id=current_user.id).order_by(TodoList.date_created).all()
#     return jsonify([todo_list.to_dict() for todo_list in todo_lists])

# @todo_lists_blueprint.route('/todo_lists/<int:id>', methods=['GET'])
# @token_required
# def get_todo_list(current_user, id):
#     try:
#         todo_list = TodoList.query.filter_by(id=id, user_id=current_user.id).one()
#         return jsonify(todo_list.to_dict())
#     except NoResultFound:
#         return jsonify({"error": "Todo list not found"}), 404

# @todo_lists_blueprint.route('/todo_lists/<int:id>', methods=['PUT'])
# @token_required
# def update_todo_list(current_user, id):
#     data = request.get_json()
#     try:
#         todo_list = TodoList.query.filter_by(id=id, user_id=current_user.id).one()
#         todo_list.name = data.get('name', todo_list.name)
#         db.session.commit()
#         return jsonify(todo_list.to_dict())
#     except NoResultFound:
#         return jsonify({"error": "Todo list not found"}), 404

# @todo_lists_blueprint.route('/todo_lists/<int:id>', methods=['DELETE'])
# @token_required
# def delete_todo_list(current_user, id):
#     try:
#         todo_list = TodoList.query.filter_by(id=id, user_id=current_user.id).one()
#         db.session.delete(todo_list)
#         db.session.commit()
#         return jsonify({"message": "Todo list deleted"}), 204
#     except NoResultFound:
#         return jsonify({"error": "Todo list not found"}), 404

# # Register error handlers within blueprint
# @todo_lists_blueprint.app_errorhandler(404)
# def not_found_error(error):
#     return jsonify({"error": "Not Found"}), 404

# @todo_lists_blueprint.app_errorhandler(500)
# def internal_error(error):
#     return jsonify({"error": "Internal Server Error"}), 500
