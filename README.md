# Contacts Management API - README

## Project Overview

This mini-project is a REST API built using FastAPI, designed for managing contacts and their information. The project uses **SQLAlchemy** as the ORM (Object Relational Mapper) to handle the database interactions, and **PostgreSQL** as the database. The API allows users to perform CRUD operations (Create, Read, Update, Delete) and includes additional features for searching and filtering contacts based on different attributes.

### Key Features:
- Store contacts with details such as:
    - First Name
    - Last Name
    - Email Address
    - Phone Number
    - Date of Birth
    - Additional Information (optional)
    - CRUD operations for contacts
    - Search for contacts by:
    - First Name
    - Last Name
    - Email Address
    - Retrieve contacts whose birthdays are in the upcoming 7 days

## Technologies Used

- **FastAPI**: For building the REST API.
- **SQLAlchemy**: For database ORM.
- **PostgreSQL**: The database used for storing contact data.
- **Pydantic**: For data validation and serialization.
- **UVicorn**: ASGI server for serving FastAPI applications.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database**:
    - Ensure you have PostgreSQL installed and running.
    - Create a new database for the project:
      ```bash
      psql -U postgres -c "CREATE DATABASE contacts_db;"
      ```

5. **Configure the `config.py` file**:
   Example:
   ```
   DATABASE_URL=postgresql://postgres:<password>@localhost:5432/contacts_db
   ```

6. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

7. **API Documentation**:
   After starting the server, navigate to `http://127.0.0.1:8000/docs` to explore the API documentation via the FastAPI Swagger UI.

## API Endpoints

### Contact Management

1. **Create a new contact**  
   `POST /api/contacts/`  
   Create a new contact with the provided details.

2. **Get all contacts**  
   `GET /api/contacts/`  
   Retrieve a list of all contacts.

3. **Get a contact by ID**  
   `GET /api/contacts/{contact_id}`  
   Retrieve a specific contact by its ID.

4. **Update a contact by ID**  
   `PUT /api/contacts/{contact_id}`  
   Update the details of an existing contact.

5. **Delete a contact by ID**  
   `DELETE /api/contacts/{contact_id}`  
   Remove a contact from the database.

### Additional Features

1. **Search contacts**  
   `GET /api/contacts/search?name=<name>&lastName=<lastName>&email=<email>`  
   Search for contacts based on first name, last name, or email address.

## General Requirements

- The project is built with FastAPI.
- Uses SQLAlchemy ORM to interact with the PostgreSQL database.
- Includes full CRUD functionality for managing contacts.
- Supports data validation through Pydantic.
- Exposes API documentation through FastAPI’s built-in Swagger interface.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

