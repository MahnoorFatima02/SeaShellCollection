## SeaShell API

SeaShell Collection is a full-stack web application for managing sea shells, built with **FastAPI** (backend), **React** (frontend), and **PostgreSQL** (Neon cloud database). It supports user authentication, CRUD operations, and modern CI/CD practices.

## Project Structure
The project is structured as follows:

### Backend Explanation
The backend code is organized as follows:

**backend/:** Contains the backend code for the SeaShell API.

**app/**: Contains the FASTAPI application initialization.

**models/**: Contains the database models.

**routes/**: Contains the route definitions.

**services/**: Contains the service layer for business logic.

**migrations/**: Contains the database migration files.

**tests/**: Contains the test files.

**docker/**: Contains the Docker Compose file for setting up the Postgres database.

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

### Endpoints

---

#### Users

1. **User Signup**

*Endpoint:* [POST] /api/v1/signup

*Description:* Registers a new user and returns an access token.

*Request Body:*
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

*Responses:*

_200 OK_ : User registered successfully, returns an access token.
```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```
_400 Bad Request_ : Username already exists.
```json
{
  "detail": "Username already exists"
}
```

---

2. **User Login**

*Endpoint:* [POST] /api/v1/login

*Description:* Authenticates a user and returns an access token.

*Request Body (form data):*
```
username=your_username
password=your_password
```

*Responses:*

_200 OK_ : Login successful, returns an access token.
```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```
_401 Unauthorized_ : Invalid credentials.
```json
{
  "detail": "Incorrect username or password"
}
```

---

#### SeaShells

1. **Create a Shell**

*Endpoint:* [POST] /api/v1/shells  
*Requires Authorization header with Bearer token.*

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
_401 Unauthorized_ : Missing or invalid access token.  
_500 Internal Server Error_ : An unexpected error occurred on the server.

---

2. **Get All Shells**

*Endpoint:* [GET] /api/v1/shells

*Description:* Retrieves all shell records.

*Responses:*

_200 OK_ : The request was successful, and the response contains an array of shell records.  
_500 Internal Server Error_ : An unexpected error occurred on the server.

---

3. **Get a Shell by ID**

*Endpoint:* [GET] /api/v1/shells/{id}  
*Requires Authorization header with Bearer token.*

*Description:* Retrieves a shell record by its ID.

*Path Parameters:*
```json
id: The ID of the shell to retrieve.
```

*Responses:*

_200 OK_ : The request was successful, and the response contains the shell record.  
_404 Not Found_ : The shell record with the specified ID does not exist.  
_401 Unauthorized_ : Missing or invalid access token.  
_500 Internal Server Error_ : An unexpected error occurred on the server.

---

4. **Update a Shell**

*Endpoint:* [PUT] /api/v1/shells/{id}  
*Requires Authorization header with Bearer token.*

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
_401 Unauthorized_ : Missing or invalid access token.  
_500 Internal Server Error_ : An unexpected error occurred on the server.

---

5. **Delete a Shell**

*Endpoint:* [DELETE] /api/v1/shells/{id}  
*Requires Authorization header with Bearer token.*

*Description:* Deletes a shell record by its ID.

*Path Parameters:*
```json
id: The ID of the shell to delete.
```

*Responses:*

_204 No Content_ : The shell record was successfully deleted.  
_404 Not Found_ : The shell record with the specified ID does not exist.  
_401 Unauthorized_ : Missing or invalid access token.  
_500 Internal Server Error_ : An unexpected error occurred on the server.

---

6. **Suggest Shell Species (GBIF)**

*Endpoint:* [POST] /api/v1/shells/suggest

*Description:* Suggests real seashell species based on a keyword using the GBIF API.

*Request Body:*
```json
{
  "keyword": "clam"
}
```

*Responses:*

_200 OK_ : Returns a list of suggested species.
```json
{
  "suggestions": [
    "Scientific Name 1 (Canonical Name 1)",
    "Scientific Name 2 (Canonical Name 2)"
  ]
}
```
_500 Internal Server Error_ : GBIF API error or unexpected error.

---

7. **Suggest Creative Shell (LLM)**

*Endpoint:* [POST] /api/v1/shells/creative

*Description:* Suggests a fictional seashell name and description using an LLM (e.g., OpenAI).

*Request Body:*
```json
{
  "keyword": "rainbow"
}
```

*Responses:*

_200 OK_ : Returns a creative suggestion.
```json
{
  "suggestion": "Rainbow Spiral: A vibrant shell with iridescent bands..."
}
```
_500 Internal Server Error_ : LLM API error or unexpected error.

---

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


## Backend Design Choices

### Frameworks and Libraries

**FASTAPI**

FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. Here are its advantages over other frameworks like Flask or Django:

#### The project uses FASTAPI framework, as it has following advantages: 

- **Performance**:  
  FastAPI is one of the fastest Python frameworks, rivaling Node.js and Go for API workloads, thanks to its async support and Starlette underpinnings.

- **Automatic Interactive Docs**:  
  FastAPI automatically generates interactive Swagger and ReDoc documentation for your API, making it easy for developers and clients to explore and test endpoints.

- **Type Safety & Validation**:  
  Built-in support for Python type hints and Pydantic models means you get automatic request validation, serialization, and editor autocompletion.

- **Async Support**:  
  Native support for async/await makes it ideal for modern, high-concurrency applications (e.g., APIs that call external services or databases).

- **Developer Experience**:  
  FastAPI offers excellent error messages, automatic docs, and type checking, making development faster and less error-prone.

- **Minimal Boilerplate**:  
  You can build production-ready APIs with less code compared to Django (which is more monolithic) or Flask (which requires more manual setup for validation and docs).


**SQLAlchemy**

#### The project uses SQLAlchemy as an ORM for interacting with the database.

- **Async Support**:  
  Native async ORM support for high-performance, concurrent APIs.

- **Framework Agnostic**:  
  Works with any Python web framework.

- **Full SQLAlchemy Power**:  
  Direct access to all SQLAlchemy features, not just what Flask-SQLAlchemy exposes.

- **Better Integration with FastAPI**:  
  Works seamlessly with FastAPI’s dependency injection and async request handling.


**Alembic**

#### It uses Alembic for database migrations.

- **Track Schema Changes**:  
  Migrations allow you to track every change made to your database schema (tables, columns, indexes, etc.) as your application evolves.

- **Version Control**:  
  Each migration is like a commit for your database schema, so you can move forward or backward between versions.

- **Team Collaboration**:  
  Multiple developers can work on the database schema without conflicts, and changes can be shared and applied consistently across environments (dev, staging, production).

- **Automated Deployment**:  
  Migrations can be run automatically as part of your CI/CD pipeline, ensuring your database is always up-to-date with your code.

#### Advantages of Using Migrations

- **Consistency**:  
  Ensures all environments (local, test, production) have the same database schema.

- **Reproducibility**:  
  You can recreate the database schema from scratch using the migration history.

- **Rollback**:  
  If a migration introduces a problem, you can roll back to a previous state.

- **Documentation**:  
  Migration files serve as a history and documentation of how your schema has changed over time.

- **Automation**:  
  No need to manually write SQL for every schema change; Alembic can autogenerate migrations based on your models.



**Swagger-UI**

#### Swagger-UI to easily communication with Frontend developers, it provides documentation for all the endpoints of API. 

- _API Documentation_: Swagger-UI provides a user-friendly interface for API documentation, making it easier for developers to understand and interact with the API.

- _Interactive Documentation_: It allows developers to interact with the API directly from the documentation, making it easier to test and understand the API's functionality.


**Pytest**
**Testing Frameworks**

- _Simplicity and Power_: Pytest is a powerful testing framework that is simple to use and provides many features for writing and running tests.

- _Fixtures and Plugins_: Pytest's fixture system and extensive plugin ecosystem make it easy to set up and manage test environments.


**Mockito (Python)**

- _Mocking Dependencies_: Mockito (via the `mockito` Python package) is used to mock dependencies and isolate service-level logic during testing. This allows you to test components in isolation without relying on external systems or actual database calls.
- _Improved Test Coverage_: By mocking services and DAOs, you can simulate various scenarios and edge cases, improving overall test coverage and reliability.

**Testcontainers**

- _End-to-End Integration Testing_: Testcontainers is used to spin up lightweight, disposable containers (such as MySQL) for full end-to-end integration testing. This ensures that your tests run against a real database environment, closely mirroring production.
- _Isolation and Consistency_: Each test run starts with a fresh container, ensuring tests are isolated and results are consistent across different environments and machines.
- _CI/CD Friendly_: Testcontainers makes it easy to run integration tests in CI/CD pipelines without manual database setup.


**Containerization**

#### Docker Compose

The project uses Docker Compose to containerize the PostgresSQL database. It starts the PostgresSQL container and sets up the necessary environment variables for the application to connect to the database.

## Frontend Design Choices

### Why React?

**React** is a popular JavaScript library for building user interfaces, especially single-page applications (SPAs). Here’s why React was chosen for the SeaShell Collection frontend:

- **Component-Based Architecture:**  
  React’s component model encourages modular, reusable UI components, making the codebase easier to maintain and scale.
- **Large Ecosystem & Community:**  
  React has a vast ecosystem of libraries, tools, and community support, which accelerates development and troubleshooting.
- **Declarative UI:**  
  React’s declarative approach makes it easy to reason about the UI state and how it changes over time.
- **Performance:**  
  React’s virtual DOM efficiently updates only the parts of the UI that change, improving performance for dynamic interfaces.
- **Industry Standard:**  
  React is widely adopted in the industry, making it easier to onboard new developers and integrate with other tools.

### Why Redux?

- **Centralized State Management:**  
  Redux provides a predictable, centralized store for application state, making it easier to manage complex state interactions across components.
- **Debugging & DevTools:**  
  Redux DevTools allow time-travel debugging and state inspection, which is invaluable for development and troubleshooting.
- **Scalability:**  
  Redux scales well for larger applications where state needs to be shared or persisted across many components.

### Why Vite.js?

- **Blazing Fast Development:**  
  Vite.js offers instant server start and lightning-fast hot module replacement (HMR), making the development experience much smoother than older tools like Create React App or Webpack.
- **Modern Build Tooling:**  
  Vite leverages native ES modules and modern browser features, resulting in faster builds and smaller bundles.
- **Easy Configuration:**  
  Vite requires minimal configuration to get started, but is highly extensible for advanced use cases.
- **Optimized for React:**  
  Vite has first-class support for React and other modern frameworks.

### Why Not Vue.js, Next.js, or Others?

- **Vue.js:**  
  Vue is also a great choice for SPAs, but React’s larger ecosystem, more mature tooling, and broader industry adoption made it a better fit for this project.
- **Next.js:**  
  Next.js is excellent for server-side rendering (SSR) and static site generation, but for this project’s SPA requirements and API-driven architecture, React with Vite was simpler and more lightweight.
- **Other Frameworks:**  
  Frameworks like Angular or Svelte are powerful, but React’s balance of flexibility, community support, and tooling made it the preferred choice.

### Other Frontend Design Choices

- **Component Libraries:**  
  The project can easily integrate with popular UI libraries like Material-UI or Ant Design for rapid UI development.
- **Axios for API Calls:**  
  Axios is used for HTTP requests due to its simplicity and robust feature set.
- **ESLint & Prettier:**  
  Static code analysis and formatting tools are used to maintain code quality and consistency.
- **Responsive Design:**  
  The UI is designed to be responsive and mobile-friendly, ensuring a good user experience across devices.
- **Environment Variables:**  
  API endpoints and secrets are managed via environment variables for security and flexibility.

---

**Static Code Analysis**

Static code analysis is an essential practice in modern software development, helping to ensure code quality, maintainability, and security before code is even run. In the SeaShell API project, we use several static analysis tools for both the backend and frontend:

**flake8 (Python)**

- _Purpose_: flake8 is used to check the Python backend code for PEP8 style violations, unused variables/imports, and other common issues.
- _Why_: Enforcing a consistent code style and catching potential bugs early helps maintain a clean, readable, and professional codebase. It also reduces technical debt and makes onboarding new developers easier.
- _Impact_: By integrating flake8, we identified and fixed hundreds of style and linting issues, leading to more maintainable and less error-prone backend code.

**ESLint (JavaScript/React)**

- _Purpose_: ESLint is used to analyze the frontend React code for code quality, potential errors, and style issues.
- _Why_: JavaScript is a dynamic language, so static analysis is crucial for catching bugs, enforcing best practices, and maintaining code consistency across the team.
- _Impact_: ESLint helps prevent common mistakes, enforces coding standards, and improves the overall reliability and readability of the frontend code.

**SonarQube**

- _Purpose_: SonarQube provides comprehensive static code analysis for both backend and frontend, focusing on security, reliability, and maintainability.
- _Why_: SonarQube goes beyond style checks, identifying code smells, security vulnerabilities, and maintainability issues across the entire codebase.
- _Impact_: Regular SonarQube analysis ensures that the project maintains a high standard of code quality, with actionable insights for continuous improvement. It also helps track technical debt and enforces quality gates in CI/CD pipelines.

---

**Future Developments**

- **Admin Role:**  
  Introduce an admin role with special privileges. Only admins will be able to add, update, or remove shells, while regular users can view and suggest shells. This will improve data integrity and allow for better content moderation.

- **LLM Purchase Model:**  
  Enable a feature where users can purchase creative shell suggestions generated by the LLM (e.g., OpenAI). This could include integrating a payment gateway and providing premium, unique shell ideas for collectors or enthusiasts.

- **Refresh Token Functionality:**  
  Implement refresh tokens to enhance authentication security and user experience. This will allow users to stay logged in without frequent re-authentication, while still keeping sessions secure.

- **User Profiles and Collections:**  
  Allow users to create profiles, save their favorite shells, and build personal collections. This adds a social and personalized aspect to the app.

- **Shell Image Uploads:**  
  Enable users (or admins) to upload images for each shell, making the collection more visually engaging.

- **Ratings and Reviews:**  
  Let users rate and review shells, fostering community engagement and helping highlight the most interesting or rare shells.

- **Search and Filter:**  
  Add advanced search and filtering options (by species, location, size, etc.) to help users find shells more easily.

- **Mobile Responsiveness & PWA:**  
  Enhance the mobile experience and consider making the app a Progressive Web App (PWA) for offline access and installability.

- **Notifications:**  
  Implement email or in-app notifications for important events (e.g., when a new shell is added, or when a user's suggestion is approved).

- **API Rate Limiting & Security:**  
  Add rate limiting and additional security measures to protect the API from abuse.

- **Internationalization (i18n):**  
  Support multiple languages to make the app accessible to a global audience.

These enhancements will make the SeaShell Collection app more secure, engaging, and user-friendly, while also opening up new possibilities for growth and monetization.

---

## Conclusion
The SeaShell API project leverages a combination of lightweight and flexible frameworks, powerful testing tools, and containerization to create a robust and maintainable web application. The design choices made in this project aim to balance simplicity, flexibility, and scalability, ensuring that the application can evolve and adapt to future requirements.


