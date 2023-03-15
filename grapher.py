import numpy
import matplotlib.pyplot as plt
import os
import statistics
import math

#print(os.listdir())
xyz = []
currentplot = "HYPMultConnected"

for a in os.listdir():
    if "Seedtxt" in a:
        xyz.append(a)

print(xyz)
indexx = 0
targetvalues = {}
for b in xyz:
    targetvalues[b] = numpy.loadtxt(b)
    targetvalues[b] = numpy.amax(targetvalues[b], axis = 1)
    plt.plot(targetvalues[b], linewidth = 2, label = b)
    indexx += 1

plt.title("All Simulations")
plt.legend()
plt.show()