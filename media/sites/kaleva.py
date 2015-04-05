import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( id='body-text' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':
	
	nouda("http://www.kaleva.fi/uutiset/kotimaa/asukkaat-vaativat-junille-nopeusrajoitusta-viime-yona-pamahti-niin-etta-pelkasin-hirren-menneen-poikki/683116/", file('kaleva.txt', 'w'))
