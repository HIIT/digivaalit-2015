import feedparser
import pickle
import requests

hub = "http://feeds.feedburner.com/ampparit-politiikka" ## collect from ampparit all politics related sites

feed = feedparser.parse( hub )

stored = []

try:
    stored = pickle.load( open( '.history' , 'r' ) )
except:
    pass

stored = []

out = open( 'urls.txt' , 'a')

for item in feed['items']:

    link = item['links'][0]['href']
    _id = link.split('?id=')[1]

    if _id not in stored:

        r = requests.head( link )

        url = r.headers.get('location')

        out.write( _id + ',' +  url + '\n' )

        stored.append( _id )

pickle.dump( stored, open( '.history' , 'w' ) )
