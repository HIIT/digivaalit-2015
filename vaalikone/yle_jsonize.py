# coding: utf8

import csv
import json

import sys

data = []

for row in csv.DictReader( open( sys.argv[1] , 'r' ) , delimiter = ';'  ):

    candidate = {}

    candidate['name'] = row['etunimi'] + ' ' + row['sukunimi']
    candidate['age'] = row['ikä']
    candidate['district'] = row['vaalipiiri']

    if row['sukupuoli']  == 'F':
        candidate['sex'] = 'FEMALE'
    if row['sukupuoli']  == 'M':
        candidate['sex'] = 'MALE'

    candidate['www'] = row['Kotisivun osoite:']
    candidate['facebook'] = row['Facebook-profiilin osoite:']
    candidate['twitter'] = row['Twitter-profiilin osoite:']

    data.append( candidate )

json.dump( data , open( sys.argv[1] + '.json' , 'w' ) )
