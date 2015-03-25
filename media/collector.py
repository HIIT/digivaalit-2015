import feedparser
import pickle
import requests
import sys

hub = "http://feeds.feedburner.com/ampparit-politiikka" ## collect from ampparit all politics related sites

feed = feedparser.parse( hub )

stored = []

path = sys.argv[0]

try:
    stored = pickle.load( open(  path  + '/.history' , 'r' ) )
except:
    pass

out = open( path + '/urls.txt' , 'a')

for item in feed['items']:

    link = item['links'][0]['href']
    _id = link.split('?id=')[1]

    if _id not in stored:

        r = requests.head( link )

        url = r.headers.get('location')

        out.write( _id + ',' +  url + '\n' )

        stored.append( _id )

pickle.dump( stored, open( path + '/.history' , 'w' ) )
