import requests
import datetime

from bs4 import BeautifulSoup

def nouda( out ):

	lapi = raw_input("Monta uutissivua lapi(20 uutista per sivu): ")

	lapi_num = int(lapi)

	sivu = 1

	r = requests.get( 'http://www.iltamakasiini.fi/haku?hakusanat=vaalit')

	for x in range(0,lapi_num):

		sivu_str = str(sivu)

		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( class_='group-main' ):

			a = teksti.find('a').get('href')

			out.write('http://www.iltamakasiini.fi' + a + "\n")
		sivu = sivu + 1
		
		r = requests.get('http://www.iltamakasiini.fi/haku?hakusanat=vaalit&page=' + sivu_str)
	
if __name__ == '__main__':
	
	nouda("http://www.iltamakasiini.fi/haku?hakusanat=vaalit", file('linkki_iltamakasiini.txt', 'w'))
