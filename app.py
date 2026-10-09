
from flask import Flask, jsonify, request

app = Flask(__name__)


class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory database containing 10 initial events.
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop"),
    Event(3, "Hackathon"),
    Event(4, "Web Development Bootcamp"),
    Event(5, "Database Design Seminar"),
    Event(6, "API Development Workshop"),
    Event(7, "Git and GitHub Session"),
    Event(8, "Cybersecurity Awareness"),
    Event(9, "Cloud Computing Meetup"),
    Event(10, "Software Testing Workshop"),
]


def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


def get_next_event_id():
    return max((event.id for event in events), default=0) + 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Events API"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required"}), 400

    new_event = Event(get_next_event_id(), title.strip())
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required"}), 400

    event.title = title.strip()

    return jsonify(event.to_dict()), 200


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
