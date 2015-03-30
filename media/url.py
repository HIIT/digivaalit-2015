import requests

import yle
import aamulehti
import ess
import hbl
import ilkka
import iltalehti
import iltasanomat
import kaleva
import karjalainen
import keski_suomalainen
import lapinkansa
import maaseudun_tulevaisuus
import satakunnan_kansa
import savon_sanomat
import hs


from bs4 import BeautifulSoup

add = raw_input('Url: ')

txt = raw_input('Tiedoston nimi(esim yle.txt): ')

a,b,c = add.split(".", 2)

if b == "yle":
	yle.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "aamulehti":
	aamulehti.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "ess":
	ess.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "hbl":
	hbl.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "hs":
	hs.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "ilkka":
	ilkka.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "iltalehti":
	iltalehti.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "iltasanomat":
	iltasanomat.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "kaleva":
	kaleva.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "karjalainen":
	karjalainen.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "ksml":
	keski_suomalainen.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "lapinkansa":
	lapinkansa.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "maaseuduntulevaisuus":
	maaseudun_tulevaisuus.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "satakunnankansa":
	satakunnan_kansa.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

elif b == "savonsanomat":
	savon_sanomat.nouda(add, file(txt, 'w'))
	print(b + ":\n" + "Kirjoitus onnistui")

else: 
	print("Error sivua ei voitu kirjoittaa tai koodi ei toimi urlin kanssa.")

