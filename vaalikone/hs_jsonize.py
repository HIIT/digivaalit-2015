 #!/usr/bin/python
# _*_ coding: utf-8

import xlrd
import json
import sys
import codecs
import re

def _clean( value , empty):
    try:
        return int( value )
    except:
        value = value.encode('utf-8')
        if value in empty:
            return None
        return value

_clean_twitter = re.compile('((http)?[s]?(://)?(www.)?twitter(.com)?/|@)' , re.IGNORECASE )
_clean_slash = re.compile('/')

input = xlrd.open_workbook( sys.argv[1] ).sheets()[0]

data = []

for row in range( 1 , input.nrows ):
    candidate = {}

    for column in range( input.ncols ):
        header = input.cell( 0, column ).value.encode('utf8')

        if not header[0] == 'q':
            candidate[ header ] = _clean( input.cell( row, column ).value, ['', '-', 'NULL'] )

    ## clean urls from data
    if candidate[ 'twitter' ]:
        candidate[ 'twitter' ] = _clean_twitter.sub( '', candidate[ 'twitter' ] )
        candidate[ 'twitter' ] = _clean_slash.sub( '', candidate['twitter'] )

        ## urgh urgh
        if candidate[ 'twitter' ] == '' or 'http' in candidate['twitter'] or 'www.' in candidate['twitter']:
            candidate[ 'twitter' ] = None

    data.append( candidate )

json.dump( data, codecs.open( sys.argv[1] + '.json', 'w' ), ensure_ascii = False)
