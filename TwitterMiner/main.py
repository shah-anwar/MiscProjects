import tweepy
from tweepy import OAuthHandler
from config import *

#api keys stored in config.py, ignored by git (for security)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)