import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='Teksti' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.aamulehti.fi/Kotimaa/1194944556756/artikkeli/vapaavuori+fortum+turvaa+fennovoiman+kotimaisuuden.html", file('aamulehti.txt', 'w'))
