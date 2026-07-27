# 🚀 FastAPI & REST API Mastery Lab

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlite)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-e91e63?style=for-the-badge)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **FastAPI & REST API Mastery Lab**! This repository documents a step-by-step evolution from core REST API concepts to building a full-fledged, production-ready **School Management REST API** built with FastAPI, SQLAlchemy, Pydantic, and SQLite.

---

## 📂 Repository Structure

The project is structured logically into daily progressive modules:

```text
fastapi-rest-api-mastery/
│
├── 01_rest_api_basics/        # Day 1: Fundamentals of HTTP methods & REST endpoints
├── 02_employee_api/           # Day 2: Employee Management CRUD API
├── 03_movie_api/              # Day 3: Movie Catalog API with structured schemas
├── 04_auth_and_exceptions/    # Day 4: Exception Handling & Custom Middleware
└── 05_school_management_api/  # Day 5: Full Modular FastAPI School System (Users, Teachers, Students, Books)
```

---

## 🌟 Progressive Learning Journey

### 1️⃣ `first day` (REST API Basics)
- Basic REST architecture, request routes, and JSON responses.
- Handling `GET` and `POST` methods.

### 2️⃣ `second day` (Employee API)
- Implementing standard CRUD operations for Employee records.
- Integrating basic data models.

### 3️⃣ `third day` (Movie API)
- Structuring APIs with modular routers and request schemas.
- Filtering and managing movie inventories.

### 4️⃣ `forth day` (Auth & Exception Handling)
- Centralized exception handlers for `404 Not Found` and validation errors.
- Custom authentication/authorization header verification middleware.

### 5️⃣ `fifth day` (Full School Management System) 🏆
A full-stack backend modular application featuring:
- **Teachers CRUD**: Manage faculty profiles with `GET`, `POST`, `PUT`, `DELETE`.
- **User & Student Portal**: User registration and student assignment models.
- **Library Management**: Relational schema associating Books with Students & Users (`ManyToMany` relationships with SQLAlchemy).
- **ORM & Database**: Configured SQLite with SQLAlchemy ORM models (`app/models.py`).
- **Data Validation**: Strict Pydantic v2 schemas (`app/schemes.py`).

---

## 🛠️ Tech Stack & Dependencies

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Database**: SQLite
- **Security**: JWT & Passlib (OAuth2 ready)

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/umaimanoreen/fastapi-rest-api-mastery.git
cd fastapi-rest-api-mastery
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Full School Management API (Day 5)
```bash
# Navigate to the fifth day folder or run uvicorn
cd "fifth day"
uvicorn app.main:app --reload
```

---

## 📑 Interactive API Documentation

Once the server is running, explore the interactive Swagger documentation generated automatically by FastAPI:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📜 License
This project is licensed under the MIT License. Feel free to use it for learning and project development!
