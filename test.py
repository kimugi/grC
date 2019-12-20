import os
import tweepy as tw
import pandas as pd
import preprocessor.api as p
from preprocessor.api import clean, tokenize, parse

consumer_key = 'T7j9icH6CntIwN30SMcB9LpIl'
consumer_secret = 'grAiSvMaNRk18ThdBMdo7yoBt1PeqEzcXt0edwDHZrz0Anwr4C'

access_token = '1207492035680227330-xE1hVJGJwGnEq5o0sM3OvKXOm9nLeO'
access_token_secret = '1vu0fZasQJWQjRXzEmXcOxwFP0AjWhw3uncIohvLn1JiE'

# perform authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create our twitter api to access tweets from it
api = tw.API(auth)

search_words = "Korea"
date_since = "2019-11-16"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(p.clean(tweet.text))


