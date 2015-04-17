import requests

#Uutistenhaku linkeilla
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
import suomenmaa
import verkkouutiset
import demokraatti
import kansanuutiset
import aamuset
#import suomenuutiset
import kdlehti
import seura
#import blogit
import kokemaenjokilaakso
import uusisuomi
import taloussanomat
import vihrealanka
#import kauppalehti
#import mahorkka
import suomenkuvalehti
import hyvaterveys
import ts
import faktabaari
import tiedonantaja
import helsinginuutiset
import esaimaa
import kouvolansanomat
import talouselama
import iltamakasiini


#Linkkien haku uutissivuilta
import linkki_aamulehti
import ylilauta
import linkki_iltasanomat
import linkki_satakunnankansa
import linkki_esaimaa
import linkki_karjalainen
import linkki_kouvolansanomat
import linkki_talouselama
import linkki_iltamakasiini

from bs4 import BeautifulSoup

a = False
while a == False:

	print ("\n1 = uutisten haku\n")
	print ("2 = linkkien haku ja kommenttien\n")
	print ("0 = sulkee ohjelman")

	haku = raw_input('Numero: ')

	haku_num = int(haku)

	if haku_num == 1:

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

		elif b == "suomenmaa":
			suomenmaa.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "verkkouutiset":
			verkkouutiset.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "demokraatti":
			demokraatti.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "kansanuutiset":
			kansanuutiset.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "aamuset":
			aamuset.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		#elif b == "suomenuutiset":
			#suomenuutiset.nouda(add, file(txt, 'w'))
			#print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "kdlehti":
			kdlehti.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "seura":
			seura.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		#elif b =="blogit":
			#blogit.nouda(add, file(txt, 'w'))
			#print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "kokemaenjokilaakso":
			kokemaenjokilaakso.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "uusisuomi":
			uusisuomi.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "taloussanomat":
			taloussanomat.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "vihrealanka":
			vihrealanka.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		#elif b == "kauppalehti":
			#kauppalehti.nouda(add, file(txt, 'w'))
			#print(b + ":\n" + "Kirjoitus onnistui")

		#elif b == "mahorkka":
			#mahorkka.nouda(add, file(txt, 'w'))
			#print(b + ":\n" + "Kirjoitus onnistui")
	
		elif b == "suomenkuvalehti":
			suomenkuvalehti.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "hyvaterveys":
			hyvaterveys.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "ts":
			ts.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")
	
		elif b == "faktabaari":
			faktabaari.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")
	
		elif b == "tiedonantaja":
			tiedonantaja.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "helsinginuutiset":
			helsinginuutiset.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "esaimaa":
			esaimaa.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "kouvolansanomat":
			kouvolansanomat.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "talouselama":
			talouselama.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		elif b == "iltamakasiini":
			iltamakasiini.nouda(add, file(txt, 'w'))
			print(b + ":\n" + "Kirjoitus onnistui")

		else: 
			print("Error sivua ei voitu kirjoittaa tai koodi ei toimi urlin kanssa.")

	elif haku_num == 2:
		print ("Sivut jotka toimii: \n")
		print ("|Aamulehti|     |Ylilauta(kommentteja)|     |Iltasanomat|     |Satakunnankansa|\n|Etelasaimaa|   |Karjalainen|               |Kouvolansanomat| |Talouselama|\n|Iltamakasiini|\n")

		nimi = raw_input('Sivun nimi: ').lower()

		txt = raw_input('Tiedoston nimi(esim yle.txt): ')

		if nimi == "aamulehti":		

			linkki_aamulehti.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")


		elif nimi == "ylilauta":		

			ylilauta.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "iltasanomat":		

			linkki_iltasanomat.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "satakunnankansa":		

			linkki_satakunnankansa.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "etelasaimaa":		

			linkki_esaimaa.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "karjalainen":		

			linkki_karjalainen.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "kouvolansanomat":		

			linkki_kouvolansanomat.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "talouselama":		

			linkki_talouselama.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")

		elif nimi == "iltamakasiini":		

			linkki_iltamakasiini.nouda(file(txt, 'w'))

			print(nimi + ":\n" + "Kirjoitus onnistui")


		else: 
			print("Error linkkei ei voitu kirjoittaa tai koodi ei toimi urlin kanssa.")

	elif haku_num == 0:

		a = True

	else:
		print ("Error")

	
