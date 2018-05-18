#!/usr/bin/python3
from flask_oauth import OAuth
from flask import Flask, request, redirect, url_for, session, g, flash, render_template
from app import app
import tweepy

#oauth = OAuth()
access_token = '997520616570826752-p42rYkP6tBjYtsymr1fxtJfNYbr9Iyq'
access_secret = 'N25zWuENM3ZsDFwfvCKT6IA4ba5AM5tJpCK4FBJOgQleI'
 
# Use Twitter as example remote application
#twitter = oauth.remote_app('twitter',
#    base_url='https://api.twitter.com/1/',
#    request_token_url='https://api.twitter.com/oauth/request_token',
#    access_token_url='https://api.twitter.com/oauth/access_token',
#    authorize_url='https://api.twitter.com/oauth/authenticate',
#)
consumer_key='mvygqcyft9NXLWZeqFdjEDk1X'
consumer_secret='cCgRiVlpIkIkETa7o6yFi097PLeYjT9B83cAB1F3Rr0s4uLJGf'
callback_url = 'http://surfperch.holberton.us'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

listofTweets = tweepy.Cursor(api.search, q='holberton').items(10)

for mytweet in listofTweets:
    try:
        api.retweet(mytweet.id_str)
    except:
        pass

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
