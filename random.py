#!/usr/bin/python

import math, re, sys
from io import *
import timeit

cities = readinstance(sys.argv[1])

tour = []
tour.append(9999999999)
citysequence = []
for x in range(len(cities)+1):
    citysequence.append(x)
tour.append(citysequence)
random.shuffle(tour[1])
tourdistance(cities, tour)
print tour

# print "RANDOM"
# shufcities = deepcopy(tour)
# random.shuffle(shufcities[1])
# print "----------"
# print shufcities
