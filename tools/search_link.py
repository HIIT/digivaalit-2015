#!/usr/bin/python
# _*_ coding: utf-8

import json
import requests
import sys
import requests
import bs4

data = None

if sys.argv[1].endswith('.json'):

    data = json.load( open( sys.argv[1] ) )

    data = map( lambda entry: entry[ sys.argv[3] ] , data )
    data = filter( lambda entry: entry != None, data )

else:

    data = open( sys.argv[1] )


for url in data:

    try:
        site = requests.get( url )
        site = bs4.BeautifulSoup( site.text )

        for link in site.find_all('a'):
            if sys.argv[ 2] in link.get('href'):
                print link.get('href')
    except:
        pass
