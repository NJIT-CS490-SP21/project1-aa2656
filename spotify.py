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
        top_tracks.append({
            'song_name':'name',
            'artist':track['artists'][0]['name'],
            'image':track['album']['images']
            
        })
        
    return top_tracks

artist = getTopTracks('0gxyHStUsqpMadRV0Di1Qt')
for i in range(len(artist)):
    print(i)
    print(artist[i])