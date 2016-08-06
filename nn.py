#!/usr/bin/python

import math, re, sys
from io import readinstance, distance, nearestcity
import timeit

# SPEED DATA
# 3 nodes takes 0.0001220703125 seconds
# 76 nodes takes 0.454488039017 seconds
# 280 nodes takes 53.8123698235 seconds

cities = readinstance(sys.argv[1])

tour = []
startcity = 0
tour.append(startcity)
totaldistance = 0
currentcityidx = startcity

finalanswer = 999999999999

start = timeit.default_timer() # start timer

for x in range(len(cities)): # try nearest neighbor starting at all nodes
    tour = []
    startcity = x
    tour.append(startcity)
    totaldistance = 0
    currentcityidx = startcity
    
    while len(tour) < len(cities):
        n = nearestcity(currentcityidx, cities, tour)
        tour.append(n[0])
        currentcityidx = n[0]
        totaldistance += n[1]

    # add final distance to return to your starting point
    totaldistance += distance(cities[tour[-1]], cities[startcity])

    print totaldistance
    # print tour
    if totaldistance < finalanswer: finalanswer = totaldistance

stop = timeit.default_timer() # stop timer
print "FINAL: " + str(finalanswer)
print str(len(cities)) + " nodes takes " + str(stop - start) + " seconds"
