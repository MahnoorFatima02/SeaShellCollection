## SeaShell API

SeaShell API is a Flask-based web application for managing sea shells. It provides a RESTful API for creating, reading, updating, and deleting shell records.

## Project Structure
The project is structured as follows:

### Backend Explanation
The backend code is organized as follows:

**backend/:** Contains the backend code for the SeaShell API.

**app/**: Contains the Flask application initialization.

**models/**: Contains the database models.

**routes/**: Contains the route definitions.

**services/**: Contains the service layer for business logic.

**migrations/**: Contains the database migration files.

**tests/**: Contains the test files.

**docker/**: Contains the Docker Compose file for setting up the MySQL database.

**config/**: Contains the configuration files.

**README.md**: Contains the project documentation.

### Frontend Explanation
The frontend code is organized as follows:

**frontend/**: Contains the frontend code for the SeaShell application.

**public/**: Contains the public assets like index.html.

**src/**: Contains the source code for the frontend application.

**components/**: Contains the React components.

**redux/**: Contains the Redux store configuration.

**actions/**: Contains the Redux action creators.

**reducers/**: Contains the Redux reducers.

**App.js**: The main application component.

**index.js**: The entry point for the React application.

**package.json**: Contains the dependencies and scripts for the frontend application.

## Backend Endpoints and Error Handling

### Endpoints: 

1. **Create a Shell**

*Endpoint:* [POST] /api/v1/shells

*Description:* Creates a new shell record.

*Request Body:*

```json
{
  "name": "Shell 1",
  "species": "Species 1",
  "description": "Description 1",
  "location": "Location 1",
  "size": "Size 1"
}
```

*Responses:*

_201 Created_ : The shell record was successfully created.

_400 Bad Request_ : The request body is missing required fields or contains invalid data.

_500 Internal Server Error_ : An unexpected error occurred on the server.

2. **Get All Shells**

*Endpoint:* [GET] /api/v1/shells

*Description:* Retrieves all shell records.

*Responses:*

_200 OK_ : The request was successful, and the response contains an array of shell records.

_500 Internal Server Error_ : An unexpected error occurred on the server.

3. **Get a Shell by ID**

*Endpoint:* [GET] /api/v1/shells/{id}

*Description:* Retrieves a shell record by its ID.

*Path Parameters:*

```json
id: The ID of the shell to retrieve.
```

*Responses:*

_200 OK_ : The request was successful, and the response contains the shell record.

_404 Not Found_ : The shell record with the specified ID does not exist.

_500 Internal Server Error_ : An unexpected error occurred on the server.

4. **Update a Shell**

*Endpoint:* [PUT] /api/v1/shells/{id}

*Description:* Updates an existing shell record by its ID.

*Path Parameters:*

```json
id: The ID of the shell to update.
```
*Request Body:*

```json
{
    "name": "Updated Shell",
    "species": "Updated Species",
    "description": "Updated Description",
    "location": "Updated Location",
    "size": "Updated Size"

}
```
*Responses:*

_200 OK_ : The shell record was successfully updated.

_400 Bad Request_ : The request body is missing required fields or contains invalid data.

_404 Not Found_ : The shell record with the specified ID does not exist.

_500 Internal Server Error_ : An unexpected error occurred on the server.

5. **Delete a Shell**

*Endpoint:* [DELETE] /api/v1/shells/{id}

*Description:* Deletes a shell record by its ID.

*Path Parameters:*

```json
id: The ID of the shell to delete.
```
*Responses:*

_204 No Content_ : The shell record was successfully deleted.

_404 Not Found_ : The shell record with the specified ID does not exist.

_500 Internal Server Error_ : An unexpected error occurred on the server.

### Error Handling

The SeaShell API includes error handling capabilities to ensure that appropriate responses are returned for various error conditions. Here are some of the key error handling mechanisms:

**Validation Errors:**

**Description:** Occur when the request body is missing required fields or contains invalid data.

**Response:** 400 Bad Request

**Example:**

```json
{
    "error": "species is required"
}
```
**Resource Not Found:**

**Description:** Occur when a requested resource (e.g., a shell record) does not exist.

**Response:** 404 Not Found

**Example:**

```json
{
    "error": "Resource not found"
}
```

**Internal Server Errors:**
**Description:** Occur when an unexpected error happens on the server.
**Response:** 500 Internal Server Error
**Example:**
```json
{
    "error": "An unexpected error occurred"
}
```

These error handling mechanisms ensure that the API provides clear and informative responses to users, helping them understand the nature of the errors and take appropriate actions.


## Design Choices

### Frameworks and Libraries

**Flask**

#### The project uses Flask framework, as it has following advantages: 

_Lightweight and Flexible_ : Flask is a micro-framework that provides the essentials to get a web application up and running. It is lightweight and allows for flexibility in design and implementation.

_Extensible_: Flask's modular design allows for easy integration of extensions to add functionality as needed.

_Community and Documentation_ : Flask has a large and active community, which means there are many resources, tutorials, and extensions available.


**Flask-SQLAlchemy**

#### The project uses Flask-SQLAlchemy as an ORM for interacting with the database.

_ORM Support_: Flask-SQLAlchemy provides an Object-Relational Mapping (ORM) layer, making it easier to interact with the database using Python objects.

_Database Agnostic_: It supports multiple databases, including PostgreSQL, MySQL, SQLite, and more.

_Ease of Use_: It simplifies database operations by providing a high-level API for interacting with the database.


**Flask-Migrate**

#### It uses Flask-Migrate for database migrations.

_Database Migrations_: Flask-Migrate, built on Alembic, provides tools to handle database migrations, making it easier to manage changes to the database schema over time.

_Integration with Flask-SQLAlchemy_: It integrates well with Flask-SQLAlchemy, providing a smooth workflow for database migrations.

_Automated Migrations_: It automates the process of creating and applying database migrations, reducing manual effort.


**Flask-Swagger-UI**

#### Flask-Swagger-UI to easily communication with Frontend developers, it provides documentation for all the endpoints of API. 

_API Documentation_: Flask-Swagger-UI provides a user-friendly interface for API documentation, making it easier for developers to understand and interact with the API.

_Interactive Documentation_: It allows developers to interact with the API directly from the documentation, making it easier to test and understand the API's functionality.

### Alternative Swagger Frameworks 
**Flasgger**

The flasgger library is used to generate interactive API documentation for Flask applications. It allows you to describe your API using YAML or JSON, and it generates a Swagger-compatible API documentation.

It could be used as an alternative to Flask-Swagger-UI.

**Pytest**
**Testing Frameworks**

_Simplicity and Power_: Pytest is a powerful testing framework that is simple to use and provides many features for writing and running tests.

_Fixtures and Plugins_: Pytest's fixture system and extensive plugin ecosystem make it easy to set up and manage test environments.


### Alternative Testing Techniques

**Containerzation of mysql database**

Another way to test API is to containerize the mysql database.

It provides a end to end testing of API, especially the database queries.

**Containerization**

#### Docker Compose

The project uses Docker Compose to containerize the MySQL database. It starts the MySQL container and sets up the necessary environment variables for the application to connect to the database.


## Conclusion
The SeaShell API project leverages a combination of lightweight and flexible frameworks, powerful testing tools, and containerization to create a robust and maintainable web application. The design choices made in this project aim to balance simplicity, flexibility, and scalability, ensuring that the application can evolve and adapt to future requirements.


