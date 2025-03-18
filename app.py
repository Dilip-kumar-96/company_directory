from flask import Flask
from services import welcome, employee_profile, update_employee, create_employee, create_employee_batch, employee_aggregation, delete_employee

app = Flask(__name__)

@app.route("/show_employee_table")
def main_employee_table():
    return welcome()


@app.route("/employee/<int:id>")
def main_employee_profile(id):
    return employee_profile(id)


@app.route("/create/employee", methods=['POST'])
def main_create_employee():
    return create_employee()


@app.route("/create/employee_batch", methods=['POST'])  # Send json data in the form of list
def main_create_employee_batch():
    return create_employee_batch


@app.route("/delete/<int:id>", methods=['DELETE'])
def main_delete_employee(id):
    return delete_employee(id)


@app.route("/update/employee", methods=['POST'])
def main_update_employee():
    return update_employee()


@app.route("/employee")
def main_employee_aggregation():
    return employee_aggregation()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
