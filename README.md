# prodpulse-api
API for time-series metrics on products.
# My Django Project

A Django REST API with JWT authentication powered by Simple JWT.

---

## Prerequisites

- Python 3.8 or higher  
- pip installed  
- Git client  

---

## Setup

Follow these steps to get your local development environment ready.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo 
```

## Project Overview

This project is a Django-based RESTful API for managing and analyzing time-series metrics related to products. It is designed to provide secure endpoints for data ingestion, retrieval, and analytics, leveraging JWT authentication for user access control.

### Project Structure

- `api/` - Contains the main application logic, including models, views, and tests.
- `core/` - Django project configuration, settings, and URL routing.
- `db.sqlite3` - Default SQLite database for development.
- `manage.py` - Django's command-line utility for administrative tasks.

### Running the Project Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Apply migrations:
    ```bash
    python manage.py migrate
    ```

3. Create a superuser (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

---

For more details on API endpoints and usage, see the code in the `api/` directory.