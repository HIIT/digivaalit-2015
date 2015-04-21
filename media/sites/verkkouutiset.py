import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( class_='articlepart-1' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.verkkouutiset.fi/talous/ammattisijoittajan_neuvot-33352", file('verkkouutiset.txt', 'w'))
