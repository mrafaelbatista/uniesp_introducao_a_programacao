from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace with a database in a real application)
events = []

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    new_event = request.get_json()
    if not new_event or 'title' not in new_event or 'date' not in new_event:
        return jsonify({'error': 'Invalid event data'}), 400
    events.append(new_event)
    return jsonify(new_event), 201

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

# Get a specific event by index (not ideal for production)
@app.route('/events/<int:index>', methods=['GET'])
def get_event(index):
    if 0 <= index < len(events):
        return jsonify(events[index])
    return jsonify({'error': 'Event not found'}), 404

# Update an event
@app.route('/events/<int:index>', methods=['PUT'])
def update_event(index):
    if 0 <= index < len(events):
        updated_event = request.get_json()
        if not updated_event or 'title' not in updated_event or 'date' not in updated_event:
            return jsonify({'error': 'Invalid event data'}), 400
        events[index] = updated_event
        return jsonify(updated_event)
    return jsonify({'error': 'Event not found'}), 404

# Delete an event
@app.route('/events/<int:index>', methods=['DELETE'])
def delete_event(index):
    if 0 <= index < len(events):
        deleted_event = events.pop(index)
        return jsonify({'message': 'Event deleted', 'event': deleted_event})
    return jsonify({'error': 'Event not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
