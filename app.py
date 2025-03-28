from flask import Flask
from services import employee_services

app = Flask(__name__)
emp_serve = employee_services()

@app.route("/show_employee_table")
def main_employee_table():
    return emp_serve.welcome()


@app.route("/employee/<int:id>")
def main_employee_profile(id):
    return emp_serve.employee_profile(id)


@app.route("/create/employee", methods=['POST'])
def main_create_employee():
    return emp_serve.create_employee()


@app.route("/create/employee_batch", methods=['POST'])  # Send json data in the form of list
def main_create_employee_batch():
    return emp_serve.create_employee_batch()


@app.route("/delete/<int:id>", methods=['DELETE'])
def main_delete_employee(id):
    return emp_serve.delete_employee(id)


@app.route("/update/employee", methods=['POST'])
def main_update_employee():
    return emp_serve.update_employee()


@app.route("/employee")
def main_employee_aggregation():
    return emp_serve.employee_aggregation()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
