import requests
import datetime
import time

from bs4 import BeautifulSoup

def nouda( out ):

	laskuri = []

	print "Today(vuosi, kuukausi, paiva): ", datetime.date.today()

	paiva = raw_input("Paiva: ")
	kuukausi = raw_input("Kuukausi: ")
	vuosi = raw_input("Vuosi: ")

	lapi = raw_input("Monta paivaa lapi: ")

	lapi_num = int(lapi)	

	paiva_num = int(paiva)
	kuukausi_num = int(kuukausi)
	vuosi_num = int(vuosi)

	for x in range(0,lapi_num):

		paiva_str = str(paiva_num)
		kuukausi_str = str(kuukausi_num)
		vuosi_str = str(vuosi_num)

		r = requests.get( 'http://www.aamulehti.fi/cs/Satellite?pagename=Premium/Presentation/TopicArticleListExtra&site=KAL_newssite&auth=false&topicMain=1194924055819&time='+ vuosi_str +'-'+ kuukausi_str + '-' + paiva_str )
		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		if paiva_num == 0:
			paiva_num = 31
			kuukausi_num = kuukausi_num - 1

		if kuukausi_num == 0:
			kuukausi_num = 12
			vuosi_num = vuosi_num - 1

		for teksti in soup.find_all( class_='ingress' ):

			a = teksti.find('a').get('href')
				
			if a not in laskuri:
				laskuri.append(a)

		paiva_num = paiva_num - 1

	out.write(repr(laskuri))
	
if __name__ == '__main__':
	
	nouda("http://www.aamulehti.fi/Kotimaa/1194924055819/artikkeli/eduskuntavaalit+2015.html", file('linkki.txt', 'w'))
