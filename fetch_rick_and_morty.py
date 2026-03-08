import requests
import json
from retry_dec import retry
import time
import logging

@retry(attempts=3, delay=2)
def fetch_page(url:str):
    response = requests.get(url)
    if response.status_code == 404:
        return {"results": None}
    if not response.ok:
        raise Exception(f"API returned {response.status_code}")
    return response.json()

def fetch_all_characters():
    all_characters = []
    keys = ['id', 'name', 'status', 'species']
    page = 1

    while True:
        url = f'https://rickandmortyapi.com/api/character/?page={page}'
        print(url)
        data = fetch_page(url)
        results = data.get('results')
        if not results:
            break
        for character in results:
            all_characters.append({k: character.get(k, None) for k in keys})
        page += 1
        time.sleep(0.5)

    return all_characters