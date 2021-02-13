import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLIENT_ACCESS = os.getenv('CLIENT_ACCESS_TOKEN')

headers = {
    'Authorization': f'Bearer {CLIENT_ACCESS}'
}

BASE_URL = 'https://api.genius.com'

def get_lyrics(song_name,artist):
    try:
        r = requests.get(
            BASE_URL+"/search",
            headers=headers,
            data={'q':song_name.replace(' ','_')+artist.replace(' ','_')}
        )
        
        return r.json()['response']['hits'][0]['result']['url']
    except:
        return None