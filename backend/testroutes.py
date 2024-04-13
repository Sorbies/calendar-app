import json
from app import app, db
from model import Event, Calendar

def test_create_event():
    with app.test_client() as client:
        # Prepare request data
        data = {
            'name': 'Test Event',
            'description': 'Test description',
            'parent_calendar': 1,
            'date_time': '2024-04-15 12:00:00',
            'duration': 2
        }

        # Make POST request to create event
        response = client.post('/events/create', json=data)
        assert response.status_code == 200

        # Parse JSON response
        result = json.loads(response.data)
        assert result['message'] == 'Event created successfully'

# def test_get_events_by_calendar():
#     with app.test_client() as client:
#         # Make GET request to get events by calendar ID
#         response = client.get('/events/getEventsByCalendar?calendar_id=1')
#         assert response.status_code == 200

#         # Parse JSON response
#         events = json.loads(response.data)
#         assert isinstance(events, list)  # Assuming the response is a list of events

# def test_get_event_info():
#     with app.test_client() as client:
#         # Make GET request to get event info by event ID
#         response = client.get('/events/getEventInfo?event_id=1')
#         assert response.status_code == 200

#         # Parse JSON response
#         event_info = json.loads(response.data)
#         assert 'name' in event_info  # Assuming the response contains event information

if __name__ == '__main__':
    # Run tests
    test_create_event()
    # test_get_events_by_calendar()
    # test_get_event_info()
