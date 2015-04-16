import requests
import datetime

from bs4 import BeautifulSoup

def nouda( out ):

	lapi = raw_input("Monta uutissivua lapi(20 uutista per sivu): ")

	lapi_num = int(lapi)

	sivu = 0	

	for x in range(0,lapi_num):

		sivu_str = str(sivu)

		r = requests.get( 'http://www.iltasanomat.fi/dev/laneitems/1288883382405/moreItems?from=' + sivu_str + '&pageId=1288883368835&lanePosition=main&even=false')
		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( class_='teaser' ):

			a = teksti.find('a').get('href')

			out.write('http://www.iltasanomat.fi' + a + "\n")
		sivu = sivu + 20
	
if __name__ == '__main__':
	
	nouda("http://www.iltasanomat.fi/dev/laneitems/1288883382405/moreItems?from=0&pageId=1288883368835&lanePosition=main&even=false", file('linkki_iltasanomat.txt', 'w'))
