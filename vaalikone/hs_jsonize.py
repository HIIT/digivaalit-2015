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

def _reclean( candidate, field, cleaners, invalids ):

    if candidate[ field ]:

        for cleaner in cleaners:
            candidate[ field ] = cleaner.sub( '' , candidate[ field ] )

        for invalid in invalids:
            if invalid in candidate[ field ]:
                candidate[ field ] = None
                return

        if candidate[ field ] == '':
            candidate[ field ] = None


_clean_twitter = re.compile('((http)?[s]?(://)?(www.)?twitter(.com)?/|@)' , re.IGNORECASE )
_clean_facebook = re.compile('(http)?[s]?(://)?(www.)?facebook.com/(pages/)?' , re.IGNORECASE )
_clean_slash = re.compile('/')
_clean_refs = re.compile('\?(f)?ref=[a-z]*')

input = xlrd.open_workbook( sys.argv[1] ).sheets()[0]

data = []

for row in range( 1 , input.nrows ):
    candidate = {}

    for column in range( input.ncols ):
        header = input.cell( 0, column ).value.encode('utf8')

        if not header[0] == 'q':
            candidate[ header ] = _clean( input.cell( row, column ).value, ['', '-', 'NULL'] )

    ## clean urls from data
    _reclean( candidate, 'twitter' , [ _clean_twitter , _clean_slash ], ['www.', 'http'] )
    _reclean( candidate, 'facebook' , [ _clean_facebook , _clean_refs ], ['www.', 'http'] )

    data.append( candidate )

json.dump( data, codecs.open( sys.argv[1] + '.json', 'w' ), ensure_ascii = False)
