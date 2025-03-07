from flask import Flask, request
import psycopg2
app = Flask(__name__)
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="dilip1231",
    host="localhost"
)
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