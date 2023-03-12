import pybullet as p
import os

class WORLD:
	def __init__(self,worldnum):
		p.loadSDF("world"+worldnum+".sdf")
		self.planeId = p.loadURDF("plane.urdf")
		os.system("rm " + "world"+worldnum+".sdf")
