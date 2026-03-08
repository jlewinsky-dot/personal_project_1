from fetch_rick_and_morty import fetch_all_characters
from get_connection import get_db_connection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Fetching characters...")
    characters = fetch_all_characters()
    logger.info("Inserting character data into MySQL database")
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.executemany(
            'INSERT INTO personal_project_1 (id, name, status, species) VALUES (%s, %s, %s, %s)',
            [(character['id'], character['name'], character['status'], character['species']) for character in characters]
            )
        conn.commit()

if __name__ == '__main__':
    main()
    