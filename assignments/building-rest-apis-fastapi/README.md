# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating endpoints for reading and creating data, handling JSON requests, and returning structured responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a small FastAPI application and configure the base project structure for a REST API.

#### Requirements
Completed program should:

- Install and import FastAPI
- Create an app instance using `FastAPI()`
- Add a root endpoint at `/` that returns a welcome message
- Run the app locally with `uvicorn` and confirm the API responds successfully

### 🛠️ Build Resource Endpoints

#### Description
Create endpoints to manage a collection of items, such as tasks, books, or students.

#### Requirements
Completed program should:

- Define an in-memory list of items to simulate a database
- Add a `GET /items` endpoint that returns all items
- Add a `GET /items/{item_id}` endpoint that returns one item by ID
- Add a `POST /items` endpoint that accepts new item data and adds it to the list
- Return JSON responses with clear data structures

### 🛠️ Validate Input and Handle Errors

#### Description
Improve the API by validating request data and handling edge cases like missing items or invalid input.

#### Requirements
Completed program should:

- Use a Pydantic model to define the expected item format
- Reject invalid API input with a validation error
- Return a helpful response when an item is not found
- Include status codes that match the action being performed
- Test the API using a browser, curl, or the FastAPI docs interface
