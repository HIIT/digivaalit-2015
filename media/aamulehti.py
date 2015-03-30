import requests

from bs4 import BeautifulSoup

r = requests.get("http://www.aamulehti.fi/Kotimaa/1194944556756/artikkeli/vapaavuori+fortum+turvaa+fennovoiman+kotimaisuuden.html")
r.encoiding = 'UTF-8'
soup = BeautifulSoup( r.text )

teksti = soup.find_all( class_='Teksti' )

for i in teksti:
    print i

i.contents[0]

for string in i.stripped_strings:
        print(repr(string))
