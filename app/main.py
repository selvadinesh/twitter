from flask import Flask
app = Flask(__name__)

import tweepy
import config
client = tweepy.Client(config.BEARER_TOKEN, config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
authenticator = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(authenticator, wait_on_rate_limit=True)
def search_twitter(query=''):

    client.search_recent_tweets(query= query)

def create_tweet(tweet_text=''):

    client.create_tweet(text = tweet_text)

@app.route('/')
def welcome():
    return 'Welcome to SelvaTwitter'

def main():
    search_twitter(query ='TESLA')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()