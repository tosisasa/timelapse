import datetime
import twitter
import sys
import tweetkey

args = sys.argv
filepath = args[1]

api = twitter.Api(tweetkey.CONSUMER_KEY,
                  tweetkey.CONSUMER_SECRET,
                  tweetkey.ACCESS_KEY,
                  tweetkey.ACCESS_SECRET)

message = '#ソライロ'
api.PostUpdate(message, media=filepath)
