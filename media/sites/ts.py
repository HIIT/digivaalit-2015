import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( class_='tsv3-c-common-article__text' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write(repr(string))
if __name__ == '__main__':

	nouda("http://www.ts.fi/eduskuntavaalit/750980/Start+up+yrittaja+kuplii+innostusta", file('ts.txt', 'w'))

