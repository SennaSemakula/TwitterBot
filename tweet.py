#!/usr/bin/env python3
import os
import tweepy
import json
from quotes import QUOTES

HASH_TAGS = ["#CodeNewbie", "#100daysofcode", "#tech", "#python", "#javascript"]

auth = tweepy.OAuthHandler(os.environ["CONSUMER_API_KEY"], os.environ["CONSUMER_API_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

a_file = open("counter.json", "r")
day = json.load(a_file)['day']
a_file.close()

tweet = "{0}\n".format(QUOTES[day])
for tag in HASH_TAGS:
    tweet += f"{tag} "
print(tweet)

new_day = day + 1

with open("counter.json", "w+") as f_obj:
    f_obj.write(json.dumps({"day": new_day}))

api.update_status(tweet)

