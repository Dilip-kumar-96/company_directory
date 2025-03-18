from flask import request, jsonify
import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.environ.get('dbname'),
    user=os.environ.get('user'),
    password=os.environ.get('password'),
    host=os.environ.get('host')
)


def validate_create_employee_input_data(data):  # data = {"reports_to" : 100000,"salary" : 500000}

    if isinstance(data, list):
        for i in data:
            if len(i) != 3:
                raise Exception("make sure the input has 3 values")
    else:
        dict_len = len(data)
        if dict_len != 3:
            raise Exception("make sure the input has 3 values")


def employee_check(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from company_directory.employee_data where employee_id = %s;", (id,))
    record = cursor.fetchall()
    conn.commit()
    cursor.close()
    if len(record) == 0:
        raise Exception("employee unavailable")


def welcome():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * from company_directory.employee_data;")
        # Fetch all rows from database
        record = cursor.fetchall()
        print("Data from Database:- ", record)
        return record
    except Exception as e:
        return jsonify({"message": f"error occurred: {e}"}), 500


def employee_profile(id):
    try:
        try:
            employee_check(id)
        except Exception as e:
            return jsonify({"message": str(e)}), 404
        cursor = conn.cursor()
        cursor.execute("SELECT * from company_directory.employee_data where employee_id = %s;", (id,))

        # Fetch all rows from database
        record = cursor.fetchall()
        record = record[0]
        columns_data = cursor.description
        columns = []
        for col in columns_data:
            columns.append(col[0])
        result = jsonify(dict(zip(columns, record)))
        return result, 200
    except Exception as e:
        return jsonify({"message": f"error occurred: {e}"}), 500


def create_employee():
    try:
        try:
            employee_check(id)
        except Exception as e:
            return jsonify({"message": str(e)}), 404

        cursor = conn.cursor()
        data = request.get_json()
        insert_query = "insert into company_directory.employee_data (employee_name, reports_to, salary) values (%s, %s, %s)"
        values = (data['employee_name'], data['reports_to'], data['salary'])
        try:
            cursor.execute(insert_query, values)
        except psycopg2.errors.InvalidTextRepresentation:
            conn.commit()  # Once the error has handled it doesn't handle the next time unless the server is restarted.
            # the transaction will be pending and throws error next. The transaction needs to either rolled back or changes need to be commited.
            return jsonify({"message": "invalid data type"})
        conn.commit()
        cursor.close()
        return jsonify({"message": "employee created successfully!"}), 201
    except Exception as e:
        return jsonify({"message": f"error occurred: {e}"}), 500


def create_employee_batch():
    try:
        cursor = conn.cursor()
        data = request.get_json()
        try:
            validate_create_employee_input_data(data)
        except Exception as e:
            return jsonify({"message": str(e)})

        insert_query = "insert into company_directory.employee_data (employee_name, reports_to, salary) values (%s, %s, %s)"
        values_list = []
        for i in data:
            values_list.append((i['employee_name'], i['reports_to'], i['salary']))
            try:
                cursor.executemany(insert_query, values_list)
            except psycopg2.errors.InvalidTextRepresentation:
                conn.commit()  # Once the error has handled it doesn't handle the next time unless the server is restarted.
                # the transaction will be pending and throws error next. The transaction needs to either rolled back or changes need to be commited.
                return jsonify({"message": "invalid data type"})

        conn.commit()
        cursor.close()

        return jsonify(
            {"message": "employee_batch created successfully!"}), 201
    except Exception as e:
        return jsonify({"message": f"error occurred: {e}"}), 500


def delete_employee(id):
    try:
        try:
            employee_check(id)
        except Exception as e:
            return jsonify({"message": str(e)}), 404
        cursor = conn.cursor()
        cursor.execute("delete from company_directory.employee_data where employee_id = %s", (id,))

        conn.commit()
        cursor.close()

        return jsonify({"message": "employee has been deleted!"}), 200
    except Exception as e:
        return jsonify({"message": f"error occurred: {e}"}), 500


def update_employee():
    try:
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
            print(col_name)
            print(col_value)
            cursor.execute("update company_directory.employee_data set {} = %s where employee_id = %s".format(col_name),
                           (col_value, emp_id))

        conn.commit()
        cursor.close()

        return jsonify({"message": "employee has been updated!"}), 200
    except Exception as e:
        return jsonify({"message": f"error occurred: {e}"}), 500


def employee_aggregation():
    cursor = conn.cursor()
    data = request.args.to_dict()
    col_name = next(iter(data))
    col_value = data[col_name]
    cursor.execute("select * from company_directory.employee_data where {} = %s".format(col_name), (col_value,))
    record = cursor.fetchall()
    conn.commit()
    cursor.close()
    return record, 200
