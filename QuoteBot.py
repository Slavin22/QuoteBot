# Dependencies
import pandas as pd
import tweepy
import time
import json
import random

# Twitter API Keys
consumer_key = "1kiIH7jZF7PQUUJ8toc34qyRg"
consumer_secret = "kz9fQqtyTzI82nGcJEewRwOfOg9NJgbZFKXH8SIq3mCuIvKJw5"
access_token = "907734081244450817-sCHEcTJYiHb8A0PLWdJUe1K3pqwVPU7"
access_token_secret = "QZnnI0g3IO5r9MLhpw9aVz0k5VOuCttM5w2bPduBR04NW"

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - by Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - by Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - by Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - by John Lennon",
    "Happiness is a warm puppy. - by Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - by Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - by Guillaume Apollinaire"]

# Create function for tweeting
def tweet_function(text):
	api.update_status(str(text))

# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Tweet a random quote
#random_quote = happy_quotes[random.randrange(0,len(happy_quotes), 1)]
#tweet_function(random.quote)

# Print success message
print()

# Set timer to run every minute
while(True):
    random_quote = happy_quotes[random.randrange(0,len(happy_quotes), 1)]
    tweet_function(random_quote)
    print("Successful Tweet")
    time.sleep(60)