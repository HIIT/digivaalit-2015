import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='article-body' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://seura.fi/puheenaihe/ajankohtaista/vasemmisto-kehuu-kokoomusta-harjoittavat-rehellisesti-politiikkaa-joka-on-ajanut-suomen-lamaan/?shared=43026-ad87bd06-500", file('seura.txt', 'w'))
