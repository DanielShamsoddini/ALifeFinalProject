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
    #matplotlib.pyplot.plot(targetvalues[indexx], linewidth = 2, label = b)
    indexx += 1
# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# print(backLegSensorValues)
# matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = "frontleg")
# matplotlib.pyplot.plot(frontLegSensorValues, label = "backleg")



def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25):
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    confidence_interval = z * stdev / math.sqrt(len(values))

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, 'o', color='#f44336')

    return mean, confidence_interval

print(targetvalues.keys)
x1 = []
x2 = []
x3 = []
x4 = []
for a in targetvalues.keys():
    if "ControlAll" in a:
        x1.append(numpy.max(targetvalues[a]))
    elif "ControlOne" in a:
        x2.append(numpy.max(targetvalues[a]))
    elif "HYPOne" in a:
        x3.append(numpy.max(targetvalues[a]))
    else:
        x4.append(numpy.max(targetvalues[a]))
        

plt.xticks([1, 2, 3, 4], ['ControlAll', 'ControlOne', 'HYPOne', 'HYPAll'])
plt.title('Confidence Interval')
plot_confidence_interval(1, numpy.array(x1))
plot_confidence_interval(2, numpy.array(x2))
plot_confidence_interval(3, numpy.array(x3))
plot_confidence_interval(4, numpy.array(x4))
plt.show()


#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()