# Employee Management System

A console-based Employee Management System built using Python and PostgreSQL.

This project demonstrates CRUD operations, database connectivity, input validation,
error handling, and automated testing using Python and PostgreSQL.

## Features

- Add new employees
- View all employees
- Search employees by:
  - Employee ID
  - Name
  - Email
- Update employee department and salary
- Delete employees with confirmation
- Validate employee name
- Validate email format
- Validate salary input
- Prevent duplicate email addresses
- Handle database connection errors
- Automated testing using pytest

## Technologies Used

- Python
- PostgreSQL
- SQL
- psycopg2
- python-dotenv
- pytest
- Git

## Project Structure

```text
employee-management-system-python/
│
├── main.py
├── employee.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── tests/
│   ├── __init__.py
│   └── test_employee.py
│
└── venv/


