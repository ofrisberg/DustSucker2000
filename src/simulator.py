import sys

class Simulator:
	"""Simulator-class
	
	This class manages the simulation and the room.
	To do: Move the room-part to a different class.
	"""
	def __init__(self,Lx,Ly,vacuumCleaner):
		"""The constructor. Inputs the room dimensions and a VacuumCleaner-object"""
		self._vc = vacuumCleaner
		if Lx < 0 or Ly < 0:
			sys.exit('Error: Lx and Ly must be positive')
		self._setBorders(Lx,Ly)
		
		
	def _setBorders(self,Lx,Ly):
		"""Setting the borders of the room.
		The negative radius is to fix the miss alignment between
		the coordinate systems of the cleaner and the room """
		self._west = -self._vc.getRadius()
		self._east = Lx-self._vc.getRadius()
		self._south = 0-self._vc.getRadius()
		self._north = Ly-self._vc.getRadius()
		
	def start(self,commands):
		"""Start the simulation. Inputs a string of command-characters."""
		self._checkCollisions()
		for cmd in commands:
			self._execute(cmd)
			
	def getResult(self):
		"""Get result of the simulation.
		To do: Move this method to the VacuumCleaner-class."""
		res = self._vc.angle2str() + " "
		res += str(self._vc.getX()) + " "
		res += str(self._vc.getY())
		return res
			
	def _execute(self,cmd):
		if cmd == 'A':
			self._vc.move()
			self._checkCollisions()
		elif cmd == 'L':
			self._vc.turn(90)
		elif cmd == 'R':
			self._vc.turn(-90)
		else:
			sys.exit("Error: Couldn't recognize command '"+cmd+"'")
		
	def _checkCollisions(self):
		r = self._vc.getRadius()
		x = self._vc.getX()
		y = self._vc.getY()
		if self._west >  x - r:
			self._onCollision('west')
		elif self._east <  x + r:
			self._onCollision('east')
		elif self._south >  y - r:
			self._onCollision('south')
		elif self._north <  y + r:
			self._onCollision('north')
		
	def _onCollision(self,wall):
		sys.exit("Error: The "+str(self._vc)+" has crashed into the "+wall+" wall")