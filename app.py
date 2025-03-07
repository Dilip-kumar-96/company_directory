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


@app.route("/employee/<int:id>")
def employee_profile(id):
    cursor = conn.cursor()

    cursor.execute("SELECT * from company_directory.employee_data where employee_id = %s;", (id,))

    # Fetch all rows from database
    record = cursor.fetchall()
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


@app.route("/create/employee_batch", methods=['POST'])  # Send json data in the form of list
def create_employee_batch():
    cursor = conn.cursor()
    data = request.get_json()
    insert_query = "insert into company_directory.employee_data (employee_id, manager_id, employee_name, manager_name, salary) values (%s, %s, %s, %s, %s)"
    values_list = []
    created_employee_ids = []
    for i in data:
        values_list.append((i['employee_id'], i['manager_id'], i['employee_name'], i['manager_name'], i['salary']))
        created_employee_ids.append(i['employee_id'])
    cursor.executemany(insert_query, values_list)
    conn.commit()
    cursor.close()

    return jsonify(
        {"message": "employee_batch created successfully!", "newly created employee id's": created_employee_ids}), 201


@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_employee(id):
    cursor = conn.cursor()

    cursor.execute("delete from company_directory.employee_data where employee_id = %s", (id,))

    conn.commit()
    cursor.close()

    return jsonify({"message": "employee has been deleted!"}), 200


@app.route("/update/employee", methods=['POST'])
def update_employee():
    cursor = conn.cursor()
    data = request.get_json()
    emp_id = data.get("employee_id")
    if not emp_id:
        return jsonify({"message": "employee id is missing!"}), 400
    for key, value in data.items():
        if key == "employee_id":
            continue
        col_name = key
        col_value = value
        cursor.execute("update company_directory.employee_data set {} = %s where employee_id = %s".format(col_name),
                       (col_value, emp_id))

    conn.commit()
    cursor.close()

    return jsonify({"message": "employee has been updated!"}), 200

@app.route("/employee")
def employee_aggrigation():
    cursor = conn.cursor()
    data = request.args.to_dict()
    col_name = next(iter(data))
    col_value = data[col_name]
    cursor.execute("select * from company_directory.employee_data where {} = %s".format(col_name), (col_value,))
    record = cursor.fetchall()
    conn.commit()
    cursor.close()
    return record, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
