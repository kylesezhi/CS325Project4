import matplotlib.pyplot as plt
from ioio import *

cities = readinstance(sys.argv[1])
# print cities

x = []
y = []
for z in cities:
    x.append(z[0])
    y.append(z[1])

color=['m','g','r','b']

plt.scatter(x,y, s=100 ,marker='o', c=color)

plt.show()
