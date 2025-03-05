import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="dilip1231",
    host="localhost"
)
cursor = conn.cursor()

cursor.execute("SELECT * from learning.persons;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)
 print ("created git repository")