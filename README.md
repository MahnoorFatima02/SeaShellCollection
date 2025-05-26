# SeaShell Collection

SeaShell Collection is a full-stack web application for managing sea shells, built with **FastAPI** (backend), **React** (frontend), and **PostgreSQL** (Neon cloud database). It supports user authentication, CRUD operations, and modern CI/CD practices.

# SeaShell Collection

[![Frontend](https://img.shields.io/badge/Live%20Frontend-blue?style=flat-square)](https://seashellcollection.onrender.com/)
[![Backend](https://img.shields.io/badge/Live%20Backend-green?style=flat-square)](https://seashellcollection-backend.onrender.com/)
[![Swagger Docs](https://img.shields.io/badge/Swagger%20UI-orange?style=flat-square)](https://seashellcollection-backend.onrender.com/docs)

SeaShell Collection is a full-stack web application for managing sea shells, built with **FastAPI** (backend), **React** (frontend), and **PostgreSQL** (Neon cloud database). It supports user authentication, CRUD operations, and modern CI/CD practices.

---

## Project Pictures

<p>
<img src="https://github.com/MahnoorFatima02/kone-challenge/blob/main/Images/MainPage.png" alt="Main Page" width="350" height="180" /> &nbsp;&nbsp;
<img src="https://github.com/MahnoorFatima02/kone-challenge/blob/main/Images/ShellAddForm.png" alt="Add SeaShell page" width="350" height="180" /> &nbsp;&nbsp;
<img src="https://github.com/MahnoorFatima02/kone-challenge/blob/main/Images/RequiredFields.png" alt="Required Fields" width="350" height="180" /> &nbsp;&nbsp;
<img src="https://github.com/MahnoorFatima02/kone-challenge/blob/main/Images/ShellCollection.png" alt="SeaShell Collection" width="350" height="180" /> &nbsp;&nbsp;
</p>

---

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Static Code Analysis](#static-code-analysis)
- [API Documentation](#api-documentation)
- [Database Migrations](#database-migrations)
- [Deployment](#deployment)
- [Additional Information](#additional-information)

---

## Project Structure

```
SeaShellProject/
├── backend/
│   ├── app/                # FastAPI application
│   ├── database/           # Database models and session
│   ├── alembic/            # Alembic migrations
│   ├── config/             # Configuration files
│   ├── tests/              # Backend tests
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/                # React source code
│   ├── public/
│   ├── package.json
│   └── .env
└── README.md
```

---

## Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL (Neon cloud or local)
- fastapi
- uvicorn
- sqlalchemy
- asyncpg
- alembic
- python-dotenv
- pydantic
- passlib[bcrypt]
- python-jose[cryptography]
- pytest==6.2.4
- pytest-asyncio==0.15.1
- httpx==0.18.2
- pytest-mock==3.6.1
- aiomysql
- testcontainers
- pytest-cov
- asyncmy
- openai
- python-multipart
- asyncpg
- psycopg2-binary

---

## Setup

### 1. **Clone the repository**

```sh
git clone https://github.com/yourusername/SeaShellProject.git
cd SeaShellProject
```

### 2. **Backend Setup**

```sh
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Set up environment variables**  
Create a `.env` file in the `backend/` directory:

```env
SECRET_KEY=your-very-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>/<db>?sslmode=require
```

### 3. **Frontend Setup**

```sh
cd ../frontend
npm install
```

---

## Docker Setup
To set up the MySQL database using Docker Compose, follow these steps:

1. Navigate to the Docker directory:
```sh
cd docker 
```
2. Start the Docker containers:
```sh
docker-compose up -d
```

--- 

## Running the Application

### **Backend (FastAPI)**

```sh
cd backend
uvicorn app:app --reload
```

### **Frontend (React)**

```sh
cd frontend
npm run dev
```

---

## Testing

### **Backend**

This FastAPI application includes a robust testing setup to ensure reliability and maintainability.

- **Testcontainers**: Used to spin up lightweight, disposable containers (e.g., PostgreSQL, Redis) for full end-to-end integration testing.
- **Mockito**: Applied for mocking dependencies and isolating service-level tests (via `mockito` for Python).

```sh
cd backend
pytest
```
The test includes mockito and test containers.
---

## Code Quality & Static Analysis

### **flake8 (Python)**

The project uses **flake8** Checks for style guide violations (PEP8), unused variables/imports, and other linting issues.

**flake8 configuration:**

```sh
cd backend
flake8 . --exclude=venv,migrations
```

This plugin helped us identify and fix **1597** code style violations out of **1622**, ensuring a clean and maintainable codebase.

### **ESLint (JavaScript/React)**

The project uses **ESLint** to check for code quality, potential errors, and style issues in the frontend React codebase.

**How to run ESLint:**

```sh
cd frontend
npx eslint src
```

- You can also use ESLint plugins in your IDE for real-time feedback as you code.

This helps maintain a consistent and error-free codebase for the frontend.



---
## SonarQube Code Analysis

The project uses **SonarQube** for comprehensive static code analysis, focusing on **security**, **reliability**, and **maintainability**.

**Current Quality Gate Rating:**

- **Security: A**
- **Reliability: A**
- **Maintainability: A**

### How to Run SonarQube Analysis

1. **Start SonarQube Server (if running locally):**
   - Navigate to the `bin` directory of your SonarQube installation.
   - Run the appropriate script:
     - On Windows: `StartSonar.bat`
     - On Linux/Mac: `./sonar.sh start`
   - Access the server at `http://localhost:9000`.

2. **Configure Your Project:**
   - Create a `sonar-project.properties` file in the root of your project with the following content:
     ```properties
     sonar.projectKey=your_project_key
     sonar.host.url=http://localhost:9000
     sonar.login=your_generated_token 
     sonar.sources=backend,frontend
     ```
   - If you use a token, set it as an environment variable:
     ```export SONAR_TOKEN=your_generated_token
      sonar-scanner
      ```

3. **Run Sonar Scanner:**
   - Open a terminal in your project directory.
   - Execute the command:
     ```sh
     sonar-scanner
     ```

4. **View Results:**
   - Open `http://localhost:9000` in your browser.
   - Navigate to your project to view the analysis results.

---

## API Documentation

- **Swagger UI:**  
  Visit [http://localhost:8000/docs](http://localhost:9000/docs) when backend is running.

---

## Database Migrations

- **Initialize Alembic (if not already):**
  ```sh
  alembic init alembic
  ```
- **Create a migration:**
  ```sh
  alembic revision --autogenerate -m "Describe migration"
  ```
- **Apply migrations:**
  ```sh
  alembic upgrade head
  ```

---

## Deployment

### **Render.com**

- **Frontend:** Deploy as a static site, root: `frontend`, build command: `npm install && npm run build`, publish directory: `dist`.
- **Backend:** Deploy as a web service, root: `backend`, start command: `uvicorn app:app --host 0.0.0.0 --port 10000`
- **Environment variables:** Set your `.env` values in the Render dashboard for both services.

---

## Additional Information

- **API base URL:**  
  Update `frontend/src/redux/axiosInstance.jsx` with your deployed backend URL.
- **Database:**  
  Uses Neon PostgreSQL cloud database.
- **Authentication:**  
  JWT-based authentication for protected endpoints.
- **CI/CD:**  
  Recommended: Add GitHub Actions for automated testing and linting.

---

**Enjoy your SeaShell Collection app!**


