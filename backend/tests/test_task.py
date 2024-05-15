import requests
from test_user import *
#from models.user import User
import sys; 


import sys
import os

# Assuming your script is running from the 'tests' directory and you need to go up two levels to reach the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
print(sys.path)
# from models.user import User  # Now you should be able to import User


# Define the base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000'

# Function to delete all tasks
def delete_all_tasks():
    url = BASE_URL + '/tasks'
    try:
        response = requests.delete(url, headers= authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("All tasks deleted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting tasks: {e}")

# Function to create predefined tasks for testing
def create_predefined_tasks():
    tasks = [
        {'content': 'Task 1: Wash dishes'},
        {'content': 'Task 2: Do laundry'},
        {'content': 'Task 3: Buy groceries'}
    ]
    ids = []
    for task in tasks:
        url = BASE_URL + '/tasks'
        try:
            response = requests.post(url, json=task, headers= authenticated_request(token))
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(f"Task created successfully: {task['content']}")
            ids.append(response.json()['id'])
        except requests.exceptions.RequestException as e:
            print(f"Error creating task: {e}")
    return ids

# Function to test creating a new task
def test_create_task(user):
    url = BASE_URL + '/tasks'
    data = {'content': 'Test Task Content', 'username':user}
    try:
        # print(User.query.filter_by(username = user))
        response = requests.post(url, json=data, headers= authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("New task response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error creating task: {e}")

# Function to test getting all tasks
def test_get_tasks():
    url = BASE_URL + '/tasks'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("All tasks:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting tasks: {e}")

# Function to test getting a specific task by ID
def test_get_task(task_id):
    url = BASE_URL + f'/tasks/{task_id}'
    try:
        response = requests.get(url, headers= authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Task {task_id} details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting task {task_id}: {e}")

# Function to test updating a task by ID
def test_update_task(task_id, new_content):
    url = BASE_URL + f'/tasks/{task_id}'
    data = {'content': new_content}
    try:
        response = requests.put(url, json=data, headers= authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Updated task {task_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating task {task_id}: {e}")

# Function to test deleting a task by ID
def test_delete_task(task_id):
    url = BASE_URL + f'/tasks/{task_id}'
    try:
        response = requests.delete(url, headers= authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Deleted task {task_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error deleting task {task_id}: {e}")

def authenticated_request(token):
     return {'Authorization': f'Bearer {token}'}


# Main function to execute test cases
def main():
    # delete_all_tasks()  # Delete all preexisting tasks
    # ids = create_predefined_tasks()  # Create predefined tasks for testing
    test_create_task(user='newuser')
    test_get_tasks()
    # if ids:
    #     test_get_task(ids[0])  # Test with the first created task ID
    #     test_update_task(ids[0], 'Updated Task Content')
    #     test_delete_task(ids[0])

if __name__ == "__main__":
    token = login_user('newuser', 'password123')
    # if token:
    #     authenticated_request(token)
    main()
