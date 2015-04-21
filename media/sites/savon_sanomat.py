import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='body' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.savonsanomat.fi/uutiset/kotimaa/itsenaisyyspaivan-korkein-kunniamerkki-arkkipiispa-makiselle/1944316", file('savon.txt', 'w'))
