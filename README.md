# Productivity App Backend

## Project Description

The Productivity App Backend is a Flask REST API that allows users to register, log in, and manage personal notes. The application uses session-based authentication, ensuring that users can only access and modify their own data.

The backend uses Flask-Bcrypt for password hashing and Flask-Migrate for database migrations.

This backend is intended to work with the provided frontend for the project.

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

## 4. Apply database migrations

If you're cloning the project for the first time, simply run:

```bash
flask db upgrade
```

If you modify the database models later, generate and apply a new migration:

```bash
flask db migrate -m "Describe your changes"
flask db upgrade
```

---

## 5. Seed the database

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

Registers a new user account.

### Request Body

```json
{
  "username": "philip",
  "password": "password123"
}
```

Returns:
- **201 Created** on success.

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

Returns:
- **200 OK** when login succeeds.
- **401 Unauthorized** for invalid credentials.

---

## GET `/me`

Returns the currently authenticated user.

Returns:
- **200 OK**
- **401 Unauthorized** if no active session exists.

---

## DELETE `/logout`

Ends the current user session.

Returns:
- **204 No Content**

---

# Notes Endpoints

> All Notes endpoints require an authenticated user.

---

## GET `/notes`

Returns all notes belonging to the authenticated user.

Example:

```
GET /notes?page=1
```

Returns:
- **200 OK**

---

## GET `/notes/<id>`

Returns a specific note belonging to the authenticated user.

Returns:
- **200 OK**
- **401 Unauthorized**
- **404 Not Found**

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

Returns:
- **201 Created**

---

## PATCH `/notes/<id>`

Updates an existing note.

### Request Body

```json
{
  "title": "Updated Meeting Notes"
}
```

Returns:
- **200 OK**

---

## DELETE `/notes/<id>`

Deletes a note belonging to the authenticated user.

Returns:
- **204 No Content**

---

# Database Models

## User

Stores user authentication information.

### Fields
- id
- username
- password_hash

### Relationships
- One User has many Notes.

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

- User registration and login
- Session-based authentication
- Secure password hashing with Flask-Bcrypt
- CRUD operations for notes
- Pagination for notes
- Protected routes
- User-specific authorization
- Database migrations with Flask-Migrate
- Seed data for testing

---

# Project Structure

```text
productivityapp-auth-backend/
│
├── migrations/
│
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── auth.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── seed.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

# Testing

The API can be tested using **Postman**.

Recommended authentication flow:

1. Register a user using `/signup`
2. Log in using `/login`
3. Verify the session with `/me`
4. Create notes using `/notes`
5. Retrieve notes using `/notes?page=1`
6. Update and delete notes
7. Log out using `/logout`
8. Verify protected routes return **401 Unauthorized** after logout

---

# Author

**Philip Muchiru**
```
