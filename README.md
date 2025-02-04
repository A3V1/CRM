
## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd dcrm
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/Scripts/activate  # On Windows
    source venv/bin/activate      # On Unix or MacOS
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Features

- User authentication (login, logout, register)
- Add, update, and delete customer records
- View customer records

