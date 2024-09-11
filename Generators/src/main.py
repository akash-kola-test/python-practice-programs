from collections.abc import Iterable
from dataclasses import dataclass
from typing import List
import time
import mysql.connector as db_connector

conn = db_connector.connect(
    host="localhost",
    port = 32768,
    user="root",
    password="my-secret-pw",
    database="employees"
)


@dataclass
class Employee:
    emp_no: int
    first_name: str
    dept_name: str
    title: str


def get_employees_heavy() -> List[Employee]:
    cursor = conn.cursor()
    query = """ SELECT e.emp_no, e.first_name, d.dept_name, t.title FROM employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    JOIN departments d ON d.dept_no = de.dept_no 
    JOIN titles t ON e.emp_no = t.emp_no
    """
    cursor.execute(query)
    employees = []

    records = cursor.fetchall()

    for record in records:
        employee_record = Employee(
            emp_no=record[0],
            first_name=record[1],
            dept_name=record[2],
            title=record[3]
        )
        employees.append(employee_record)

    return employees


def get_employees(batch_size=100) -> Iterable[Employee]:
    cursor = conn.cursor()
    query = """ SELECT e.emp_no, e.first_name, d.dept_name, t.title FROM employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    JOIN departments d ON d.dept_no = de.dept_no 
    JOIN titles t ON e.emp_no = t.emp_no
    """
    cursor.execute(query)
    while True:
        records = cursor.fetchmany(size=batch_size)
        if records is None:
            break
        for record in records:
            yield Employee(
                emp_no=record[0],
                first_name=record[1],
                dept_name=record[2],
                title=record[3]
            )


for employee in get_employees():
    print(employee.emp_no, employee.first_name, employee.dept_name, employee.title)
    time.sleep(1)
