📌 FundooNotes Backend (FastAPI)
🚀 Overview

FundooNotes is a backend REST API built using FastAPI that supports user authentication, secure note management, labels, and automated testing.

🧰 Tech Stack

FastAPI

PostgreSQL

SQLAlchemy

JWT Authentication

Argon2 Password Hashing

PyTest

Postman

🔐 Features

User Registration & Login

JWT-based Authentication

Create, Read, Update, Delete Notes

Labels Management

User-scoped Data Access

Password Reset using Token

Automated API Tests (PyTest)

▶️ Run the Application
uvicorn src.app.main:app --reload


Access API docs:

http://127.0.0.1:8000/docs

🧪 Run Tests
pytest -v

🗂 Project Structure
backend/
├── src/app
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── logs/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── venv
└── README.md

🔑 Authentication

All protected routes require:

Authorization: Bearer <JWT_TOKEN>

✅ Status

Backend fully functional and tested.