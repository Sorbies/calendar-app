import requests
from test_user import login_user
import sys
import os

# Assuming your script is running from the 'tests' directory and you need to go up two levels to reach the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Define the base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000'

# Function to create a calendar
def create_calendar(token, name, color):
    url = BASE_URL + '/calendars'
    data = {'name': name, 'color': color}
    try:
        response = requests.post(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()
        print("Calendar created successfully:", response.json())
        return response.json()['id']
    except requests.exceptions.RequestException as e:
        print(f"Error creating calendar: {e}")
        print(f"Response text: {e.response.text}")

# Function to get all calendars
def get_calendars(token):
    url = BASE_URL + '/calendars'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()
        print("All calendars:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting calendars: {e}")

# Function to get a specific calendar by ID
def get_calendar(token, calendar_id):
    url = BASE_URL + f'/calendars/{calendar_id}'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()
        print(f"Calendar {calendar_id} details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting calendar {calendar_id}: {e}")

# Function to update a calendar by ID
def update_calendar(token, calendar_id, name, color):
    url = BASE_URL + f'/calendars/{calendar_id}'
    data = {'name': name, 'color': color}
    try:
        response = requests.put(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()
        print(f"Updated calendar {calendar_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating calendar {calendar_id}: {e}")

# Function to delete a calendar by ID
def delete_calendar(token, calendar_id):
    url = BASE_URL + f'/calendars/{calendar_id}'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        response.raise_for_status()
        if response.status_code == 204:
            print(f"Deleted calendar {calendar_id} successfully.")
        else:
            print(f"Deleted calendar {calendar_id} response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting calendar {calendar_id}: {e}")

def authenticated_request(token):
    return {'Authorization': f'Bearer {token}'}

# Main function to execute test cases
def main():
    token = login_user('rana', 'pass4rana')
    if token:
        calendar_id = create_calendar(token, 'Work Calendar', 'blue')
        get_calendars(token)
        if calendar_id:
            get_calendar(token, calendar_id)
            update_calendar(token, calendar_id, 'Updated Work Calendar', 'green')
            delete_calendar(token, calendar_id)

if __name__ == "__main__":
    main()
