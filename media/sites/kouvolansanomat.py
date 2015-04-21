import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( id='main_text' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	nouda("http://www.kouvolansanomat.fi/vaalit2015/2015/04/14/Ennakko%C3%A4%C3%A4nestys%20vilkkaampaa%20kuin%20edellisiss%C3%A4%20vaaleissa%20%E2%80%94%20kolmasosa%20kouvolalaisista%20on%20jo%20%C3%A4%C3%A4nest%C3%A4nyt/20151430/386", file('kouvolansanomat.txt', 'w'))
