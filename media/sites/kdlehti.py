import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )

	## seems that some content has been deleted
	if r.status_code == 404:
		return

	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='content' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.kdlehti.fi/2015/03/15/paivi-rasanen-internetin-terrorismisisaltoon-puututtava-tehokkaammin/", file('kdlehti.txt', 'w'))
