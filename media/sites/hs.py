import requests

from bs4 import BeautifulSoup
import bs4

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( id="article-text-content" )
	for e in teksti[0]:
		if isinstance( e, bs4.element.Tag):
			if not e.get('class'):
				out.write( repr( e.string ) )

if __name__ == '__main__':
	
	nouda("http://www.hs.fi/ulkomaat/a1417488621135", file('hs.txt', 'w'))
