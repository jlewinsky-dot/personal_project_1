import mysql.connector
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

def get_db_connection():
    load_dotenv()
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PW'),
            database=os.getenv('DB')
        )
    except mysql.connector.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise
    return connection