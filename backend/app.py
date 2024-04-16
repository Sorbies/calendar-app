from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from sqlalchemy.orm.exc import NoResultFound

# Initialize the Flask application
app = Flask(__name__)

# Set the absolute path for the SQLite database
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'tasks.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize SQLAlchemy for database management
db = SQLAlchemy(app)

# Define the Task model for the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        # Convert Task object to a dictionary
        return {
            "id": self.id,
            "content": self.content,
            "date_created": self.date_created.isoformat()
        }

# Create database tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Get JSON data from the request
    data = request.get_json()
    # Create a new Task object
    new_task = Task(content=data['content'])
    # Add the new task to the database session
    db.session.add(new_task)
    # Commit changes to the database
    db.session.commit()
    # Return the newly created task as JSON response
    return jsonify(new_task.to_dict()), 201

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Query all tasks from the database and order by creation date
    tasks = Task.query.order_by(Task.date_created).all()
    # Convert tasks to list of dictionaries and return as JSON
    return jsonify([task.to_dict() for task in tasks])

# Route to get a specific task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    try:
        # Query task by ID or raise NoResultFound if not found
        task = Task.query.filter_by(id=id).one()
        # Return the task as JSON response
        return jsonify(task.to_dict())
    except NoResultFound:
        # Return error message if task with given ID doesn't exist
        return jsonify({"error": "Task not found"}), 404

# Route to update a task by ID
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    # Get JSON data from the request
    data = request.get_json()
    try:
        # Query task by ID or raise NoResultFound if not found
        task = Task.query.filter_by(id=id).one()
        # Update task content
        task.content = data['content']
        # Commit changes to the database
        db.session.commit()
        # Return the updated task as JSON response
        return jsonify(task.to_dict())
    except NoResultFound:
        # Return error message if task with given ID doesn't exist
        return jsonify({"error": "Task not found"}), 404

# Route to delete a task by ID
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        # Query task by ID or raise NoResultFound if not found
        task = Task.query.filter_by(id=id).one()
        # Delete the task from the database
        db.session.delete(task)
        # Commit changes to the database
        db.session.commit()
        # Return success message as JSON response
        return jsonify({"message": "Task deleted"}), 204
    except NoResultFound:
        # Return error message if task with given ID doesn't exist
        return jsonify({"error": "Task not found"}), 404

# Route to delete all tasks
@app.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    # Delete all tasks from the database
    try:
        num_deleted = db.session.query(Task).delete()
        # Commit changes to the database
        db.session.commit()
        # Return success message with number of tasks deleted
        return jsonify({"message": f"{num_deleted} tasks deleted"}), 204
    except Exception as e:
        # Return error message if deletion fails
        return jsonify({"error": f"Failed to delete tasks: {e}"}), 500

# Error handling for 404 errors (Not Found)
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

# Error handling for 500 errors (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)