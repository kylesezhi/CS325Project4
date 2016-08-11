#!/usr/bin/python

import math, re, sys
from ioio import *
import timeit

cities = readinstance(sys.argv[1])

tour = []
tour.append(9999999999)
citysequence = []
for x in range(len(cities)):
    citysequence.append(x)
tour.append(citysequence)
random.shuffle(tour[1])
tourdistance(tour, cities)
print tour

# tour2 = twooptswap(tour, 3, 5)
# tourdistance(tour2, cities)
# print tour2

twoopt(cities, tour)
print tour

# outputtour(tour, sys.argv[1] + ".group3.tour")
