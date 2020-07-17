#!/usr/bin/env python3
import os
import tweepy
import json
import argparse
from quotes import QUOTES
from jokes import JOKES

parser = argparse.ArgumentParser(description="Script to tweet")
parser.add_argument('--type', help="Type of tweet. Can be motivational or joke.")
args = parser.parse_args()

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

if args.type == "motivation":
    data = QUOTES
    config = "{0}/counter.json".format(DIR_PATH)
elif args.type == "joke":
    data = JOKES
    config = "{0}/jokes_counter.json".format(DIR_PATH)

HASH_TAGS = ["#CodeNewbie", "#100daysofcode", "#tech", "#python", "#javascript"]

auth = tweepy.OAuthHandler(os.environ["CONSUMER_API_KEY"], os.environ["CONSUMER_API_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

a_file = open(config, "r")
day = json.load(a_file)['day']
a_file.close()

tweet = "{0}\n".format(data[day])
for tag in HASH_TAGS:
    tweet += f"{tag} "
print(tweet)

new_day = day + 1
with open(config, "w+") as f_obj:
    f_obj.write(json.dumps({"day": new_day}))

api.update_status(tweet)

