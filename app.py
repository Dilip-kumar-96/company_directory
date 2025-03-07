from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="dilip1231",
    host="localhost"
)


@app.route("/show_employee_table")
def welcome():
    cursor = conn.cursor()

    cursor.execute("SELECT * from company_directory.employee_data;")

    # Fetch all rows from database
    record = cursor.fetchall()

    print("Data from Database:- ", record)
    return record


@app.route("/create/employee", methods=['POST'])
def create_employee():
    cursor = conn.cursor()
    data = request.get_json()
    insert_query = "insert into company_directory.employee_data (employee_id, manager_id, employee_name, manager_name, salary) values (%s, %s, %s, %s, %s)"
    values = (data['employee_id'], data['manager_id'], data['employee_name'], data['manager_name'], data['salary'])

    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    return jsonify({"message": "employee created successfully!"}), 201

@app.route("/create/employee_batch", methods=['POST']) #Send json data in the form of list
def create_employee():
    cursor = conn.cursor()
    data = request.get_json()
    insert_query = "insert into company_directory.employee_data (employee_id, manager_id, employee_name, manager_name, salary) values (%s, %s, %s, %s, %s)"
    values_list = []
    for i in data:
        values_list.append((i['employee_id'], i['manager_id'], i['employee_name'], i['manager_name'], i['salary']))

    cursor.executemany(insert_query, values_list)
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
