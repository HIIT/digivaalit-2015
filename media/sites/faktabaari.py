import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='entry-content' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':

	nouda("http://faktabaari.fi/fakta/petrus-pennanen-energiewende-oli-kaynnissa-jo-2002/", file('faktabaari.txt', 'w'))

