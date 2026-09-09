import re

from database import get_connection
from psycopg2.errors import UniqueViolation


def get_valid_employee_id():
    while True:
        try:
            employee_id = int(input("Enter employee ID: "))
            return employee_id
        except ValueError:
            print("Invalid employee ID. Please enter a number.")


def is_valid_email(email):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def add_employee():

    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        while True:
            name = input("Enter employee name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        while True:
            email = input("Enter employee email: ").strip()
            if is_valid_email(email):
                break
            print("Invalid email. Please enter a valid email address.")

        while True:
            department = input("Enter department: ").strip()
            if department:
                break
            print("Department cannot be empty.")

        while True:
            try:
                salary = float(input("Enter salary: "))
                if salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break

            except ValueError:
                print("Invalid salary. Please enter a number.")

        query = """
        INSERT INTO employees (name, email, department, salary)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, email, department, salary))

        connection.commit()

        print("Employee added successfully!")

    except UniqueViolation:
        connection.rollback()
        print("Email already exists. Please use another email.")

    except Exception as error:
        connection.rollback()
        print("Error adding employee:", error)

    finally:
        cursor.close()
        connection.close()

def view_employees():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    if not employees:
        print("No employees found.")
    else:
        print("\n==================== EMPLOYEES ====================")

        print(
            f"{'ID':<5}"
            f"{'Name':<20}"
            f"{'Email':<30}"
            f"{'Department':<15}"
            f"{'Salary':>12}"
        )

        print("-" * 82)

        for employee in employees:
            print(
                f"{employee[0]:<5}"
                f"{employee[1]:<20}"
                f"{employee[2]:<30}"
                f"{employee[3]:<15}"
                f"{employee[4]:>12.2f}"
            )

    cursor.close()
    connection.close()

def search_employee():
    print("\n========== SEARCH EMPLOYEE ==========")
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Email")

    choice = input("Enter your choice: ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    if choice == "1":
        employee_id = get_valid_employee_id()

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = %s",
            (employee_id,)
        )

    elif choice == "2":
        name = input("Enter employee name: ").strip()

        cursor.execute(
            "SELECT * FROM employees WHERE name ILIKE %s",
            (f"%{name}%",)
        )

    elif choice == "3":
        email = input("Enter employee email: ").strip()

        cursor.execute(
            "SELECT * FROM employees WHERE email ILIKE %s",
            (f"%{email}%",)
        )

    else:
        print("Invalid choice.")
        cursor.close()
        connection.close()
        return

    employees = cursor.fetchall()

    if not employees:
        print("No employees found.")
    else:
        print("\n==================== SEARCH RESULTS ====================")

        print(
            f"{'ID':<5}"
            f"{'Name':<20}"
            f"{'Email':<30}"
            f"{'Department':<15}"
            f"{'Salary':>12}"
        )

        print("-" * 82)

        for employee in employees:
            print(
                f"{employee[0]:<5}"
                f"{employee[1]:<20}"
                f"{employee[2]:<30}"
                f"{employee[3]:<15}"
                f"{employee[4]:>12.2f}"
            )

    cursor.close()
    connection.close()


def update_employee():
    employee_id = get_valid_employee_id()

    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()

    # Check whether employee exists
    cursor.execute(
        "SELECT * FROM employees WHERE employee_id = %s",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if employee is None:
        print("Employee not found.")
        cursor.close()
        connection.close()
        return

    print("\n========== EMPLOYEE DETAILS ==========")
    print(f"Name: {employee[1]}")
    print(f"Email: {employee[2]}")
    print(f"Department: {employee[3]}")
    print(f"Salary: {employee[4]}")

    print("\nEnter new details.")
    print("Press Enter to keep the current value.")

    department = input(
        f"Department [{employee[3]}]: "
    ).strip()

    while True:
        salary_input = input(
            f"Salary [{employee[4]}]: "
        ).strip()

        if salary_input == "":
            salary = employee[4]
            break

        try:
            salary = float(salary_input)

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid salary. Please enter a number.")

    if department == "":
        department = employee[3]

    cursor.execute(
        """
        UPDATE employees
        SET department = %s,
            salary = %s
        WHERE employee_id = %s
        """,
        (department, salary, employee_id)
    )

    connection.commit()

    print("Employee updated successfully.")

    cursor.close()
    connection.close()

def delete_employee():
    employee_id = get_valid_employee_id()

    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name FROM employees WHERE employee_id = %s",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if employee is None:
        print("Employee not found.")
        cursor.close()
        connection.close()
        return

    print(f"Employee found: {employee[0]}")

    confirmation = input("Are you sure you want to delete this employee? (y/n): ").lower()

    if confirmation == "y":
        cursor.execute(
            "DELETE FROM employees WHERE employee_id = %s",
            (employee_id,)
        )

        connection.commit()
        print("Employee deleted successfully.")

    else:
        print("Delete cancelled.")

    cursor.close()
    connection.close()