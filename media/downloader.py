import sys
import os
import re

urlpat = r'((http[s]?):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'

outf = './media/'

def download( link, filename ):

    link = link.strip()


    try:
        ## try to dynamically load the correct script using the domain name
        loader = re.match( urlpat , link ).group('domain')

        loader = structures = __import__( 'sites.' + loader, fromlist = [ loader ] )

        ## load the current story

        out = open( outf + filename + '.txt', 'w' )
        loader.nouda( link, out )
        out.close()

    except Exception, e:

        print e

        print "Failed " + link
