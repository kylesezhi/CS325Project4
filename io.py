#!/usr/bin/python

import math, re, sys, random

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

def nearestneighbor(startcity, cities):
    tour = []
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
    
    r = []
    r.append(totaldistance)
    r.append(tour)
    return r

def outputtour(tour, filename):
    text_file = open(filename, "w")
    text_file.write(str(tour[0]) + '\n')
    for node in tour[1]:
        text_file.write(str(node) + '\n')
    text_file.close()
    
# def tourdistance(tour, cities): # update the first element in tour with distance
#     tour[0] = 0
#     for node in tour[1]:
        
    
# def twoopt(cities, tour):
#     for range(10):
#         #Choose 2 random cities
#         city1 = random.randint(0,len([1,2,3])-1)
#         city2 = 
