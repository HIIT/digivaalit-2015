import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='article-body' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':

	nouda("http://suomenkuvalehti.fi/jutut/kotimaa/politiikka/timo-soini-aikoo-olla-puheenjohtaja-viela-vuoden-2019-vaaleissa/?shared=74287-e5d264da-500", file('suomenkuvalehti.txt', 'w'))

