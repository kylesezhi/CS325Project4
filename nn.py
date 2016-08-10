#!/usr/bin/python

import math, re, sys
from ioio import *
import timeit

# SPEED DATA for EXHAUSTIVE NEAREST NEIGHBOR
# 3 nodes takes 0.0001220703125 seconds
# 76 nodes takes 0.454488039017 seconds
# 280 nodes takes 53.8123698235 seconds
# 386 nodes takes 176.600210905 seconds <---- SWEET SPOT
# 443 nodes takes 299.670012951 seconds

cities = readinstance(sys.argv[1])

startcity = 0

finalanswer = [999999999999, []]

start = timeit.default_timer() # start timer

if len(cities) < 386: # over length of 386 and NN doesnt work fast enough
    for startcity in range(len(cities)): # try nearest neighbor starting at all nodes
        thistour = nearestneighbor(startcity, cities)
        if thistour[0] < finalanswer[0]: finalanswer = deepcopy(thistour)

    stop = timeit.default_timer() # stop timer
    
outputtour(finalanswer, sys.argv[1] + ".group3.tour")
# print str(len(cities)) + " nodes takes " + str(stop - start) + " seconds"
