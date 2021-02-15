# Random Spotify Song Preview(CS490 Project 1)

This is a website that will show a random Spotify song and preview of a top song from a list of artists. It will also include a link to the songs lyrics if it could be found on [genius.com](https://genius.com/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required python libraries that can be found below or in [requirements.txt](https://github.com/NJIT-CS490-SP21/project1-aa2656/blob/main/requirements.txt).

```bash
pip install Flask
pip install requests
pip install python-dotenv
```
## Getting Spotify and Genius keys
1) Follow [this](https://developer.spotify.com/documentation/web-api/quick-start/) tutorial to get your Spotify keys. Dont go past "Register Your Application"
2) Do the [same](https://docs.genius.com/#/getting-started-h1) for the Genius API keys, don't go past "Registering Your Application". Then goto Generate Access Token, this will be your client token.
3) Take these keys and create a file called ".env", then put the following in the file:
```bash
export SPOTIFY_KEY='your spotify secret key'
export SPOTIFY_CLIENT_KEY='your spotify client key'
export CLIENT_ACCESS_TOKEN='your genius client token'
```
This will allow you to run the website locally. Proceed to the next step if you want to host it publically.
## Deploying the Webapp to Heroku
If you plan on deploying to Heroku for free, do the following.

1) Install the Heroku Command Line Interface with `npm install -g heroku`
2) Create a Heroku account for free at [https://signup.heroku.com/login](https://signup.heroku.com/login)
3) Go back to the command line and login to heroku with `heroku login -i`
4) Create the Heroku app with `heroku create`
5) Run `git push heroku main` to send this code to heroku
6) Go to [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps) and type the keys from your .env file in the setting->"Reveal Config Vars" section so that heroku can access the Spotify and Genius API's
7) Lastly run `heroku open` to get a link to your new website

## Additional Features to Add in the Future
1) Add a button to show the next random song. Currently, you have to refresh the page to get the next random song. I want to implement a button that will show the next song. This will make showing the next random song much more intuitive. I'm currently looking into options shown in [this](https://stackoverflow.com/questions/29884654/button-that-refreshes-the-page-on-click) stack overflow answer. This seems like a simple but very useful addition.
2) I'd also like to add an option to either show or not show the song lyrics link, and it will save between reloads. This can increase the speed that the website is able to show new random previews. This can be implemented by using cookies to save if someone wants to either show or hide the song lyrics. This can be implemented by Flask's [cookie method](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies). The cookie can store whether or not to show the lyrics and then use jinja to check to display the lyrics. If they click the button to display the lyrics for a current song it will use a javascript function to fetch the link to the lyrics if it's available and then add it to the end of the DOM.



## Solved Technical Issues
### Genius Search API
Creating the correct search term for the search request for Genius API is important to get the most accurate result. When first using the search API it would lead to unreliable results for getting the lyrics of a song because I would just search for the song name, which leads to other songs with a similar name to be played. After looking at [this](https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62) very helpful site, I then tried searching for the song, replacing and spaces in the song name with underscores, I then added a space and then the artist name with spaces replaced by underscores again. For example, `Never_Gonna_Give_You_Up Rick_Astley`. Using this method has so far only given me the correct song lyrics or returned with none, which meant that Genius didn't have the lyrics to that song.

### Spotify Preview URL
When first trying to get a song preview, I would display it in HTML using an audio tag. But it wouldn't display, at first I believed it was due to me using the incorrect HTML tag. After a few minutes of looking up how to display Spotify previews in HTML and trying different HTML tags I decided to inspect the website and I found that there was nothing in the src= in the audio tag. I looked back at how I get the preview link, and I realized it was as simple as misspelling a variable name leading to nothing being parsed from the Spotify json response. In the future, be sure to inspect an element before assuming you are using the incorrect element.

### Getting Spotify Authorization Credentials
When first attempting to get authorization credentials from Spotify, it would return an unknown grant type error. After looking up the error message I was able to understand what went wrong was that I was missing the `grant_type` key in my post request. after using the `client_credentials` grant type I was able to get my auth token from Spotify and make a get request for an artist's top songs.