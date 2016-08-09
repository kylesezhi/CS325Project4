#!/usr/bin/python

import math, re, sys
from io import *
import timeit

cities = readinstance(sys.argv[1])

tour = []

shufcities = deepcopy(thistour)
random.shuffle(shufcities[1])
print "----------"
print shufcities
twoopt(cities, shufcities)
print shufcities
