from flask import request, jsonify
from app import app, db
from model import Event, Calendar


@app.route('/events/create', methods=['POST'])
def create_event():
    # Parse request data
    data = request.json
    name = data.get('name')
    description = data.get('description')
    parent_calendar = data.get('parent_calendar')
    date_time = data.get('date_time')
    duration = data.get('duration', 0)  # Default duration to 0 if not provided

    # Validate input
    if not (name and description and parent_calendar and date_time):
        return jsonify({'error': 'Missing required fields'}), 400

    # Add entry to events database
    new_event = Event(
        name=name,
        description=description,
        calendar_id=parent_calendar,
        date_time=date_time,
        duration=duration
    )
    db.session.add(new_event)
    db.session.commit()

    return jsonify({'message': 'Event created successfully'})


# @app.route('/events/getEventsByCalendar', methods=['GET'])
# def get_events_by_calendar():
#     # Implement get events by calendar logic here
#     pass

# @app.route('/events/getEventInfo', methods=['GET'])
# def get_event_info():
#     # Implement get event info logic here
#     pass
