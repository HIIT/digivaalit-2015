## Twitter API only provides the latest 3k statuses
## this script allows us to go deeper into Twitter history by using
## their website

import requests
import bs4
import re
import datetime

match_id = '.*/([0-9]+)'

def _collect_ids( username , date ):

    date2 = date + datetime.timedelta( 1 )

    url = 'https://mobile.twitter.com/search?src=typd&q=from%3A' + username + '%20since%3A' + date.isoformat() + '%20until%3A' + date2.isoformat()

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

        print date

    return tweets



if __name__ == '__main__':
    print len( collect_tweets( 'Jyrkikasvi', datetime.date( 2011, 1, 1 ), datetime.date( 2011, 1, 31 ) ) )
