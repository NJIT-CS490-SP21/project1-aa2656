import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_KEY')
CLIENT_SECRET = os.getenv('SPOTIFY_KEY')

#URL to get AUTH
AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST requesting client credential auth token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

#get the access token from json
auth_response_data = auth_response.json()
# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'market':'US'
}


def getTopTracks(artist_ID):
    top_tracks=[]
    BASE_URL='https://api.spotify.com/v1/artists/'
    
    artist_ID=artist_ID
    search = requests.get(BASE_URL+artist_ID+'/top-tracks', headers=headers, params=params)

    for track in search.json()['tracks']:
        try:
            top_tracks.append({
                'name':track['name'],
                'artist':track['artists'][0]['name'],
                'image':track['album']['images'],
                'preview':track['preview_url']
            })
        except:
            top_tracks.append({
                'name':'Never Gonna Give You Up',
                'artist':'Rick Astley',
                'image':[{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273237665d08de01907e82a7d8a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d0000b273237665d08de01907e82a7d8a', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000b273237665d08de01907e82a7d8a', 'width': 64}],
                'preview':'https://p.scdn.co/mp3-preview/22bf10aff02db272f0a053dff5c0063d729df988?cid=008468e3cc40485389d5bc87871f2c3c'
            })
    return top_tracks
