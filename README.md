# Events REST API

A RESTful API built with Python and Flask to manage events using
in-memory storage. The API supports creating, retrieving, updating,
and deleting events.

## Features

- Retrieve a welcome message.
- Retrieve all events.
- Create events with unique IDs.
- Update event titles.
- Delete events.
- Validate incoming JSON data.
- Return appropriate HTTP status codes and error messages.

## Technologies

- Python 3.11
- Flask
- pytest
- Pipenv

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/wdiana78/course-8-module-5-flask-full-crud-api-lab.git
cd course-8-module-5-flask-full-crud-api-lab
```

Install dependencies:

```bash
pipenv install
```

Start the server:

```bash
pipenv run python app.py
```

The API runs at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| GET    | `/`                  | Welcome message       |
| GET    | `/events`            | Retrieve all events   |
| POST   | `/events`            | Create an event       |
| PATCH  | `/events/<event_id>` | Update an event title |
| DELETE | `/events/<event_id>` | Delete an event       |

## Example Requests

Create an event:

```bash
curl -i -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title":"Flask API Testing Session"}'
```

Update an event:

```bash
curl -i -X PATCH http://127.0.0.1:5000/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Advanced Tech Meetup"}'
```

Delete an event:

```bash
curl -i -X DELETE http://127.0.0.1:5000/events/2
```

## HTTP Status Codes

- `200 OK`: Successful retrieval or update.
- `201 Created`: Event created successfully.
- `204 No Content`: Event deleted successfully.
- `400 Bad Request`: Invalid JSON data or missing/invalid title.
- `404 Not Found`: Requested event does not exist.

## Testing

Run the automated tests:

```bash
pipenv run pytest -q
```

## Storage

Events are stored in an in-memory Python list. Data is not persisted
after the server restarts. A database could be introduced in a future
version for persistent storage.
