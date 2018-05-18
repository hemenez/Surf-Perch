import tweepy
import json
import time

# SurfPerch account verification
access_token = "997520616570826752-p42rYkP6tBjYtsymr1fxtJfNYbr9Iyq"
access_token_secret = "N25zWuENM3ZsDFwfvCKT6IA4ba5AM5tJpCK4FBJOgQleI"
consumer_key = "mvygqcyft9NXLWZeqFdjEDk1X"
consumer_secret = "cCgRiVlpIkIkETa7o6yFi097PLeYjT9B83cAB1F3Rr0s4uLJGf"

if __name__ == '__main__':

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Fetch tweets with query
    query = ''
    search_tweets = tweepy.Cursor(api.search, query).items()

    for tweet in search_tweets:
        tweet_id = tweet.id_str
    print(search_tweets)

    def retweet(api, tweet_id):
        success = False
        try:
            a=api.retweet(tweet_id)

            # Sleep for 2 seconds, Thanks Twitter
            print("Sleeping...")
            time.sleep(30)
            success = True
        except tweepy.TweepError as e:
            print("Got into the error")
            a=e.response.text
            b=json.loads(a)
            error_code = b['errors'][0]['code']
            
            if(error_code == 327):
                success = True
 
        return success

    api.retweet(tweet_id)
