import requests
from test_user import login_user
import sys
import os

# Assuming your script is running from the 'tests' directory and you need to go up two levels to reach the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Define the base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000'

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

# Function to test creating a new todo list
def test_create_todo_list(token):
    url = BASE_URL + '/todo_lists'
    data = {
        'name': 'Test Todo List'
    }
    try:
        response = requests.post(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("New todo list response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error creating todo list: {e}")
        print(f"Response text: {e.response.text}")  # Log the server response for debugging

# Function to test getting all todo lists
def test_get_todo_lists(token):
    url = BASE_URL + '/todo_lists'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("All todo lists:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting todo lists: {e}")

# Function to test getting a specific todo list by ID
def test_get_todo_list(token, todo_list_id):
    url = BASE_URL + f'/todo_lists/{todo_list_id}'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Todo list {todo_list_id} details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting todo list {todo_list_id}: {e}")

# Function to test updating a todo list by ID
def test_update_todo_list(token, todo_list_id, new_name):
    url = BASE_URL + f'/todo_lists/{todo_list_id}'
    data = {
        'name': new_name
    }
    try:
        response = requests.put(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Updated todo list {todo_list_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating todo list {todo_list_id}: {e}")

# Function to test deleting a todo list by ID
def test_delete_todo_list(token, todo_list_id):
    url = BASE_URL + f'/todo_lists/{todo_list_id}'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 204:
            print(f"Deleted todo list {todo_list_id} successfully.")
        else:
            print(f"Deleted todo list {todo_list_id} response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting todo list {todo_list_id}: {e}")

def authenticated_request(token):
    return {'Authorization': f'Bearer {token}'}

# Main function to execute test cases
def main():
    token = login_user('selma', 'pass4selma')
    if token:
        delete_all_todo_lists(token)  # Delete all preexisting todo lists
        todo_list_id = create_predefined_todo_list(token)  # Create a predefined todo list for testing
        test_create_todo_list(token)
        test_get_todo_lists(token)
        if todo_list_id:
            test_get_todo_list(token, todo_list_id)  # Test with the created todo list ID
            test_update_todo_list(token, todo_list_id, 'Updated Todo List Name')
            test_delete_todo_list(token, todo_list_id)

if __name__ == "__main__":
    main()
