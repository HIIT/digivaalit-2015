import os
import sys
import re
import subprocess

def lemmatize( text ):

    text = text.encode('utf8')
    text = re.sub( '[\.,?!:;]' , '' , text )

    out = subprocess.check_output( 'module load finnish-process; echo "' + text + '" | finnish-process', shell = True)

    lemma = ''
    for line in out.split('\n'):
        line = line.strip()
        line = line.split('\t')

        if len( line ) >= 2:
            lemma += line[1] + ' '

    return lemma

## read a file and lemmatize it
def file( path ):

    text = open( path )
    text = text.readlines()
    text = map( lambda x: x.strip(), text )
    text = ' '.join( text )

    lemma = lemmatize( text )

    fo = open( path + file + '.lemma', 'w' )
    fo.write( lemma )
    fo.close()

## read every file in folder and fix based on that
def folder( path ):

    for file in os.listdir( path ):

        file( path + file )

if '__name__' == '__main__':

    ## take as many parameters as needed
    for item in sys.argv[1:]:

        if( os.path.isdir( item ) ):

            folder( item )

        else:

            file( item )
