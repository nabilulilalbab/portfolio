# Django Project

A web application built with Django framework.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11 or higher
* pip (Python package manager)
* virtualenv (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nabilulilalbab/portfolio.git
cd project-name
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
- Create a `.env` file in the project root
- Add necessary environment variables (see `.env.example`)

5. Run database migrations:
```bash
python manage.py migrate
```

6. Create superuser (admin):
```bash
python manage.py createsuperuser
```

## Running the Application

To run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Project Structure

```
project_name/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio/
    ├── migrations/
    ├── templates/
    ├── static/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Development

1. Create new app:
```bash
python manage.py startapp app_name
```

2. Make migrations after model changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Run tests:
```bash
python manage.py test
```

## Deployment

Steps to deploy the application:
1. Configure production settings
2. Set DEBUG=False in settings
3. Configure static files serving
4. Set up a production database
5. Configure WSGI server (e.g., Gunicorn)
6. Set up reverse proxy (e.g., Nginx)

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.