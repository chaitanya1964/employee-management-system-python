Employee Management System
A console-based Employee Management System built with Python and
PostgreSQL. The project demonstrates CRUD operations, database
connectivity, input validation, error handling, environment-based
configuration, and automated testing.
Features
Add new employees
View all employees in a formatted table
Search employees by:
Employee ID
Name
Email
Update employee department and salary
Delete employees with confirmation
Validate employee names
Validate email format
Validate salary input
Prevent duplicate email addresses
Handle database connection failures
Automated tests using pytest
Technologies Used
Python
PostgreSQL
SQL
psycopg2
python-dotenv
pytest
Git and GitHub
Project Structure
``` text
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
└── tests/
    ├── __init__.py
    └── test_employee.py
```
> `.env`, `venv/`, cache files, and other local files are excluded from
> Git using `.gitignore`.
Database Schema
The application uses PostgreSQL with an `employees` table.
Column         Type                  Description
---
employee_id    SERIAL PRIMARY KEY    Unique employee ID
name           VARCHAR(100)          Employee name
email          VARCHAR(100) UNIQUE   Employee email
department     VARCHAR(50)           Employee department
salary         NUMERIC(10,2)         Employee salary
joining_date   DATE                  Employee joining date
Create the Database
Create a PostgreSQL database named:
``` text
employee_management
```
Then create the table:
``` sql
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50),
    salary NUMERIC(10, 2),
    joining_date DATE DEFAULT CURRENT_DATE
);
```
Environment Configuration
Create a `.env` file in the project root:
``` text
DB_HOST=localhost
DB_NAME=employee_management
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```
Replace `your_password` with your local PostgreSQL password.
Never commit or share the `.env` file.
Installation
1. Clone the repository
``` bash
git clone https://github.com/chaitanya1964/employee-management-system-python.git
cd employee-management-system-python
```
2. Create a virtual environment
``` bash
python -m venv venv
```
3. Activate the virtual environment
On Windows:
``` bash
venv\Scripts\activate
```
4. Install dependencies
``` bash
pip install -r requirements.txt
```
5. Configure PostgreSQL
Make sure PostgreSQL is running, create the `employee_management`
database, create the `employees` table, and configure the `.env` file.
Run the Application
``` bash
python main.py
```
The application provides the following options:
``` text
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
```
Run Tests
Run the automated tests with:
``` bash
pytest
```
The current test suite covers email validation, including valid and
invalid email formats.
What I Learned
Through this project, I practiced:
Python functions and modules
CRUD operations
SQL queries
PostgreSQL database connectivity
Input validation
Exception handling
Environment variables
Git and GitHub
Automated testing with pytest
Future Improvements
Build a REST API using FastAPI
Add authentication and authorization
Add employee sorting and advanced filtering
Add department-wise reports
Increase automated test coverage
Add a graphical or web-based interface
Author
Krishna Chaitanya
