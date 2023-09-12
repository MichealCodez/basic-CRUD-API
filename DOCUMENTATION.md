```markdown
# Person CRUD API Documentation

Welcome to the documentation for the Person CRUD API. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on persons with a single field, "name."

## Table of Contents

1. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
2. [API Endpoints](#api-endpoints)
   - [List Persons](#list-persons)
   - [Create Person](#create-person)
   - [Read Person](#read-person)
   - [Update Person](#update-person)
   - [Delete Person](#delete-person)
3. [Authentication and Permissions](#authentication-and-permissions)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Built With](#built-with)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework (DRF)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MichealDavid1/basic-CRUD-API.git
   cd basic-CRUD-API
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for accessing the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

The API will be available at `https://basic-crud-api.onrender.com/api/`.

## API Endpoints

### List Persons

- **Endpoint:** `GET /api/`
- **Description:** Retrieve a list of all persons.
- **Authentication:** None (publicly accessible)

**Usage Example:**

**Request:**

```http
GET /api/
```

**Expected Result:**


```json
Status: 200 OK

[
    {
        "id": 1,
        "name": "John Doe"
    },
    {
        "id": 2,
        "name": "Jane Smith"
    }
]
```

### Create Person

- **Endpoint:** `POST /api/create/`
- **Description:** Create a new person.
- **Authentication:** None (publicly accessible)
- **Request Body:** JSON data with the "name" field.

**Usage Example:**

**Request:**

```http
POST /api/create/
Content-Type: application/json

{
    "name": "Kayode Celeb"
}
```

**Expected Result:**

```json
Status: 201 Created

{
    "id": 3,
    "name": "Kayode Celeb"
}
```

### Read Person

- **Endpoint:** `GET /api/<int:id>/`
- **Description:** Retrieve a specific person by ID.
- **Authentication:** None (publicly accessible)

**Usage Example:**

**Request:**

```http
GET /api/1/
```

**Expected Result:**

```json
Status: 200 OK

{
    "id": 1,
    "name": "John Doe"
}
```

### Update Person

- **Endpoint:** `PUT /api/<int:id>/`
- **Description:** Update a specific person by ID.
- **Authentication:** None (publicly accessible)
- **Request Body:** JSON data with the "name" field.

**Usage Example:**

**Request:**

```http
PUT /api/update/1/
Content-Type: application/json

{
    "name": "John Updated"
}
```

**Expected Result:**

```json
Status: 200 OK

{
    "id": 1,
    "name": "John Updated"
}
```

### Delete Person

- **Endpoint:** `DELETE /api/delete/<int:id>/`
- **Description:** Delete a specific person by ID.
- **Authentication:** None (publicly accessible)

**Usage Example:**

**Request:**

```http
DELETE /api/delete/1/
```

**Expected Result:**

```json
Status: 204 No Content
```

## Authentication and Permissions

By default, the API has no authentication or permission restrictions. You can customize authentication and permissions based on your project requirements.

## Testing

You can run tests to ensure the API is functioning correctly:

```bash
python manage.py test CRUD_API.tests
```

## Deployment

To deploy this API locally

```bash
python manage.py runserver
```

Your server will run at port 8000 with localhost
You can then access it at http://localhost:8000/api/ 

## Built With

- [Django](https://www.djangoproject.com/) - The web framework for Python
- [Django Rest Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs
