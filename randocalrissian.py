#!/usr/bin/python

import math, re, sys
from io import *
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

outputtour(tour, sys.argv[1] + ".group3.tour")
