from flask import Flask, render_template
import os
import random
import spotify
import genius
temp=[]
app = Flask(__name__)
@app.route('/')
def hello_world():
    artists = ['0gxyHStUsqpMadRV0Di1Qt','2iEvnFsWxR0Syqu2JNopAd','7cTXfwpe9peK0UE1bZyIWZ']
    random_top_track = spotify.getTopTracks(artists[random.randint(0,2)])
    rand_song = random.choice(random_top_track)
    return render_template(
        'index.html',
        rand_song = rand_song,
        rand_song_lyrics_url = genius.get_lyrics(rand_song['name'],rand_song['artist'])
        )


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
