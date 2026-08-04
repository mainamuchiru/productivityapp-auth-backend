# Productivity App Backend

## Project Description

The Productivity App Backend is a Flask REST API that allows users to register, log in, and manage personal notes. The application uses **session-based authentication**, ensuring that authenticated users can only create, view, update, and delete their own notes.

The backend uses **Flask-Bcrypt** for secure password hashing and **Flask-Migrate** for database migrations. It is designed to integrate with the provided frontend for the project.

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- SQLAlchemy-Serializer
- SQLite
- python-dotenv

---

# Installation Instructions

## 1. Clone the repository

```bash
git clone https://github.com/mainamuchiru/productivityapp-auth-backend.git

cd productivityapp-auth-backend
```

> **Important:** Run all commands from the project root directory.

---

## 2. Create and activate a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file inside the `server` directory.

```text
server/
└── .env
```

Add the following environment variables:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///app.db
```

> **Note:** The `.env` file is ignored by Git and should not be committed to the repository.

---

## 5. Apply database migrations

If you're setting up the project for the first time, run:

```bash
flask db upgrade
```

If you make changes to the database models later, create and apply a new migration:

```bash
flask db migrate -m "Describe your changes"
flask db upgrade
```

---

## 6. Seed the database

Populate the database with sample users and notes.

```bash
python -m server.seed
```

---

# Running the Application

Start the Flask development server.

```bash
python run.py
```

The API will be available at:

```
http://127.0.0.1:5555
```

---

# Authentication Endpoints

## POST `/signup`

Registers a new user.

### Request Body

```json
{
  "username": "philip",
  "password": "password123"
}
```

**Response**

- `201 Created`

---

## POST `/login`

Authenticates an existing user and creates a session.

### Request Body

```json
{
  "username": "philip",
  "password": "password123"
}
```

**Responses**

- `200 OK`
- `401 Unauthorized`

---

## GET `/me`

Returns the currently authenticated user.

**Responses**

- `200 OK`
- `401 Unauthorized`

---

## DELETE `/logout`

Logs out the authenticated user.

**Response**

- `204 No Content`

---

# Notes Endpoints

> All Notes endpoints require authentication.

---

## GET `/notes`

Returns all notes belonging to the authenticated user.

Supports pagination.

Example:

```
GET /notes?page=1
```

**Response**

- `200 OK`

---

## GET `/notes/<id>`

Returns a specific note owned by the authenticated user.

**Responses**

- `200 OK`
- `401 Unauthorized`
- `404 Not Found`

---

## POST `/notes`

Creates a new note.

### Request Body

```json
{
  "title": "Meeting Notes",
  "content": "Prepare sprint presentation."
}
```

**Response**

- `201 Created`

---

## PATCH `/notes/<id>`

Updates an existing note.

### Request Body

```json
{
  "title": "Updated Meeting Notes"
}
```

**Response**

- `200 OK`

---

## DELETE `/notes/<id>`

Deletes a note owned by the authenticated user.

**Response**

- `204 No Content`

---

# Database Models

## User

Stores authentication information.

### Fields

- id
- username
- password_hash

### Relationship

A User can have many Notes.

---

## Note

Stores notes created by authenticated users.

### Fields

- id
- title
- content
- created_at
- updated_at
- user_id

---

# Features

- User registration
- User login and logout
- Session-based authentication
- Secure password hashing with Flask-Bcrypt
- Full CRUD operations for notes
- Pagination for notes
- Protected routes
- User-specific authorization
- Database migrations with Flask-Migrate
- Seed script with sample data

---

# Project Structure

```text
productivityapp-auth-backend/
│
├── migrations/
│
├── server/
│   ├── .env.example
│   ├── __init__.py
│   ├── app.py
│   ├── auth.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── seed.py
│   └── ...
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Testing

The API can be tested using **Postman**.

Suggested testing flow:

1. Register a user using `POST /signup`
2. Log in using `POST /login`
3. Verify authentication with `GET /me`
4. Create a note using `POST /notes`
5. Retrieve notes using `GET /notes?page=1`
6. Update a note using `PATCH /notes/<id>`
7. Delete a note using `DELETE /notes/<id>`
8. Log out using `DELETE /logout`
9. Verify protected routes return `401 Unauthorized` after logout
10. Confirm one user cannot access another user's notes

---

# Author

**Philip Muchiru**