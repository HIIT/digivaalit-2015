import requests
import datetime

from bs4 import BeautifulSoup

def nouda( out ):	

	for x in range(0,1):

		r = requests.get('http://www.talouselama.fi/vaalit')
		r.encoding = 'UTF-8'
		soup = BeautifulSoup( r.text )

		for teksti in soup.find_all( class_='article news' ):
			for luokka in teksti.find_all(class_='media news'):

				a = luokka.find('a').get('href')

				out.write(a + "\n")
	
if __name__ == '__main__':
	
	nouda("http://www.talouselama.fi/vaalit", file('linkki_talouselama.txt', 'w'))
