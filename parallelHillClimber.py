
from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import pickle
#import time



class PARALLEL_HILL_CLIMBER:
	def __init__(self, picklename, randseed):
		#os.system("rm brain*.nndf")
		#os.system("rm fitness*.txt")
		self.parents = {}
		self.nextAvailableID = 0
		for a in range(c.populationSize):
				self.parents[a] = SOLUTION(self.nextAvailableID, randseed)
				if randseed != None:
					randseed += 1
				self.nextAvailableID = self.nextAvailableID + 1    

		self.sample = picklename
		self.fitarrays = numpy.zeros((500,10))
		os.system("mkdir pickles/"+picklename)
		self.BestFitness = 0
		
		#print(self.parents)
		#exit()

	def Evolve(self):
		self.Evaluate(self.parents)
		self.Print(0)
		# self.parent.Evaluate("GUI")
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation(currentGeneration)
			print("generation"+ str(currentGeneration))

		self.Show_Best()
		#self.Print()
		exit()

	def Evaluate(self,xyz):
		for parent in xyz:
			xyz[parent].Start_Simulation("DIRECT")
		for parent in self.parents:
			xyz[parent].Wait_For_Simulation_To_End()
			#print(self.parents[parent].fitness)

	def Evolve_For_One_Generation(self,abc):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		self.Print(abc)

		self.Select()

	def Spawn(self):
		self.children = {}
		for parent in self.parents:
			self.children[parent] = copy.deepcopy(self.parents[parent])
			self.children[parent].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1


	def Mutate(self):
		for child in self.children:
			self.children[child].Mutate()

	def Select(self):
		for child in self.children:
			if self.children[child].fitness > self.parents[child].fitness:
				self.parents[child] = self.children[child]

	def Print(self,gennum):
#		#for parent in self.parents:
#			#self.parents[parent].Evaluate("DIRECT")
#			print("\n")
#			print("parent: " + str(self.parents[parent].fitness))
#			print("child " + str(self.children[parent].fitness))
#			print("\n")
		abc = [self.parents[parent].fitness for parent in self.parents]
		self.fitarrays[gennum, :] = abc
		minarg = numpy.argmax(abc)
		if self.parents[minarg].fitness > self.BestFitness:
			self.BestFitness = self.parents[minarg].fitness
			picklefile = open("pickles/" + self.sample+"/" +"generation"+str(gennum), 'wb')
			pickle.dump(self.parents[minarg], picklefile)
			picklefile.close()
		# minarg = numpy.argmax(parentfitness)
		# print()
		
		# fil = open(self.sample + ".txt", "a")
		# fil.write(str(self.parents[minarg].fitness) + " ")
		# fil.close()

	def Show_Best(self):

		print("finalgen")

		parentfitness = [self.parents[parent].fitness for parent in self.parents]
		minarg = numpy.argmax(parentfitness)
		#print(self.parents[minarg].fitness)
		picklefile = open(self.sample, 'wb')
		pickle.dump(self.parents[minarg], picklefile)
		picklefile.close()
		#arrayfilepath = 
		numpy.savetxt(self.sample+"txt", self.fitarrays)
		#time.sleep(5)
		picklefile2 = open(self.sample, 'rb')
		pickled = pickle.load(picklefile2)
		pickled.Best_Simulation("GUI")
		exit()
