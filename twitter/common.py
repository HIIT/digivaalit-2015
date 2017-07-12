import tweepy
import time
import math

from secrets import *

auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessTokenKey,AccessTokenSecret)
twitter = tweepy.API(auth)

def tweets( ids ):

    ret = []

    ## the API can take 100 per time
    count = len( ids ) / 100.0
    count = int( math.ceil( count ) )

    for i in range( 0, count ):

        _ids = ids[ i * 100 : ( i + 1 ) * 100 ]

        print i, count, len( _ids )

        _ids = ','.join( _ids )


        t = None
        while not t:
            try:
                t = twitter._statuses_lookup( _ids, tweet_mode='extended' ) ## extended gets the full tweet text if truncated
                t = map( lambda x: x._json , t )
            except tweepy.error.TweepError:
                time.sleep( 60 * 15 ) ## wait for ratelimit to come back
        ret += t

    return ret
