import requests

from bs4 import BeautifulSoup
import bs4

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_ ="article-text-content" )

	for e in teksti[0]:
		if isinstance( e, bs4.element.Tag):
			if not e.get('class') and e.string:
				out.write( e.string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.hs.fi/paakirjoitukset/a1428030701507", file('hs.txt', 'w'))
