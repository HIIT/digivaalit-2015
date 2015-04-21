import requests
import datetime

from bs4 import BeautifulSoup

def nouda( out ):

	lapi = raw_input("Monta uutissivua lapi(20 uutista per sivu): ")

	lapi_num = int(lapi)

	sivu = 0	

	for x in range(0,lapi_num):

		sivu_str = str(sivu)

		r = requests.get( 'http://www.karjalainen.fi/eduskuntavaalit?src=nav&start=' + sivu_str)
		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( id='des_text' ):

			a = teksti.find('a').get('href')

			out.write('http://www.karjalainen.fi' + a + "\n")
		sivu = sivu + 20
	
if __name__ == '__main__':
	
	nouda("http://www.karjalainen.fi/eduskuntavaalit?src=nav&start=0", file('linkki_karjalainen.txt', 'w'))
