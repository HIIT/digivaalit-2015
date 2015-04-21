import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( id='main_text' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.esaimaa.fi/vaalit/2015/04/14/Kolumni%3A%20Mit%C3%A4%20tied%C3%A4mme%20p%C3%A4%C3%A4ministerist%C3%A4/2015118896734/478", file('esaimaa.txt', 'w'))
