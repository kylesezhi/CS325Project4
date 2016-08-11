#!/usr/bin/python

import math, re, sys
from ioio import *
import timeit

start = timeit.default_timer() # start timer

MAXTIME = 175 # max 3 min = 180 s, so to be safe 175

cities = readinstance(sys.argv[1])

finalanswer = [999999999999, []]

if len(cities) < 386: # over length of 386 and NN doesnt work fast enough
    for startcity in range(len(cities)): # try nearest neighbor starting at all nodes
        thistour = nearestneighbor(startcity, cities)
        if thistour[0] < finalanswer[0]: finalanswer = deepcopy(thistour)
    stop = timeit.default_timer() # stop timer
else:
    # random tour
    tour = []
    tour.append(9999999999)
    citysequence = []
    for x in range(len(cities)):
        citysequence.append(x)
    tour.append(citysequence)
    random.shuffle(tour[1])
    tourdistance(tour, cities)
    
    # 2 OPT
    size = len(cities)
    for i in range(0,size-1):
        if ((timeit.default_timer() - start) > MAXTIME): break
        for j in range(i+1,size):
            if ((timeit.default_timer() - start) > MAXTIME): break
            tour2 = twooptswap(tour, i, j)
            tourdistance(tour2, cities) # update tourlength
            #print "tour: " + str(tour[0]) + " tour2: " + str(tour2[0])
            if tour[0] > tour2[0]: 
                #print "OPTIMIZE FOUND"
                tour = deepcopy(tour2)
    stop = timeit.default_timer()
    finalanswer = tour
print (stop - start)
outputtour(finalanswer, sys.argv[1] + ".group3.tour")
