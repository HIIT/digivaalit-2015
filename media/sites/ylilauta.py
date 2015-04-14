import requests
import datetime
import time

from bs4 import BeautifulSoup

def nouda( out ):

	lapi = raw_input("Monta kommentti sivua lapi: ")

	lapi_num = int(lapi) + 2

	r = requests.get( 'http://ylilauta.org/politiikka/' )

	for x in range(2,lapi_num):

		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( class_='post' ):
			#for p in teksti.find_all('p'):

			for string in teksti.stripped_strings:
				out.write(repr(string)+ '\n')

		x_str = str(x)

		r = requests.get( 'http://ylilauta.org/politiikka' + '-' + x_str )
	
if __name__ == '__main__':
	
	nouda("http://ylilauta.org/politiikka/", file('linkki.txt', 'w'))
