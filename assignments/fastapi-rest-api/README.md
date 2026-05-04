# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you will have built a simple API for managing a collection of resources (e.g., books, tasks, or users).

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and set up the basic structure for your API.

#### Requirements
Completed program should:

- Include a main Python file (e.g., `main.py`) that starts a FastAPI app
- Install FastAPI and Uvicorn as dependencies
- Run the server locally and display a welcome message at the root endpoint (`/`)


### 🛠️ Task 2: Implement CRUD Endpoints

#### Description
Create RESTful endpoints to manage a collection of items (e.g., books, tasks, or users). Implement Create, Read, Update, and Delete operations.

#### Requirements
Completed program should:

- Define a Pydantic model for your resource (e.g., Book, Task, or User)
- Implement endpoints for:
  - Creating a new item (`POST /items/`)
  - Listing all items (`GET /items/`)
  - Retrieving a single item by ID (`GET /items/{item_id}`)
  - Updating an item (`PUT /items/{item_id}`)
  - Deleting an item (`DELETE /items/{item_id}`)
- Use in-memory storage (a Python list or dictionary)


### 🛠️ Task 3: API Documentation and Testing

#### Description
Explore FastAPI's automatic API documentation and test your endpoints using the interactive docs.

#### Requirements
Completed program should:

- Access the interactive API docs at `/docs`
- Test all endpoints using the Swagger UI
- Ensure all endpoints return appropriate status codes and responses

---

**Extension:** Add data validation, error handling, or authentication for extra credit!

---

**Starter code is provided in `starter-code.py`.**
