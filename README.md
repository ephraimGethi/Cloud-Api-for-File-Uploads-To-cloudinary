# Django API Project

## Overview
This Django project provides a REST API for managing computers and rooms using Django Rest Framework (DRF). It includes endpoints for adding and retrieving computers and rooms, with custom exception handling.

## Features
- Add and retrieve computers
- Add and retrieve rooms
- Supports file uploads
- Custom exception handling for improved error responses

## Technologies Used
- Django
- Django REST Framework
- PostgreSQL (Database)
- Cloudinary (for media storage, if configured)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Virtualenv (recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <project-directory>
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': '<your_db_name>',
           'USER': '<your_db_user>',
           'PASSWORD': '<your_db_password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
5. Apply migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser (optional):
   ```sh
   python manage.py createsuperuser
   ```
7. Run the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### 1. Computers API
#### `POST /api/computers/`
- Adds a new computer entry
- Accepts multipart/form-data
- **Request Body:**
  ```json
  {
    "name": "Computer A",
    "brand": "Dell",
    "specs": "16GB RAM, 512GB SSD"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Computer A",
    "brand": "Dell",
    "specs": "16GB RAM, 512GB SSD"
  }
  ```

#### `GET /api/computers/`
- Retrieves all computers

#### `GET /api/computers/<id>/`
- Retrieves a single computer by ID
- **Response:**
  ```json
  {
    "status": "success",
    "data": {
      "id": 1,
      "name": "Computer A",
      "brand": "Dell",
      "specs": "16GB RAM, 512GB SSD"
    }
  }
  ```

### 2. Rooms API
#### `POST /api/rooms/`
- Adds new room(s)
- Supports bulk or single creation
- **Request Body (Single Room):**
  ```json
  {
    "name": "Conference Room",
    "capacity": 20
  }
  ```
- **Request Body (Multiple Rooms):**
  ```json
  [
    {"name": "Room A", "capacity": 10},
    {"name": "Room B", "capacity": 15}
  ]
  ```

#### `GET /api/rooms/`
- Retrieves all rooms

## Error Handling
- Custom exception handling is implemented.
- Example error response for a missing computer:
  ```json
  {
    "message": "Computer not found",
    "status_code": 404,
    "code": "computer_not_found",
    "hint": "Check if the computer ID is correct",
    "extra": {
      "requested_id": 99
    }
  }
  ```

## Deployment
- The project can be deployed on **Heroku**
- Ensure you have configured environment variables correctly for production.

## License
This project is licensed under the MIT License.

## Author
- **Your Name** - Junior Full-Stack Developer (Django & React.js)

