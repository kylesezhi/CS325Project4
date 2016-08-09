#!/usr/bin/python

import math, re, sys, random
from copy import deepcopy

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
    currentcityidx = startcity
    
    while len(tour) < len(cities):
        n = nearestcity(currentcityidx, cities, tour)
        tour.append(n[0])
        currentcityidx = n[0]

    r = []
    r.append(0)
    r.append(tour)
    
    tourdistance(r, cities)
    print r
    
    return r

def outputtour(tour, filename):
    text_file = open(filename, "w")
    text_file.write(str(tour[0]) + '\n')
    for node in tour[1]:
        text_file.write(str(node) + '\n')
    text_file.close()

# tourdistance()
# takes a list with the first element as the (old) distance and the second element
# is the tour, for example:
# [12499, [3, 1, 0, 2]]
# and update the first number (in the above example, 12499) = the distance, based 
# on the coordinates in the cities array
def tourdistance(tour, cities): # update the first element in tour with distance
    tour[0] = 0
    for idx in range(len(tour[1])-1):
        # print len(tour[1])
        # print len(cities)
        tour[0] += distance(cities[tour[1][idx]],cities[tour[1][idx+1]])
        # print str(tour[1][idx]) + " to " + str(tour[1][idx+1]) + " is " + str(distance(cities[idx],cities[idx+1]))
    tour[0] += distance(cities[tour[1][-1]],cities[tour[1][0]])
    # print str(tour[1][-1]) + " to " + str(tour[1][0]) + " is " + str(distance(cities[idx],cities[idx+1]))
    
# def randomswap(cities, tour):
#     optimized = False
#     while optimized == False:
#         tour2 = deepcopy(tour) #COPIES list; does not point to it
#         # Choose 2 random cities
#         city1 = random.randint(0,len(cities)-1)
#         city2 = (city1 + random.randint(0, len(cities)-2)) % len(cities)
#         # print "random1: " + str(city1) + " random2: " + str(city2)
#         # print str(tour)
#         # print "index1: " + str(tour[1].index(city1)) + " index2: " + str(tour[1].index(city2))
#         # Swap edges and get distances
#         a, b = tour[1].index(city1), tour[1].index(city2)
#         tour2[1][b], tour2[1][a] = tour[1][a], tour[1][b]
#         tourdistance(tour2, cities)
#         print "tour: " + str(tour[0]) + " tour2: " + str(tour2[0])
#         if tour[0] > tour2[0]:
#             print "OPTIMIZE"
#             optimized = True
#             tour = deepcopy(tour2)
    
# http://www.technical-recipes.com/2012/applying-c-implementations-of-2-opt-to-travelling-salesman-problems/        
def twoopt(cities, tour):
    size = len(cities)
    improve = 0
    while (improve < 20): #FIXME change to 20
        for i in range(0,size-1):
            for j in range(i+1,size):
                tour2 = deepcopy(tour) #COPIES list; does not point to it (default = points to it)
                twooptswap(tour2, i, j)
                tourdistance(tour2, cities) # update tourlength
                # print tour
                # print "----------"
                # print tour2
                print "tour: " + str(tour[0]) + " tour2: " + str(tour2[0])
                if tour[0] > tour2[0]: 
                    print "OPTIMIZE FOUND"
                    improve = 0
                    tour = deepcopy(tour2)
        improve += 1

def twooptswap(tour, i, k):
    newtour = deepcopy(tour)
    for x in range(len(newtour[1])):
        newtour[1][x] = -1
    # add tour[0] to tour[i-1] IN ORDER to the newtour
    for x in range(i):
        newtour[1][x] = tour[1][x]
    # add tour[i] to tour[k] IN REVERSE ORDER to the newtour
    r = tour[1][i:k+1]
    r.reverse()
    for idx,x in enumerate(range(i,k+1)):
        newtour[1][x] = r[idx]
    # add tour[k+1] to the end IN ORDER to the newtour
    for x in range(k+1,len(tour[1])):
        newtour[1][x] = tour[1][x]
    tour = newtour
    print tour
    print newtour


def twoopt2(cities, tour):
    size = len(tour)
    improve = 0
    tour2 = deepcopy(tour)
    while improve < 20:
        best_distance = tourdistance(tour, cities)
        for i in range(0,size - 1):
            for x in range((i+1), size):
                twooptswap(tour2, i, x)
                newdistance = tourdistance(tour2, cities)
                if newdistance < best_distance:
                    improve = 0
                    tour = tour2
                    best_distance = newdistance
                    print best_distance
        improve += 1
