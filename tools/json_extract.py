#!/usr/bin/python
# _*_ coding: utf-8

import json
import sys

data = json.load( open( sys.argv[1] , 'r' ) )

index = sys.argv[2]

for field in sys.argv[3].split(','):

    f = open( field + '.txt' , 'w' )

    for entry in data:
        if entry[field]:
            a = entry[index].encode('utf8')
            b = entry[field].encode('utf8')
            f.write( a + ',' + b + '\n' )

    f.close()
