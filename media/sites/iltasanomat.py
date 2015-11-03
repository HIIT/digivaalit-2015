import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_= "content-inner" )
	teksti[0].find( class_ = 'side-ads' ).decompose()

	map( lambda x: x.extract() , teksti[0].find_all('script')  )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.iltasanomat.fi/ulkomaat/art-1288789081654.html", file('iltasa.txt', 'w'))
