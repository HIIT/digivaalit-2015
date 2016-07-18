# coding: utf-8

import os
import sys
import re
import subprocess

def lemmatize( text ):

    text = text.decode('utf8')
    text = re.sub( ' +',' ', text )
    text = re.sub( u'[^a-zA-ZöäåÖÄÅ]' , ' ' , text )
    text = re.sub( ' +',' ', text )
    text = text.replace('"', '' ) ## no "

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

    fo = open( path + '.lemma', 'w' )
    fo.write( lemma )
    fo.close()

## read every file in folder and fix based on that
def folder( path ):

    for f in os.listdir( path ):

        print path + '/' + f

        file( path + '/' + f )


def serial( path , index ):

   files = os.listdir( path )

   files = filter( lambda x: '.lemma' not in x, files )

   files = map( int , files )

   files = filter( lambda x: x % 200 == index , files )

   files = map( str , files )

   for f in files:
       file( path + '/' + f )

if __name__ == '__main__':

    if sys.argv[1] == 'serial': ## conduct serial lemma

        for path in sys.argv[3:]:

           serial( path , int( sys.argv[2] ) )

    ## take as many parameters as needed
    for item in sys.argv[1:]:

        if( os.path.isdir( item ) ):

            folder( item )

        else:

            file( item )
