# 🧾 FastAPI - Employee Leave Management API

This project is a RESTful API built with **FastAPI**, **SQLAlchemy**, and **SQLite** to manage employee leave requests.  
It includes validation rules, error handling, and unit testing with **Pytest**.

---

## 📦 Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy ORM
- SQLite (local database)
- Pydantic for validation
- Pytest for testing

---

## 🚀 Features

- ✅ Create leave requests with business rules:
  - `end_date` must be after `start_date`
  - Excludes weekends from leave count
  - No overlapping leave requests
  - Maximum of 14 consecutive working days
- ✅ Retrieve leave requests by employee ID
- ✅ Proper error handling and validation
- ✅ Unit-tested using Pytest

---

## 📂 Project Structure

