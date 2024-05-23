import requests
from test_user import login_user
import sys
import os

# Assuming your script is running from the 'tests' directory and you need to go up two levels to reach the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Define the base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000/'

# Function to create a note
def create_note(token, body):
    url = BASE_URL + '/notes'
    data = {'body': body}
    try:
        response = requests.post(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()
        print("Note created successfully:", response.json())
        return response.json()['id']
    except requests.exceptions.RequestException as e:
        print(f"Error creating note: {e}")
        print(f"Response text: {e.response.text}")

# Function to get all notes
def get_notes(token):
    url = BASE_URL + '/notes'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()
        print("All notes:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting notes: {e}")

# Function to get a specific note by ID
def get_note(token, note_id):
    url = BASE_URL + f'/notes/{note_id}'
    try:
        response = requests.get(url, headers=authenticated_request(token))
        response.raise_for_status()
        print(f"Note {note_id} details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting note {note_id}: {e}")

# Function to update a note by ID
def update_note(token, note_id, body):
    url = BASE_URL + f'/notes/{note_id}'
    data = {'body': body}
    try:
        response = requests.put(url, json=data, headers=authenticated_request(token))
        response.raise_for_status()
        print(f"Updated note {note_id} response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating note {note_id}: {e}")

# Function to delete a note by ID
def delete_note(token, note_id):
    url = BASE_URL + f'/notes/{note_id}'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        response.raise_for_status()
        if response.status_code == 204:
            print(f"Deleted note {note_id} successfully.")
        else:
            print(f"Deleted note {note_id} response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting note {note_id}: {e}")

# Function to delete all notes
def delete_all_notes(token):
    url = BASE_URL + '/notes'
    try:
        response = requests.delete(url, headers=authenticated_request(token))
        response.raise_for_status()
        print("Deleted all notes:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error deleting all notes: {e}")

def authenticated_request(token):
    return {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Main function to execute test cases
def main():
    token = login_user('selma', 'pass4selma')
    if token:
        # Create a new note
        note_id = create_note(token, 'This is a test note.')

        # Get all notes
        get_notes(token)

        # Get the created note
        if note_id:
            get_note(token, note_id)

            # Update the note
            update_note(token, note_id, 'This is an updated test note.')

            # Get the updated note
            get_note(token, note_id)

            # Delete the note
            delete_note(token, note_id)

        # Create multiple notes
        for _ in range(3):
            create_note(token, 'This is another test note.')

        # Get all notes again
        get_notes(token)

        # Delete all notes
        delete_all_notes(token)

        # Get all notes to confirm deletion
        get_notes(token)

if __name__ == "__main__":
    main()
