import requests

# Define the base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000'

# Function to delete all tasks
def delete_all_tasks():
    url = BASE_URL + '/tasks'
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("All tasks deleted successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting tasks: {e}")

# Function to create predefined tasks for testing
def create_predefined_tasks():
    tasks = [
        {'content': 'Task 1: Wash dishes'},
        {'content': 'Task 2: Do laundry'},
        {'content': 'Task 3: Buy groceries'}
    ]
    for task in tasks:
        url = BASE_URL + '/tasks'
        try:
            response = requests.post(url, json=task)
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(f"Task created successfully: {task['content']}")
        except requests.exceptions.RequestException as e:
            print(f"Error creating task: {e}")

# Function to test creating a new task
def test_create_task():
    url = BASE_URL + '/tasks'
    data = {'content': 'Test Task Content'}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())  # Print the response
    except requests.exceptions.RequestException as e:
        print(f"Error creating task: {e}")

# Function to test getting all tasks
def test_get_tasks():
    url = BASE_URL + '/tasks'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())  # Print the response
    except requests.exceptions.RequestException as e:
        print(f"Error getting tasks: {e}")

# Function to test getting a specific task by ID
def test_get_task(task_id):
    url = BASE_URL + f'/tasks/{task_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())  # Print the response
    except requests.exceptions.RequestException as e:
        print(f"Error getting task: {e}")

# Function to test updating a task by ID
def test_update_task(task_id, new_content):
    url = BASE_URL + f'/tasks/{task_id}'
    data = {'content': new_content}
    try:
        response = requests.put(url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())  # Print the response
    except requests.exceptions.RequestException as e:
        print(f"Error updating task: {e}")

# Function to test deleting a task by ID
def test_delete_task(task_id):
    url = BASE_URL + f'/tasks/{task_id}'
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())  # Print the response
    except requests.exceptions.RequestException as e:
        print(f"Error deleting task: {e}")

# Main function to execute test cases
def main():
    delete_all_tasks()  # Delete all preexisting tasks
    create_predefined_tasks()  # Create predefined tasks for testing
    test_create_task()
    test_get_tasks()
    test_get_task(3)  # Provide an existing task ID to test
    test_update_task(3, 'Updated Task Content')  # Provide an existing task ID and new content to test
    test_delete_task(3)  # Provide an existing task ID to test

if __name__ == "__main__":
    main()




# import requests

# # Define the base URL for the Flask application
# BASE_URL = 'http://127.0.0.1:5000'

# # Function to test creating a new task
# def test_create_task():
#     url = BASE_URL + '/tasks'
#     data = {'content': 'Test Task Content'}
#     try:
#         response = requests.post(url, json=data)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         print(response.json())  # Print the response
#     except requests.exceptions.RequestException as e:
#         print(f"Error creating task: {e}")

# # Function to test getting all tasks
# def test_get_tasks():
#     url = BASE_URL + '/tasks'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         print(response.json())  # Print the response
#     except requests.exceptions.RequestException as e:
#         print(f"Error getting tasks: {e}")

# # Function to test getting a specific task by ID
# def test_get_task(task_id):
#     url = BASE_URL + f'/tasks/{task_id}'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         print(response.json())  # Print the response
#     except requests.exceptions.RequestException as e:
#         print(f"Error getting task: {e}")

# # Function to test updating a task by ID
# def test_update_task(task_id, new_content):
#     url = BASE_URL + f'/tasks/{task_id}'
#     data = {'content': new_content}
#     try:
#         response = requests.put(url, json=data)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         print(response.json())  # Print the response
#     except requests.exceptions.RequestException as e:
#         print(f"Error updating task: {e}")

# # Function to test deleting a task by ID
# def test_delete_task(task_id):
#     url = BASE_URL + f'/tasks/{task_id}'
#     try:
#         response = requests.delete(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         print(response.json())  # Print the response
#     except requests.exceptions.RequestException as e:
#         print(f"Error deleting task: {e}")

# # Main function to execute test cases
# def main():
#     test_create_task()
#     test_get_tasks()
#     test_get_task(3)  # Provide an existing task ID to test
#     test_update_task(3, 'Updated Task Content')  # Provide an existing task ID and new content to test
#     test_delete_task(3)  # Provide an existing task ID to test

# if __name__ == "__main__":
#     main()

