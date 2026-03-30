import requests
import time
import json
import os

# This is the key require to access TMDB APIs 
API_KEY = "1d90e30056293a84c655513c26f94c7e"

# Base url fetches show level info of shows
def fetch_popular_shows(page):
    fetch_url = f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=en-US&page={page}"

    fetch_url_response = requests.get(fetch_url, timeout=10)
    return fetch_url_response

# season url fetches season level info of shows
def fetch_show_details(show_id):
    for attempt in range(3):
        try:
            detail_url = f"https://api.themoviedb.org/3/tv/{show_id}?api_key={API_KEY}"
            response = requests.get(detail_url, timeout=10)
            return response
        except Exception as e:
            if attempt < 2:
                time.sleep(5)
            else:
                raise e
season_result = []

for i in range(1, 51):
    try:
        fetch_response = fetch_popular_shows(i)
        fetch_data = fetch_response.json()
        season_result.extend(fetch_data['results'])
    except Exception as f:
        print(f"Skipping page: {i}")
        continue
    time.sleep(1)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, '..', 'data', 'raw', 'tmdb_popular_shows.json')
file_check = os.path.exists(filepath)

if file_check == True:
    with open(filepath, 'r') as m:
        existing_data = json.load(m)
        season_result = existing_data + season_result
else:
    pass

# Deduplicating by ID
seen = set()
unique_shows = []
for show in season_result:
    if show['id'] not in seen:
        seen.add(show['id'])
        unique_shows.append(show)

season_result = unique_shows

with open(filepath, 'w') as f:
    json.dump(season_result, f, indent=2)

print(f"Saved {len(season_result)} shows")




# response = requests.get(f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=en-US&page=1")
# print(response.status_code)




# r = requests.get(f"https://api.themoviedb.org/3/tv/1871?api_key={API_KEY}", timeout=10, stream=False)
# print(r.status_code)
# # print(r.json())

