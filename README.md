# Django CRUD Project

This is a Django-based web application that allows users to perform CRUD (Create, Read, Update, Delete) operations on a data model, as well as update the data.

## Features

1. **Create**: Users can create new entries in the data model.
2. **Read**: Users can view the list of existing entries and the details of a specific entry.
3. **Update**: Users can edit and update the details of an existing entry.
4. **Delete**: Users can delete an existing entry from the data model.

## Project Structure

The project consists of the following components:

1. **Django Application**: The Django application handles the core functionality of the CRUD operations and data updating.
2. **Django REST Framework (DRF)**: The Django REST Framework is used to provide a RESTful API for the CRUD operations.

## Installation and Setup

1. The repository: python maage.py startapp api

2. Create and activate a virtual environment: 
cd crudProj
python -m virtualenv venv
venv\Scripts\activate

3. Install the required dependencies: pip install postgres

4. Set up the database: python manage.py migrate

5. Start the development server:  python manage.py runserver


The application should now be running at `http://127.0.0.1:8000/`.

## Usage

1. **Create**: Use the provided form or API endpoint to create a new entry in the data model.
2. **Read**: Visit the list view to see all the existing entries, and click on an entry to view its details.
3. **Update**: On the detail view of an entry, click the "Edit" button to update the entry's details.
4. **Delete**: On the detail view of an entry, click the "Delete" button to remove the entry from the data model.

## API Endpoints

The following postman operation:

- `GET http://127.0.0.1:8000/movies/`: List all entries
- `GET http://127.0.0.1:8000/movies/{id}/`: Retrieve a specific entry
- `POST http://127.0.0.1:8000/movies/`: Create a new entry
- `PUT http://127.0.0.1:8000/movies/{id}/`: Update an existing entry
- `DELETE http://127.0.0.1:8000/movies/{id}/`: Delete an existing entry

