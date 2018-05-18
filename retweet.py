#!/usr/bin/python3

from app import app
from models import storage
from flask_oauth import OAuth
from flask import session, request, redirect

oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='mvygqcyft9NXLWZeqFdjEDk1X',
    consumer_secret='cCgRiVlpIkIkETa7o6yFi097PLeYjT9B83cAB1F3Rr0s4uLJGf'
)

@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

@app.route('/login')
def login():
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        print(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    print('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
