## Twitter API only provides the latest 3k statuses
## this script allows us to go deeper into Twitter history by using
## their website

import requests
import bs4
import re

match_id = '.*/([0-9]+)'

def _collect_ids( username , date ):

    url = 'https://mobile.twitter.com/search?src=typd&q=from%3AJyrkikasvi%20since%3A2011-01-01%20until%3A2011-04-01'

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

    return ret

if __name__ == '__main__':
    print _collect_ids( 'matnel', 'x' )
