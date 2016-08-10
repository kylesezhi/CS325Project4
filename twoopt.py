#!/usr/bin/python

import math, re, sys
from ioio import *
import timeit

cities = readinstance(sys.argv[1])

startcity = 0

finalanswer = [999999999999, []]

start = timeit.default_timer() # start timer

if len(cities) < 386: # over length of 386 and NN doesnt work fast enough
    for startcity in range(len(cities)): # try nearest neighbor starting at all nodes
        thistour = nearestneighbor(startcity, cities)
        if thistour[0] < finalanswer[0]: finalanswer = deepcopy(thistour)
    stop = timeit.default_timer() # stop timer
else:
	for startcity in range(len(cities)):
		thistour = twoopt(cities, cities)
		if thistour[0] < finalanswer[0]: finalanswer = deepcopy(thistour)

	stop = timeit.default_timer() # stop timer
    
outputtour(finalanswer, sys.argv[1] + ".group3.tour")
