import os
import psycopg2

def db_connect():
        conn = psycopg2.connect(
            dbname=os.environ.get('dbname'),
            user=os.environ.get('user'),
            password=os.environ.get('password'),
            host=os.environ.get('host')
        )
        return conn