
from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import pickle
import time
import sys

picklefile2 = open(sys.argv[1], 'rb')
pickled = pickle.load(picklefile2)
pickled.Best_Simulation("GUI")
exit()