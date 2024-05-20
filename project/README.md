# Quote API (Django)

This Django project provides an API for managing and retrieving quotes. It includes endpoints for retrieving quotes in both English and translated to Bengali.

## Requirements

- Python 3.8+
- Django
- Docker
- Srapping script run before this

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Anisujjaman-Md/newroz_task.git

   ```

2. Navigate to the project directory:

   ```shell
   cd newroz_task/project # for Linux/Mac

   ```

3. Create a virtual environment and activate it:

   ```shell
   python3 -m venv venv
   source venv/bin/activate  # for Linux/Mac
   venv\Scripts\activate  # for Windows

   ```

4. Install the dependencies:

   ```shell
   pip install -r requirements.txt

   ```

5. Apply migrations:

   ```shell
   python manage.py migrate

   ```

6. Start the development server:

   The API will be accessible at http://localhost:8000

   ```shell
    python manage.py runserver

   ```

## Run in Docker

1. Build and run the Docker containers:

   The API will be accessible at http://localhost:8000

   ```shell
    docker-compose up
   ```

## Usage

Endpoints

1. GET /quotes/: Retrieve a list of all quotes.

2. GET /quotes/<id>/: Retrieve a specific quote by its ID.

## Bonus

3. GET /random/quotes/: Retrieve a random quote.

4. GET /quotes-bangla-translate/<id>/: Retrieve a specific quote translated to Bengali.

## Example Usage

# Retrieve all quotes

curl http://localhost:8000/quotes/

# Retrieve a specific quote by ID

curl http://localhost:8000/quotes/1/

# Retrieve a random quote

curl http://localhost:8000/random/quotes/

# Retrieve a specific quote translated to Bengali

curl http://localhost:8000/quotes-bangla-translate/1/

# Swagger Api Documentation

curl http://127.0.0.1:8000/swagger/
