# test_task.py
import requests
from test_user import login_user
import sys
import os

# Assuming your script is running from the 'tests' directory and you need to go up two levels to reach the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Define the base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000'

# Function to delete all tasks
def delete_all_tasks(token):
    url = BASE_URL + '/tasks'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        if response.status_code == 204:
            print("All tasks deleted successfully.")
        elif response.status_code == 200:
            print(f"Deleted tasks response: {response.json()}")
        else:
            response.raise_for_status()  # Raise an exception for unexpected HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error deleting tasks: {e}")

# Function to delete all todo lists
def delete_all_todo_lists(token):
    url = BASE_URL + '/todo_lists'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        if response.status_code == 204:
            print("All todo lists deleted successfully.")
        elif response.status_code == 200:
            print(f"Deleted todo lists response: {response.json()}")
        else:
            response.raise_for_status()  # Raise an exception for unexpected HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error deleting todo lists: {e}")

# Function to create a predefined todo list for testing
def create_predefined_todo_list(token):
    todo_list = {
        'name': 'Household Chores'
    }
    url = BASE_URL + '/todo_lists'
    try:
        response = requests.post(url, json=todo_list, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Todo list created successfully: {todo_list['name']}")
        return response.json()['id']
    except requests.exceptions.RequestException as e:
        print(f"Error creating todo list: {e}")
        print(f"Response text: {e.response.text}")  # Log the server response for debugging
    return None

# Function to create predefined tasks for testing
def create_predefined_tasks(token, todo_list_id):
    tasks = [
        {
            'title': 'Dishwashing',
            'content': 'Task 1: Wash dishes',
            'completed': False,
            'start_date_time': '2024-05-30T09:00:00',
            'end_date_time': '2024-05-30T10:00:00',
            'todo_list_id': todo_list_id
        },
    ]
    ids = []
    for task in tasks:
        url = BASE_URL + '/tasks'
        try:
            response = requests.post(url, json=task, headers=authenticated_request(token))
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(f"Task created successfully: {task['content']}")
            ids.append(response.json()['id'])
        except requests.exceptions.RequestException as e:
            print(f"Error creating task: {e}")
            print(f"Response text: {e.response.text}")  # Log the server response for debugging
    return ids

# Function to test creating a new task
def test_create_task(token, todo_list_id):
    url = BASE_URL + '/tasks'
    data = {
        'title': 'Test Task',
        'content': 'Test Task Content',
        'completed': False,
        'start_date_time': '2024-06-01T09:00:00',
        'end_date_time': '2024-06-01T10:00:00',
        'todo_list_id': todo_list_id
    }
    try:
        response = requests.post(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("New task response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error creating task: {e}")
        print(f"Response text: {e.response.text}")  # Log the server response for debugging

# Function to test getting all tasks
def test_get_tasks(token):
    url = BASE_URL + '/tasks'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("All tasks:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting tasks: {e}")

# Function to test getting a specific task by ID
def test_get_task(token, task_id):
    url = BASE_URL + f'/tasks/{task_id}'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Task {task_id} details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting task {task_id}: {e}")

# Function to test updating a task by ID
def test_update_task(token, task_id, new_title, new_content, completed):
    url = BASE_URL + f'/tasks/{task_id}'
    data = {
        'title': new_title,
        'content': new_content,
        'completed': completed,
        'start_date_time': '2024-06-01T09:00:00',
        'end_date_time': '2024-06-01T10:00:00'
    }
    try:
        response = requests.put(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Updated task {task_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating task {task_id}: {e}")

# Function to test deleting a task by ID
def test_delete_task(token, task_id):
    url = BASE_URL + f'/tasks/{task_id}'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 204:
            print(f"Deleted task {task_id} successfully.")
        else:
            print(f"Deleted task {task_id} response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting task {task_id}: {e}")

def authenticated_request(token):
    return {'Authorization': f'Bearer {token}'}

# Main function to execute test cases
def main():
    token = login_user('selma', 'pass4selma')
    if token:
        delete_all_tasks(token)  # Delete all preexisting tasks
        delete_all_todo_lists(token)  # Delete all preexisting todo lists
        todo_list_id = create_predefined_todo_list(token)  # Create a predefined todo list for testing
        if todo_list_id:
            create_predefined_tasks(token, todo_list_id)  # Create predefined tasks for testing
            test_create_task(token, todo_list_id)
            test_get_tasks(token)
            task_id = todo_list_id  # Use the first created task ID for testing
            test_get_task(token, task_id)
            test_update_task(token, task_id, 'Updated Task Title', 'Updated Task Content', True)
            test_delete_task(token, task_id)

if __name__ == "__main__":
    main()

