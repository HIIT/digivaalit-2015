import sys
import os
import re

urlpat = r'((http[s]?):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'

outf = './media/'

def download( link, time ):

    link = link.strip()


    try:

        ## link format: id, url
        out = open( outf + str( hash( link ) ) + '_' + time + '.txt', 'w' )

        ## try to dynamically load the correct script using the domain name
        loader = re.match( urlpat , link ).group('domain')

        loader = structures = __import__( 'sites.' + loader, fromlist = [ loader ] )

        ## load the current story
        loader.nouda( link, out )
        out.close()

    except Exception, e:

        print e

        print "Failed " + link
