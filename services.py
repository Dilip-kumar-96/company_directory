from flask import request, jsonify
from database_conn import db_connect
import psycopg2


conn = db_connect()

class employee_services:
    def __init__(self):
        self.cursor = conn.cursor()

    def validate_create_employee_input_data(self,data):  # data = {"reports_to" : 100000,"salary" : 500000}
        self.cursor = conn.cursor()
        if isinstance(data, list):
            for i in data:
                if len(i) != 3:
                    raise Exception("make sure the input has 3 values")
        else:
            dict_len = len(data)
            if dict_len != 3:
                raise Exception("make sure the input has 3 values")


    def employee_check(self, id):
        self.cursor.execute("SELECT * from company_directory.employee_data where employee_id = %s;", (id,))
        record = self.cursor.fetchall()
        conn.commit()
        if len(record) == 0:
            raise Exception("employee unavailable")


    def welcome(self):
        try:
            self.cursor.execute("SELECT * from company_directory.employee_data;")
            # Fetch all rows from database
            record = self.cursor.fetchall()
            print("Data from Database:- ", record)
            return record
        except Exception as e:
            return jsonify({"message": f"error occurred: {e}"}), 500


    def employee_profile(self, id):
        try:
            try:
                self.employee_check(id)
            except Exception as e:
                return jsonify({"message": str(e)}), 404
            self.cursor.execute("SELECT * from company_directory.employee_data where employee_id = %s;", (id,))

            # Fetch all rows from database
            record = self.cursor.fetchall()
            record = record[0]
            columns_data = self.cursor.description
            columns = []
            for col in columns_data:
                columns.append(col[0])
            result = jsonify(dict(zip(columns, record)))
            self.cursor.close()
            return result, 200
        except Exception as e:
            return jsonify({"message": f"error occurred: {e}"}), 500


    def create_employee(self):
        try:
            data = request.get_json()

            try:
                self.validate_create_employee_input_data(data)
            except Exception as e:
                return jsonify({"message": str(e)})

            insert_query = "insert into company_directory.employee_data (employee_name, reports_to, salary) values (%s, %s, %s)"
            values = (data['employee_name'], data['reports_to'], data['salary'])
            try:
                self.cursor.execute(insert_query, values)
            except psycopg2.errors.InvalidTextRepresentation:
                conn.commit()  # Once the error has handled it doesn't handle the next time unless the server is restarted.
                # the transaction will be pending and throws error next. The transaction needs to either rolled back or changes need to be commited.
                return jsonify({"message": "invalid data type"})
            conn.commit()
            self.cursor.close()
            return jsonify({"message": "employee created successfully!"}), 201
        except Exception as e:
            return jsonify({"message": f"error occurred: {e}"}), 500


    def create_employee_batch(self):
        try:
            data = request.get_json()
            try:
                self.validate_create_employee_input_data(data)
            except Exception as e:
                return jsonify({"message": str(e)})

            insert_query = "insert into company_directory.employee_data (employee_name, reports_to, salary) values (%s, %s, %s)"
            values_list = []
            for i in data:
                values_list.append((i['employee_name'], i['reports_to'], i['salary']))
                try:
                    self.cursor.executemany(insert_query, values_list)
                except psycopg2.errors.InvalidTextRepresentation:
                    conn.commit()  # Once the error has handled it doesn't handle the next time unless the server is restarted.
                    # the transaction will be pending and throws error next. The transaction needs to either rolled back or changes need to be commited.
                    return jsonify({"message": "invalid data type"})

            conn.commit()
            self.cursor.close()

            return jsonify(
                {"message": "employee_batch created successfully!"}), 201
        except Exception as e:
            return jsonify({"message": f"error occurred: {e}"}), 500


    def delete_employee(self, id):
        try:
            try:
                self.employee_check(id)
            except Exception as e:
                return jsonify({"message": str(e)}), 404
            self.cursor.execute("delete from company_directory.employee_data where employee_id = %s", (id,))

            conn.commit()
            self.cursor.close()

            return jsonify({"message": "employee has been deleted!"}), 200
        except Exception as e:
            return jsonify({"message": f"error occurred: {e}"}), 500


    def update_employee(self):
        try:
            data = request.get_json()

            try:
                self.employee_check(id)
            except Exception as e:
                return jsonify({"message": str(e)}), 404

            emp_id = data.get("employee_id")
            if not emp_id:
                return jsonify({"message": "employee id is missing!"}), 400
            for key, value in data.items():
                if key == "employee_id":
                    continue
                col_name = key
                col_value = value
                self.cursor.execute("update company_directory.employee_data set {} = %s where employee_id = %s".format(col_name),
                               (col_value, emp_id))

            conn.commit()
            self.cursor.close()

            return jsonify({"message": "employee has been updated!"}), 200
        except Exception as e:
            return jsonify({"message": f"error occurred: {e}"}), 500


    def employee_aggregation(self):
        data = request.args.to_dict()
        col_name = next(iter(data))
        col_value = data[col_name]
        self.cursor.execute("select * from company_directory.employee_data where {} = %s".format(col_name), (col_value,))
        record = self.cursor.fetchall()
        conn.commit()
        self.cursor.close()
        return record, 200