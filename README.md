# 🚀 FastAPI & REST API Mastery Lab

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlite)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-e91e63?style=for-the-badge)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **FastAPI & REST API Mastery Lab**! This repository documents a step-by-step evolution from core REST API concepts to building a full-fledged, production-ready **School Management REST API** built with FastAPI, SQLAlchemy, Pydantic, and SQLite.

---

## 📂 Repository Structure

The project is structured logically into self-contained, topic-focused modules:

```text
fastapi-rest-api-mastery/
│
├── 01_rest_api_basics/             # REST HTTP methods & endpoint basics
│   └── main.py
│
├── 02_employee_crud_api/           # Employee CRUD operations API
│   ├── main.py
│   └── models.py
│
├── 03_movie_catalog_api/           # Movie Catalog API with structured routes
│   ├── main.py
│   └── models.py
│
├── 04_auth_and_exceptions_api/     # Custom Exception Handlers & Authorization middleware
│   ├── main.py
│   └── authorization.py
│
└── 05_school_management_system/    # Full Modular FastAPI School System (Users, Teachers, Students, Books)
    ├── .env
    └── app/
        ├── __init__.py
        ├── main.py
        ├── auth.py
        ├── config.py
        ├── database.py
        ├── models.py
        └── schemas.py
```

---

## 🌟 Modules Breakdown

### 1️⃣ `01_rest_api_basics`
- Fundamentals of RESTful web services.
- Basic request routing (`GET`, `POST`) and JSON responses.

### 2️⃣ `02_employee_crud_api`
- Complete CRUD (Create, Read, Update, Delete) cycle for Employee data.
- Basic model representation and request handling.

### 3️⃣ `03_movie_catalog_api`
- Movie catalog service.
- Query parameter filtering, item creation, and collection retrieval.

### 4️⃣ `04_auth_and_exceptions_api`
- Advanced error handling: custom HTTP exceptions (`404 Not Found`, validation errors).
- Custom request headers & token authorization middleware.

### 5️⃣ `05_school_management_system` 🏆
Production-grade modular FastAPI application featuring:
- **Teachers API**: Full CRUD endpoints (`/teachers`) with status codes & validation.
- **Students & Users Portal**: Linked user accounts and student profiles.
- **Library Management**: Relational schema associating Books with Students & Users (`ManyToMany` relationships with SQLAlchemy).
- **ORM & Database**: Configured SQLite with SQLAlchemy ORM models (`app/models.py`).
- **Data Validation**: Strict Pydantic v2 schemas (`app/schemas.py`).

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

### 4. Run the Full School Management API (Module 5)
```bash
cd 05_school_management_system
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
