#!/usr/bin/env python3
import os
from datetime import date
import time
from pprint import pprint
import tweepy
import json
from quotes import QUOTES

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
HASH_TAGS = ["#CodeNewbie", "#100daysofcode", "#tech", "#python", "#javascript"]

auth = tweepy.OAuthHandler(os.environ["CONSUMER_API_KEY"], os.environ["CONSUMER_API_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

config = "{0}/counter.json".format(DIR_PATH)
favourites = api.favorites()

for tweet in tweepy.Cursor(api.search, ["#100DaysOfCode"]).items(100):
    try:
        if tweet.id not in favourites and tweet.favorited == False:
            time.sleep(10)
            print(tweet.favorited)
            api.create_favorite(tweet.id)
            print("favouriting tweet with id {}".format(tweet.id))
    except tweepy.error.TweepError as e:
        print(e)
        print("Skipping tweet with id: {}".format(tweet.id))
    
ids = []

pprint(api.rate_limit_status())

for fav in favourites:
    ids.append(fav.id)



