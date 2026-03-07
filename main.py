import requests
import json
from retry_dec import retry

@retry(attempts=3, delay=2)
def fetch_page(url):
    response = requests.get(url)
    if not response.ok:
        raise Exception(f"API returned {response.status_code}")
    return response.json()

def fetch_all_characters():
    all_characters = []
    keys = ['id', 'name', 'status', 'species']
    page = 1

    while True:
        data = fetch_page(f'https://rickandmortyapi.com/api/character/?page={page}')
        results = data.get('results')
        if not results:
            break
        for character in results:
            all_characters.append({k: character.get(k, None) for k in keys})
        page += 1

    return all_characters