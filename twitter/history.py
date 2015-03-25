## Twitter API only provides the latest 3k statuses
## this script allows us to go deeper into Twitter history by using
## their website

import requests
import bs4
import re
import datetime

import tweepy
from secrets import *

import time

auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessTokenKey,AccessTokenSecret)
twitter = tweepy.API(auth)

match_id = '.*/([0-9]+)'

def _collect_ids( username , date ):

    date2 = date + datetime.timedelta( 1 )

    url = 'https://mobile.twitter.com/search?src=typd&q=from:' + username + ' since:' + date.isoformat() + ' until:' + date2.isoformat()

    r = requests.get( url )

    page = bs4.BeautifulSoup( r.text )

    ret = []

    for tweet in page.find( class_ ='timeline' ).children:

        if isinstance( tweet , bs4.Tag ):

            ## get tweet ID
            if 'href' in tweet.attrs:
                href = tweet['href']
                href = re.search( match_id, href )
                ret.append( (int)( href.group(1) ) )

            ## TODO: check if count > 19; then need to parse more

    return ret

def collect_tweets( username, since, until ):

    date = since

    tweets = []

    while date <= until:

        tweets += _collect_ids( username, date )
        date = date + datetime.timedelta( 1 )

    ret = []

    for tweet in tweets:

        t = None

        while not t:

            try:
                t = twitter.get_status( tweet )._json
            except tweepy.error.TweepError:
                time.sleep( 60 * 5 ) ## wait for ratelimit to come back

        ret.append( t )

    return ret

if __name__ == '__main__':
    for t in collect_tweets( 'Jyrkikasvi', datetime.date( 2011, 1, 1 ), datetime.date( 2011, 1, 15 ) ):
        print t['text'].encode('utf8')
