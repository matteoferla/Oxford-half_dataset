#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """

NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import csv, os, re
from collections import defaultdict

# Place Overall, Place Gender, Place Category, Name , BIB, Category, HALF, Finish time,
#2,2,2,"Mutai, Emmanuel (KEN)",7,18-39,01:03:06,02:06:23,


db=dict()

#Rank	Name	BIB	Club or Crew	Age	Gender	Pace / Km	Chip Time
#497	GEOFF CUMBER	6082	Halifax Harriers & AC	70	M	04:22	01:31:54


stats=defaultdict(int,[('doublerunners17',0),('unique17',0)])
with open('Ox2017-redux.csv') as fh:
    for arrival in csv.DictReader(fh):
        if arrival['Name']:  # no nameless folk
            name=arrival['Name'].title()
            if name in db:
                print('Doublerunner {}'.format(name))
                stats['doublerunners17']+=1
                db[name] = {}
            else:
                db[name]={'Name': name, 'Age2017': arrival['Age'], 'Gender':arrival['Gender'],'Time2017':arrival['Time']}

for name in list(db.keys()):
    if not db[name]:
        del db[name]
    else:
        stats['unique17']+=1

stats['unique']=stats['unique17']

for year in ['2012','2013','2014','2015','2016']:
    with open('Ox-{}.csv'.format(year)) as fh:
        for arrival in csv.DictReader(fh):
            if arrival['Name']:
                name=arrival['Name'].title()
                if name in db:
                    if not 'Time' + year in db[name]:
                        db[name]['Time' + year] = arrival['Time']
                    else:
                        del db[name]
                        stats['doublerunners'+year] +=1
                        stats['unique']-=1

print(stats)
with open('oxford-redux.csv', 'w') as fh:
    k=list(stats.keys())
    fh.write(','.join(k)+'\n')
    fh.write(','.join([str(stats[ki]) for ki in k])+'\n\n')
    #'Name': name, 'Age2017': arrival['Age'], 'Gender':arrival['Gender'],'Time17':arrival['Time'
    w = csv.DictWriter(fh, 'Name,Age2017,Gender,Time2017,Time2016,Time2015,Time2014,Time2013,Time2012,'.split(
        ','))
    w.writeheader()
    w.writerows(db.values())

