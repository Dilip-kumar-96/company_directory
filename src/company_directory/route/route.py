import psycopg2
from flask import request, jsonify

from src.company_directory.route import main

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="dilip1231",
    host="localhost"
)


@main.route("/show_employee_table")
def welcome():
    cursor = conn.cursor()

    cursor.execute("SELECT * from company_directory.employee_data;")

    # Fetch all rows from database
    record = cursor.fetchall()

    print("Data from Database:- ", record)
    return record


@main.route("/create/employee", methods=['POST'])
def create_employee():
    cursor = conn.cursor()
    data = request.get_json()
    insert_query = "insert into company_directory.employee_data (employee_id, manager_id, employee_name, manager_name, salary) values (%s, %s, %s, %s, %s)"
    values = (data['employee_id'], data['manager_id'], data['employee_name'], data['manager_name'], data['salary'])

    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    return jsonify({"message": "employee created successfully!"}), 201
