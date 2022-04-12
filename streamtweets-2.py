import tweepy
import json

from tweepy import OAuthHandler

from tweepy.streaming import StreamListener

from tweepy import Stream
from tweepy import API
#Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

class FileWriteListener(StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self.save_file = open('tweets2022.json','w')
        self.tweets = []

    def on_data(self, tweet):
        self.tweets.append(json.loads(tweet))
        self.save_file.write(str(tweet))

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, FileWriteListener())
# Here you can filter the stream by:
#    - keywords (as shown)
#    - users
twitter_stream.filter(track=[ '#JacindaArdern', '@JacindaArdern'])
