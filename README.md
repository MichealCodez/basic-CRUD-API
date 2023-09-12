```markdown
# Person CRUD API using Django Rest Framework

This is a simple CRUD (Create, Read, Update, Delete) API built using Django Rest Framework (DRF) for managing persons with a single field: name.

## Getting Started

These instructions will help you set up and run the API on your local machine for development and testing purposes.

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

- **Create Person**: `POST /api/`
- **Retrieve Person**: `GET /api/<int:id>/`
- **Update Person**: `PUT /api/update/<int:id>/`
- **Delete Person**: `DELETE /api/delete/<int:id>/`

## Authentication and Permissions

By default, the API has no authentication or permission restrictions. You can customize authentication and permissions based on your project requirements.

## Testing

You can run tests to ensure the API is functioning correctly:

```bash
python manage.py test CRUD_API.tests
```

## Deployment

To deploy this API in a production environment, you can use platforms like Heroku, AWS, or your preferred hosting service.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework for Python
- [Django Rest Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs
