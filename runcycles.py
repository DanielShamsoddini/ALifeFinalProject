import os
import random

randlist = [random.randint(0,((2**25)-1)) for a in range(7)]

for a in randlist:
    os.system("python3 runsnakemake.py" + " HYPOneConnected"+str(a)+"Seed" + " " + str(a) )