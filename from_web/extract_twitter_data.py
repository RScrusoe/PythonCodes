"""
Created on Sun Oct 04 23:10:41 2015
@author: ujjwal.karn
"""

#first, install pip by following instructions here: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows 
#then, to install tweepy library, go to Anaconda command prompt and type: pip install tweepy
#once tweepy is installed, run the codes below:

import tweepy    #this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
 
#provide your access details below 
access_token = "2888657887-q2wFGgVjo5NYO2cI3YKZ0NToGjNAIGq5SBnzoCM"
access_token_secret = "eTHW9okj8TNTlq8qRBGszojDnL76CqXin4G82gRFcWBvy"
consumer_key = "Ts3sieLqzJWLINx27AYPQNqWC"
consumer_secret = "dHIkTBAIZ5ZKCVWDr4OVj9rDjmHwAfle69oIZWlAqhegZrpR6X"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
print("Doing...")
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('/home/rs/Documents/my_python/from_web/data.txt', 'a') as f:  #change location here
                f.write(data)
                return True
        except BaseException as e:
            print("error")
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print("ERROR")
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#cricket'])
