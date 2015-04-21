import requests
import datetime

from bs4 import BeautifulSoup

def nouda( out ):	

	for x in range(0,1):

		r = requests.get('http://www.satakunnankansa.fi/vaalit')
		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( class_='ingressi' ):

			a = teksti.find('a').get('href')

			jako1, jako2 = a.split(".",1)

			if jako1 == "http://www":

				out.write(a + "\n")

			else:
				out.write('http://www.satakunnankansa.fi' + a + '\n')
	
if __name__ == '__main__':
	
	nouda("http://www.satakunnankansa.fi/vaalit", file('linkki_satakunnankansa.txt', 'w'))
