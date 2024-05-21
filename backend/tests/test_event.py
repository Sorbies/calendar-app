import requests
from test_user import login_user
import sys
import os
from datetime import datetime, timedelta

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

# Function to create an event
def create_event(token, calendar_id, name, description, date_time, duration):
    url = BASE_URL + '/events'
    data = {
        'calendar_id': calendar_id,
        'name': name,
        'description': description,
        'date_time': date_time.isoformat(),
        'duration': duration
    }
    try:
        response = requests.post(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()
        print("Event created successfully:", response.json())
        return response.json()['id']
    except requests.exceptions.RequestException as e:
        print(f"Error creating event: {e}")
        print(f"Response text: {e.response.text}")

# Function to get all events
def get_events(token, calendar_id=None):
    url = BASE_URL + '/events'
    params = {'calendar_id': calendar_id} if calendar_id else {}
    try:
        response = requests.get(url, headers=authenticated_request(token), params=params)
        response.raise_for_status()
        print("All events:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting events: {e}")

# Function to get a specific event by ID
def get_event(token, event_id):
    url = BASE_URL + f'/events/{event_id}'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()
        print(f"Event {event_id} details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting event {event_id}: {e}")

# Function to update an event by ID
def update_event(token, event_id, name, description, date_time, duration):
    url = BASE_URL + f'/events/{event_id}'
    data = {
        'name': name,
        'description': description,
        'date_time': date_time.isoformat(),
        'duration': duration
    }
    try:
        response = requests.put(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()
        print(f"Updated event {event_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating event {event_id}: {e}")

# Function to delete an event by ID
def delete_event(token, event_id):
    url = BASE_URL + f'/events/{event_id}'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        response.raise_for_status()
        if response.status_code == 204:
            print(f"Deleted event {event_id} successfully.")
        else:
            print(f"Deleted event {event_id} response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting event {event_id}: {e}")

def authenticated_request(token):
    return {'Authorization': f'Bearer {token}'}

# Main function to execute test cases
def main():
    token = login_user('rana', 'pass4rana')
    if token:
        # Create a calendar first, since events are linked to calendars
        calendar_id = create_calendar(token, 'Personal Calendar', 'red')

        if calendar_id:
            # Create an event
            event_id = create_event(
                token,
                calendar_id,
                'Doctor Appointment',
                'Annual check-up with Dr. Smith',
                datetime.now() + timedelta(days=1),  # Schedule for 1 day in the future
                60  # Duration in minutes
            )
            get_events(token, calendar_id)
            if event_id:
                get_event(token, event_id)
                update_event(token, event_id, 'Updated Doctor Appointment', 'Updated description', datetime.now() + timedelta(days=2), 90)
                delete_event(token, event_id)
            # Cleanup: delete the calendar after testing
            delete_calendar(token, calendar_id)

if __name__ == "__main__":
    main()
