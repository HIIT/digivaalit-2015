# -*- coding: utf-8 -*-

import requests
import json
import time
import datetime

from sites import yle

def data( path,
    end = datetime.datetime.now().replace( hour=0, minute=0, second=0, microsecond=0  ) ,
    begin = datetime.datetime.now().replace( hour=23, minute=59, second=59, microsecond=0  )  ):

    ## estimate scale, how many news we need to collect
    scale = ( (begin - end).days + 1 ) * 10

    if scale > 100:
        scale = 100

    scale = str( scale )

    ## fix time formats
    import time

    current = int( time.mktime( begin.timetuple() ) * 1000 )
    end = int( time.mktime( end.timetuple() ) * 1000 )

    ## collect data from current time to end
    while current > end:

        ## load urls
        jsonpath = path + 'amount=' + scale
        jsonpath += '&before=' + str( current )

        r = requests.get( jsonpath )

        articles = r.json()['articles']

        current = articles[-1]['timestamp']

        for article in articles:

            link = article['link']
            time = str( article['timestamp'] )

            yle.nouda( link, open( './data/' + time + '.txt', 'w') )



data( 'http://yle.fi/uutiset/resources/ajax/latest?category=politiikka&includeSubsections=true&homeSectionOnly=false&' ,
datetime.datetime(2014, 6, 1), datetime.datetime(2014, 12, 31) )
