# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import datetime

def parse( url ):

    page = requests.get( url )
    page = BeautifulSoup( page.text )

    for story in page.find_all( 'li' ):
        if story.find('a'):
            print story.find('a').get('href')


## example

path = 'http://www.hs.fi/ajax/aihe/lisaa/1296808807055?tagId=1296808773222' ## pääkirjotukset

for i in range(0, 150):
    parse( path + '&page=' + str(i) )
