## SeaShell API

SeaShell API is a Flask-based web application for managing sea shells. It provides a RESTful API for creating, reading, updating, and deleting shell records.

## Table of Contents

Project Structure

Prerequisites

Setup

Running the Application

Running Tests

API Documentation

Database Migrations

Docker Setup

Design Choices

## Project Structure
The project is structured as follows:

### Backend Explanation
The backend code is organized as follows:

**backend/**: Contains the backend code for the SeaShell API.

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

## Conclusion

The SeaShell API provides a comprehensive set of endpoints for managing shell records, along with robust error handling capabilities to ensure that appropriate responses are returned for various error conditions. This documentation provides an overview of the endpoints and error handling mechanisms, helping developers understand how to interact with the API and handle potential errors.


## Design Choices

### Frameworks and Libraries

**Flask**

#### Why Flask? 

_Lightweight and Flexible_ : Flask is a micro-framework that provides the essentials to get a web application up and running. It is lightweight and allows for flexibility in design and implementation.

_Extensible_: Flask's modular design allows for easy integration of extensions to add functionality as needed.

_Community and Documentation_ : Flask has a large and active community, which means there are many resources, tutorials, and extensions available.

#### Why not Django?

_Complexity_: Django is a full-stack framework that comes with a lot of built-in features. For a project like SeaShell API, which is relatively simple, Flask's lightweight nature is more suitable.

_Learning Curve_: While Django has a steeper learning curve, Flask is more straightforward and easier to understand for developers who are new to web development.

_Flexibility_: Flask allows for more flexibility in choosing components and structuring the application, which is beneficial for a project that may evolve over time.

**Flask-SQLAlchemy**

#### Why Flask-SQLAlchemy?

_ORM Support_: Flask-SQLAlchemy provides an Object-Relational Mapping (ORM) layer, making it easier to interact with the database using Python objects.

_Database Agnostic_: It supports multiple databases, including PostgreSQL, MySQL, SQLite, and more.

_Ease of Use_: It simplifies database operations by providing a high-level API for interacting with the database.

_Integration with Flask_: It integrates seamlessly with Flask, providing a simple and consistent way to manage database connections and queries.

#### Why not SQLAlchemy alone?

_Flask Integration_: Flask-SQLAlchemy provides additional features and integration specifically designed for Flask applications, making it more convenient than using SQLAlchemy alone.

_Simplified Configuration_: It simplifies the configuration of the database connection and provides a consistent way to interact with the database across the application.

**Flask-Migrate**

#### Why Flask-Migrate?

_Database Migrations_: Flask-Migrate, built on Alembic, provides tools to handle database migrations, making it easier to manage changes to the database schema over time.

_Integration with Flask-SQLAlchemy_: It integrates well with Flask-SQLAlchemy, providing a smooth workflow for database migrations.

_Automated Migrations_: It automates the process of creating and applying database migrations, reducing manual effort.

**Flask-Cors**

#### Why Flask-Cors?

_Cross-Origin Resource Sharing_: Flask-Cors allows the API to handle cross-origin requests, which is essential for enabling web applications hosted on different domains to interact with the API.

**Flask-Swagger-UI**

#### Why Flask-Swagger-UI? 

_API Documentation_: Flask-Swagger-UI provides a user-friendly interface for API documentation, making it easier for developers to understand and interact with the API.

_Interactive Documentation_: It allows developers to interact with the API directly from the documentation, making it easier to test and understand the API's functionality.

_Versioning Support_: It supports versioning of API endpoints, allowing for smooth transitions and updates to the API.

_Customization_: It allows customization of the API documentation, making it easier to tailor the documentation to the specific needs of the API.

_Integration with Flask_: It integrates seamlessly with Flask, providing a consistent and user-friendly experience for both developers and users.

_User-Friendly Interface_: It offers a user-friendly interface for exploring and testing API endpoints.

**Pytest**
**Testing Frameworks**

#### Why Pytest?

_Simplicity and Power_: Pytest is a powerful testing framework that is simple to use and provides many features for writing and running tests.

_Fixtures and Plugins_: Pytest's fixture system and extensive plugin ecosystem make it easy to set up and manage test environments.

_Assertion Library_: Pytest includes a rich assertion library, making it easier to write and maintain test assertions.

**unittest.mock**

#### Why unittest.mock?

_Standard Library_: unittest.mock is part of the Python standard library, providing tools for mocking and patching in tests without requiring additional dependencies.

_Mocking and Patching_: It provides tools for mocking and patching objects and functions, making it easier to isolate and test individual components.

_Isolation_: It allows for easy isolation of tests, making it easier to write and maintain tests that focus on specific components.

_Flexibility_: It offers a flexible and powerful way to mock objects and functions, making it easier to isolate and test individual components.

**MagicMock**
#### Why MagicMock?

_Mocking Objects_: MagicMock is a subclass of Mock that provides a convenient way to create mock objects with a wide range of features.
_Flexibility_: It offers flexibility in creating mock objects with various attributes and behaviors.

_Simplicity_: It simplifies the process of creating mock objects, making it easier to write tests that focus on specific components.

_Integration with unittest.mock_: MagicMock is part of the unittest.mock library, providing a convenient way to create mock objects with a wide range of features.

### Alternative Testing Techniques
**Containerzation of mysql database**

#### why is it important to containerize the database?

_Isolation_: Containerization isolates the database from the host system, ensuring that changes to the host system do not affect the database.

_Consistency_: Containerization ensures that the database runs consistently across different environments, reducing the risk of issues due to differences in configurations.

_Reproducibility_: Containerization allows for easy replication of the database environment, making it easier to reproduce issues and test fixes.

_Scalability_: Containerization makes it easier to scale the database horizontally, allowing for better performance and fault tolerance.

**Containerization**

**Docker and Docker Compose**

#### Why Docker?

_Consistency_: Docker ensures that the application runs consistently across different environments by packaging it with all its dependencies.

_Isolation_: Docker containers provide isolation, making it easier to manage dependencies and avoid conflicts.
Why Docker Compose?

_Multi-Container Applications_: Docker Compose simplifies the management of multi-container applications, such as setting up a MySQL database alongside the Flask application.

_Ease of Use_: It provides a simple way to define and run multi-container Docker applications using a single configuration file.

**MySQL Database**

#### Why MySQL?

_Reliability_: MySQL is a widely used and reliable database system, known for its stability and performance.

_Scalability_: MySQL is designed to handle large amounts of data and can scale well for growing applications.

_Community and Support_: MySQL has a large and active community, providing support and resources for developers.

_Data Integrity_: MySQL provides features like transactions and constraints to ensure data integrity and consistency.

_Compatibility_: MySQL is compatible with a wide range of programming languages and platforms, making it a versatile choice for web applications.

#### why not use PostgreSQL? 

**PostgreSQL** is a powerful and feature-rich open-source relational database management system. It offers many advantages over MySQL, making it a popular choice for many applications. Here are some reasons why PostgreSQL might be a better choice than MySQL:

**Advanced Features:** PostgreSQL offers advanced features that are not available in MySQL. For example, it supports advanced data types like JSON and arrays, which can be useful for handling complex data structures.

**ACID Compliance:** PostgreSQL is ACID (Atomicity, Consistency, Isolation, Durability) compliant, ensuring data integrity and consistency in transactions.

**Advanced Querying:** PostgreSQL supports advanced querying techniques like window functions, recursive queries, and full-text search, making it suitable for complex data analysis and reporting.

**Multi-Version Concurrency Control (MVCC):** PostgreSQL uses MVCC, which allows multiple transactions to run concurrently without blocking each other. This can improve performance and scalability.

**Foreign Data Wrappers:** PostgreSQL supports foreign data wrappers, enabling the integration of data from external sources into the database.

#### why chose MySQL over PostgreSQL?

**Simplicity:** MySQL is known for its simplicity and ease of use. It has a straightforward installation process and a wide range of documentation and resources available.

**Performance:** MySQL is known for its performance, especially in terms of query execution speed. It is often used in high-performance applications where speed is critical.

**Scalability:** MySQL is designed to scale well for large-scale applications. It can handle high volumes of data and concurrent connections.

## Conclusion
The SeaShell API project leverages a combination of lightweight and flexible frameworks, powerful testing tools, and containerization to create a robust and maintainable web application. The design choices made in this project aim to balance simplicity, flexibility, and scalability, ensuring that the application can evolve and adapt to future requirements.


