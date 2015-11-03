import requests

from bs4 import BeautifulSoup
import bs4

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_ = "lead-paragraph" )
	for e in teksti[0].stripped_strings:
		out.write( e.encode('utf8') + ' ' )

	teksti = soup.find_all( class_ = "editorial" )
	teksti[0].find( class_ = 'banner').decompose()

	for e in teksti[0].stripped_strings:
		out.write( e.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.mtv.fi/uutiset/kotimaa/artikkeli/jarjesto-sipilaan-kohdistuneesta-uhkailusta-iltapaivalehdissa-lausunto-hammastyttaa/4918590", file('mtv.txt', 'w'))
