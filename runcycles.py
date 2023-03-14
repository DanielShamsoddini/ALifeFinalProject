import os
import random

randlist = [random.randint(0,((2**30)-1)) for a in range(7)]

for a in randlist:
    os.system("python3 runsnakemake.py" + " ControlOneConnected"+str(a)+"Seed" + " " + str(a) )