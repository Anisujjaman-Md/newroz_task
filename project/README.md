# Quote API (Django)

This Django project provides an API for managing and retrieving quotes. It includes endpoints for retrieving quotes in both English and translated to Bengali.

## Requirements

- Python 3.8+
- Docker
- Run Srapping script Before

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Anisujjaman-Md/newroz_task.git

   ```

2. Navigate to the project directory:

   ```shell
   cd newroz_task/project # for Linux/Mac

   ```

#### Docker

- Build and run the Docker containers:

  The API will be accessible at http://localhost:8000

  ```shell
   docker-compose up
  ```

#### Local

- Create a virtual environment and activate it:

  ```shell
  python3 -m venv venv
  source venv/bin/activate  # for Linux/Mac
  venv\Scripts\activate  # for Windows

  ```

- Install the dependencies:

  ```shell
  pip install -r requirements.txt

  ```

- Apply migrations:

  ```shell
  python manage.py migrate

  ```

- Import Scrap Data from Csv file:

  ```shell
  python manage.py import_csv inspirational_quotes.csv

  ```

- Start the development server:

  The API will be accessible at http://localhost:8000

  ```shell
   python manage.py runserver

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

curl http://localhost:8000/api/v1/quotes/

# Retrieve a specific quote by ID

curl http://localhost:8000/api/v1/quotes/1/

# Retrieve a random quote

curl http://localhost:8000/api/v1/random/quotes/

# Retrieve a specific quote translated to Bengali

curl http://localhost:8000/api/v1/qoutes-bangla-translate/1/

# Swagger Api Documentation

curl http://127.0.0.1:8000/swagger/
