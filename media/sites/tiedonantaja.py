import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( class_='article' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.tiedonantaja.fi/2015-23-3/maailman-sosiaalifoorumi-tukee-tunisian-demokraattista-kehitysta", file('tiedonantaja.txt', 'w'))
