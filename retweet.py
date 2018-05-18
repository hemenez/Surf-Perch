#!/usr/bin/python3
"""App"""
from flask import Flask, render_template, request
from app import app


#flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# oauth route
consumer_key = 'mvygqcyft9NXLWZeqFdjEDk1X'
consumer_secret = 'cCgRiVlpIkIkETa7o6yFi097PLeYjT9B83cAB1F3Rr0s4uLJGf'
callback = ''
session = {}

@app.route('/auth')
def auth():
    """redirect user to Twitter login page"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    return redirect(url)


@app.route('/callback')
def twitter_callback():
    """redirect user to callback URL"""
    request_token = session['request_token']
    del session['request_token']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)
    session['token'] = (auth.access_token, auth.access_token_secret)

    return redirect('/app')


@app.route('/app')
def request_twitter:
    token, token_secret = session['token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)

    return api.me()


@app.route('/search', methods=['POST'])
def search():
    """search twitter by keyword"""
    query = request.form['searchID']
    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Fetch tweets with query
    num_tweets = 1
    search_tweets = tweepy.Cursor(api.search, query).items(num_tweets)

    for tweet in search_tweets:
        tweet_id = tweet.id_str

    # Retweet
    api.retweet(tweet_id)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
