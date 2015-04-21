import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( class_='grid__item two-thirds article__body--container' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.kauppalehti.fi/uutiset/putin-nayttaytyi-julkisuudessa-ilman-juoruja-olisi-tylsaa/pBBPEhQ2?ext=ampparit", file('kauppalehti.txt', 'w'))
