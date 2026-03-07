import mysql.connector
from dotenv import load_dotenv
import os

def get_db_connection():
    load_dotenv()
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv('DB_PW'),
        database=os.getenv('DB')
    )
    return connection