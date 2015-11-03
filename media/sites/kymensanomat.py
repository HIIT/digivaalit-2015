import requests

from bs4 import BeautifulSoup
import bs4

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='news-item' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.kymensanomat.fi/Online/2015/04/02/Kotkan%20tori%20t%C3%A4yttyi%20vaalipuheista%20ja%20ehdokkaista/2015318855714/4", file('kymeensanomat.txt', 'w'))
