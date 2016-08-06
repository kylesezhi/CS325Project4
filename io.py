#!/usr/bin/python

import math, re, sys

# readinstance() and distance() have been taken from the Canvas materials (thx!)

def readinstance(filename):
    # each line of input file represents a city given by three integers:
    # identifier x-coordinate y-coordinate (space separated)
    # city identifiers are always consecutive integers starting with 0
    # (although this is not assumed here explicitly,
    #    it will be a requirement to match up with the solution file)
    f = open(filename,'r')
    line = f.readline()
    cities = []
    while len(line) > 1:
        lineparse = re.findall(r'[^,;\s]+', line)
        cities.append([int(lineparse[1]),int(lineparse[2])])
        line = f.readline()
    f.close()
    return cities

def distance(a,b):
    # a and b are integer pairs (each representing a point in a 2D, integer grid)
    # Euclidean distance rounded to the nearest integer:
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    #return int(math.sqrt(dx*dx + dy*dy)+0.5) # equivalent to the next line
    return int(round(math.sqrt(dx*dx + dy*dy)))

def nearestcity(currentcityidx, cities, tour):
    shortestdist = 9999999999
    index = shortestdist
    for idx,city in enumerate(cities):
        if (city != cities[currentcityidx]) and not (idx in tour):
            d = distance(city, cities[currentcityidx])
            # print "distance from " + str(currentcityidx) + " to " + str(idx) + ": " + str(d)
            if d < shortestdist: 
                shortestdist = d
                index = idx
                
    return index, shortestdist # (index of closest neighbor, the distance to it)


# print readinstance(sys.argv[1])
