# coding: utf8

import csv
import json

import re

import sys

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


data = []

for row in csv.DictReader( open( sys.argv[1] , 'r' ) , delimiter = ';'  ):

    candidate = {}

    candidate['name'] = row['etunimi'] + ' ' + row['sukunimi']
    candidate['age'] = row['ikä']
    candidate['district'] = row['vaalipiiri']
    candidate['number'] = row['ehdokasnumero']

    if row['sukupuoli']  == 'F':
        candidate['sex'] = 'FEMALE'
    if row['sukupuoli']  == 'M':
        candidate['sex'] = 'MALE'

    candidate['www'] = row['Kotisivun osoite:']
    candidate['facebook'] = row['Facebook-profiilin osoite:']
    candidate['twitter'] = row['Twitter-profiilin osoite:']


    _reclean( candidate, 'twitter' , [ _clean_twitter , _clean_slash ], ['www.', 'http'] )

    data.append( candidate )

json.dump( data , open( sys.argv[1] + '.json' , 'w' ) )
