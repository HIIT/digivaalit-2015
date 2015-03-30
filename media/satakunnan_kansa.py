import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='Teksti' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':
	
	nouda("http://www.satakunnankansa.fi/Satakunta/1194944663801/artikkeli/miten+kay+vientiteollisuuteen+nojaavan+meriporin.html", file('satakunnan.txt', 'w'))
