#!/usr/bin/python

import math, re, sys
from io import readinstance, distance, nearestneighbor
import timeit

# SPEED DATA for EXHAUSTIVE NEAREST NEIGHBOR
# 3 nodes takes 0.0001220703125 seconds
# 76 nodes takes 0.454488039017 seconds
# 280 nodes takes 53.8123698235 seconds
# 386 nodes takes 176.600210905 seconds
# 443 nodes takes 299.670012951 seconds

cities = readinstance(sys.argv[1])

tour = []
startcity = 0
tour.append(startcity)
totaldistance = 0
currentcityidx = startcity

finalanswer = 999999999999

start = timeit.default_timer() # start timer

for startcity in range(len(cities)): # try nearest neighbor starting at all nodes
    thistour = nearestneighbor(startcity, cities)
    if thistour[0] < finalanswer: finalanswer = thistour[0]

stop = timeit.default_timer() # stop timer
print "FINAL: " + str(finalanswer)
print str(len(cities)) + " nodes takes " + str(stop - start) + " seconds"
