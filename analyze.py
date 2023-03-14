import numpy
import matplotlib.pyplot
targetvalues = numpy.loadtxt("ControlAllConnected345591549Seedtxt")
targetvalues = numpy.amax(targetvalues, axis = 1)
matplotlib.pyplot.plot(targetvalues, linewidth = 2, label = "Backleg")
# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# print(backLegSensorValues)
# matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = "frontleg")
# matplotlib.pyplot.plot(frontLegSensorValues, label = "backleg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()