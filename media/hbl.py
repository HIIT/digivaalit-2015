import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( id ='nodebody' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':
	
	nouda("http://hbl.fi/nyheter/2014-12-03/690266/hawking-ai-kan-vara-slutet-oss", file('hbl.txt', 'w'))
