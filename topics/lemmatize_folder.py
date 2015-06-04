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

## folder usecase
path = sys.argv[1]
for file in os.listdir( path ):

    text = open( path + file )
    text = text.readlines()
    text = map( lambda x: x.strip(), text )
    text = ' '.join( text )

    lemma = lemmatize( text )

    fo = open( path + file + '.lemma', 'w' )
    fo.write( lemma )
    fo.close()
