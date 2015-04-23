import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

    ## ylex seems to be JS single page application; this approach can't handle it. just return here

    return

if __name__ == '__main__':

	nouda("http://yle.fi/ylex/uutiset/ylexaan_tulossa_politiikan_superviikot__myos_sina_voit_tentata_paattajia_ennen_vaaleja/3-7875448", file('yle.txt', 'w'))
