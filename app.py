from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="dilip1231",
    host="localhost"
)


@app.route("/")
def welcome():
    cursor = conn.cursor()

    cursor.execute("SELECT * from learning.persons;")

    # Fetch all rows from database
    record = cursor.fetchall()

    print("Data from Database:- ", record)
    return "these are employee details"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
