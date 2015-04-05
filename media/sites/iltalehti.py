import requests

from bs4 import BeautifulSoup
import bs4

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( 'isense' )

	for e in teksti[0]:
		if isinstance( e, bs4.element.Tag):
			if not e.get('id') and e.string and not e.get('type'): ## hack, fixme
				out.write( repr( e.string ) )

if __name__ == '__main__':
	
	nouda("http://www.iltalehti.fi/uutiset/2014120218885176_uu.shtml", file('ilta.txt', 'w'))
