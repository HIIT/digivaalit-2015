import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( id='fullarticle' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write(repr(string))

if __name__ == '__main__':

	nouda("http://www.kansanuutiset.fi/kulttuuri/kirjat/3341821/lahi-idan-rajoja-vedetaan-uusiksi", file('kansanuutiset.txt', 'w'))

