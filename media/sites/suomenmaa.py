import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( class_='containerJuttu' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write(repr(string))

if __name__ == '__main__':

	nouda("http://www.suomenmaa.fi/etusivu/7399391.html", file('suomenmaa.txt', 'w'))

