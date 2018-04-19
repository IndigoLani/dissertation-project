import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv

#Access Twitter API app functionality
consumer_secret = 'wgaOupTa80hOGfx6H4EmJ2suLb5mJR3UbfARiGrq4ZuGuoST1k'
consumer_key = 	'kqphtDVP1o02tjtMeXRBwI2RT'

access_token = '955398272058888192-Z4Alh2xOaDojmjVSZyxk27po1ebDEvo'
access_token_secret = 'NpUPxzSbcLVJMoQ5IsTeZoiC8JKy9NgI1lK5CW6k4GZms'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class listener(StreamListener):

    def on_status(self, status):
        if ("RT @" not in status.text):
            print(status.text)
            file = open("sarcasm_training_data.txt","a")
            file.write(status.text.encode("utf-8"))
            file.write('\n')
            file.close()
            return(True)

    def on_error(self, status):
        print(status)

twitterStream = Stream(auth, listener())

#Filter tweets by searchterm
twitterStream.filter(track = ["#sarcasm"])
