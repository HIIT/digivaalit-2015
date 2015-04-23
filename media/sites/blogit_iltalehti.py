import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='entry-content' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') )

if __name__ == '__main__':

	nouda("http://blogit.iltalehti.fi/eija-riitta-korhola/2015/03/15/visioni-helsingista-kansainvalinen-metropoli/", file('blogit.txt', 'w'))
