#!/usr/bin/python3

from app import app
import requests
import tweepy

# callback_url = 'https://twitter.com'

auth = tweepy.OAuthHandler('mvygqcyft9NXLWZeqFdjEDk1X', 'cCgRiVlpIkIkETa7o6yFi097PLeYjT9B83cAB1F3Rr0s4uLJGf', callback_url)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

session.set('request_token', auth.request_token)

verifier = request.GET.get('oauth_verifier')

# Let's say this is a web app, so we need to re-build the auth handler
# first...
# auth = tweepy.OAuthHandler('mvygqcyft9NXLWZeqFdjEDk1X', 'cCgRiVlpIkIkETa7o6yFi097PLeYjT9B83cAB1F3Rr0s4uLJGf')
token = session.get('request_token')
session.delete('request_token')
auth.request_token = { 'oauth_token' : token,
                         'oauth_token_secret' : verifier }

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token.')

key = auth.access_token
secret = auth.access_token_secret

auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('tweepy + oauth!')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
