import tweepy
from textblob import TextBlob
import key

consumer_key = key.consumer_key
consumer_secret = key.consumer_secret

access_token = key.access_token
access_token_secret = key.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(q='turkey', count=300)

for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
