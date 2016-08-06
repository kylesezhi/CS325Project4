#!/usr/bin/python

import math, re, sys
from io import readinstance, distance, nearestcity

cities = readinstance(sys.argv[1])

tour = []
startcity = 0
tour.append(startcity)
totaldistance = 0
currentcityidx = startcity

finalanswer = 999999999999

for x in range(len(cities)):
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

    # add final distance
    totaldistance += distance(cities[tour[-1]], cities[startcity])

    print totaldistance
    # print tour
    if totaldistance < finalanswer: finalanswer = totaldistance


print "FINAL: " + str(finalanswer)
