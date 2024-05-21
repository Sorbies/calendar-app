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

# Function to create predefined tasks for testing
def create_predefined_tasks(token):
    tasks = [
        {'content': 'Task 1: Wash dishes', 'username': 'rana', 'completed': False},
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
def test_create_task(token, user):
    url = BASE_URL + '/tasks'
    data = {'content': 'Test Task Content', 'username': user, 'completed': False}
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
def test_update_task(token, task_id, new_content, completed):
    url = BASE_URL + f'/tasks/{task_id}'
    data = {'content': new_content, 'completed': completed}
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
    token = login_user('rana', 'pass4rana')
    if token:
        delete_all_tasks(token)  # Delete all preexisting tasks
        ids = create_predefined_tasks(token)  # Create predefined tasks for testing
        test_create_task(token, user='rana')
        test_get_tasks(token)
        if ids:
            task_id = ids[0]  # Use the first created task ID
            test_get_task(token, task_id)  # Test with the first created task ID
            test_update_task(token, task_id, 'Updated Task Content', True)
            test_delete_task(token, task_id)

if __name__ == "__main__":
    main()


