# Project 1: Django REST API for User, Contact, and Newsletter Management

This project provides a simple REST API built with Django and Django REST Framework. The API manages three types of data models: general user data, contact submissions, and newsletter subscriptions. It is configured to support CRUD operations for each model.

## Features

- **User Data Management**: Create, read, update, and delete general user data, including name, mobile number, and address.
- **Contact Submission**: Manage contact forms, including fields for name, email, subject, description, and submission date.
- **Newsletter Subscription**: Handle newsletter subscriptions with email and subscription date.

## Project Structure

- **Models**:
  - `Data`: Stores basic user information.
  - `Contact`: Manages user contact submissions.
  - `Newsletter`: Manages newsletter subscription data.
- **Serializers**: Defines how data is converted to JSON for API responses.
- **API Endpoints**: Exposed using Django REST Framework's ViewSets and registered with the router.

## Getting Started

### Prerequisites

- Python 3.x
- Django and Django REST Framework installed (See installation instructions below).

### Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd project_1
    ```

2. **Install Dependencies**:
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Database Migrations**:
    Set up the SQLite database:
    ```bash
    python manage.py migrate
    ```

4. **Start the Server**:
    Run the Django development server:
    ```bash
    python manage.py runserver
    ```

### API Endpoints

The API endpoints are accessible at `http://127.0.0.1:8000/api/`. The main endpoints include:

- `/api/data/`: CRUD operations for general user data.
- `/api/Contact/`: CRUD operations for contact submissions.
- `/api/News/`: CRUD operations for newsletter subscriptions.

### Example API Requests

- **Create a New Data Entry**:
    ```json
    POST /api/data/
    {
      "namesss": "John Doe",
      "mobile": "1234567890",
      "address": "123 Main St"
    }
    ```

- **List All Contacts**:
    ```json
    GET /api/Contact/
    ```

### Project Structure

The core structure of the project includes:

- `models.py`: Defines the `Data`, `Contact`, and `Newsletter` models.
- `serializers.py`: Configures serializers for each model to handle JSON conversion.
- `views.py`: Uses Django REST Framework’s `ViewSet` to enable CRUD operations.
- `urls.py`: Registers API endpoints using Django REST Framework’s router.

### Additional Configuration

- **Database**: The project uses SQLite as its database.
- **Settings**: Basic Django settings are configured in `settings.py`.

## Summary

This Django project provides a foundational REST API for managing basic user, contact, and newsletter data. It’s structured to support standard CRUD operations and can be easily extended for additional functionalities.

---

Happy coding!
