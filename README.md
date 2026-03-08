# Rick and Morty Character Database

A practice project that fetches character data from the [Rick and Morty API](https://rickandmortyapi.com/) and stores it in a MySQL database.

## What It Does

1. Pulls all characters from the Rick and Morty API (paginated)
2. Extracts `id`, `name`, `status`, and `species` for each character
3. Inserts the data into a MySQL table

## Setup

### Prerequisites

- Python 3
- MySQL running locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```
DB_PW=your_mysql_password
DB=your_database_name
```

### Database

Make sure your MySQL database has a table like:

```sql
CREATE TABLE personal_project_1 (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(50),
    species VARCHAR(100)
);
```

## Run

```bash
python main.py
```

## Project Structure

| File | Description |
|---|---|
| `main.py` | Entry point — fetches characters and inserts them into the DB |
| `fetch_rick_and_morty.py` | Handles paginated API calls to the Rick and Morty API |
| `get_connection.py` | Creates a MySQL connection using env variables |
| `retry_dec.py` | Custom retry decorator with exponential backoff |
