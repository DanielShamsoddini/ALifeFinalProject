import numpy
import matplotlib.pyplot
import os

#print(os.listdir())
xyz = []
currentplot = "HYPMultConnected"

for a in os.listdir():
    if "Seedtxt" in a:
        xyz.append(a)

print(xyz)
indexx = 0
targetvalues = [0] * len(xyz)
for b in xyz:
    targetvalues[indexx] = numpy.loadtxt(b)
    targetvalues[indexx] = numpy.amax(targetvalues[indexx], axis = 1)
    matplotlib.pyplot.plot(targetvalues[indexx], linewidth = 2, label = b)
    indexx += 1
# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# print(backLegSensorValues)
# matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = "frontleg")
# matplotlib.pyplot.plot(frontLegSensorValues, label = "backleg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()