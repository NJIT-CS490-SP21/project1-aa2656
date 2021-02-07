from flask import Flask, render_template
import os
import random
import spotify

app = Flask(__name__)

@app.route('/')
def hello_world():
    artists = ['0gxyHStUsqpMadRV0Di1Qt','2iEvnFsWxR0Syqu2JNopAd','7cTXfwpe9peK0UE1bZyIWZ']
    random_top_track = spotify.getTopTracks(artists[random.randint(0,2)])
    return render_template(
        'index.html',
        rand_song = random.choice(random_top_track),
        none = None
        )


app.run(
    port = 8080,
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
