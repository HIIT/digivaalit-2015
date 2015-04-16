import requests
import datetime

from bs4 import BeautifulSoup

def nouda( out ):	

	for x in range(0,1):

		r = requests.get('http://www.esaimaa.fi/vaalit')
		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( class_='news-ingress' ):

			a = teksti.find('a').get('href')

			out.write('http://www.esaimaa.fi' + a + "\n")
	
if __name__ == '__main__':
	
	nouda("http://www.esaimaa.fi/vaalit", file('linkki_esaimaa.txt', 'w'))
