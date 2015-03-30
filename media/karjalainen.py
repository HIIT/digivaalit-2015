import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='itemFullText' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':
	
	nouda("http://www.karjalainen.fi/uutiset/uutis-alueet/kotimaa/item/62227-vaitos-jos-naapurit-ovat-hyvaa-pataa-toistensa-kanssa-talossa-on-turvallista", file('karjalainen.txt', 'w'))
