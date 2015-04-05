import tweepy
import time

from secrets import *

auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessTokenKey,AccessTokenSecret)
twitter = tweepy.API(auth)

def tweets( ids ):

    ret = []
    for tweet in ids:
        t = None
        while not t:
            try:
                t = twitter.get_status( tweet )._json
            except tweepy.error.TweepError:
                time.sleep( 60 * 5 ) ## wait for ratelimit to come back
        ret.append( t )

    return ret
