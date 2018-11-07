import sys

class VacuumCleaner:
	"""VacuumCleaner-class
	
	This class manages a cleaner
	"""
	def __init__(self,wsymb,x0,y0,radius=0.5):
		"""The constructor. Inputs the weather symbol, starting coordinates and a optional radius"""
		self._x = x0
		self._y = y0
		self._r = radius
		self._angle = VacuumCleaner.str2angle(wsymb) #rename VacuumCleaner to special keyword
		
	def __str__(self):
		"""DustSucker2000 to string"""
		out = "DustSucker2000<"
		out += str(self._x)+","
		out += str(self._y)+","
		out += self.angle2str()+">"
		return out
		
	def move(self,distance=1):
		"""Moves the cleaner $distance meters forward"""
		if self.angle2str() == 'E':
			self._x += distance
		elif self.angle2str() == 'W':
			self._x -= distance
		elif self.angle2str() == 'N':
			self._y += distance
		elif self.angle2str() == 'S':
			self._y -= distance
		else:
			sys.exit('Error: This angle is not implemented yet.')
	
	def turn(self,delta_angle):
		"""Turns the cleaner $delta_angle degrees, positive or negative"""
		self._angle += delta_angle
		self._angle = self._angle % 360

	def getX(self): 
		return self._x
	
	def getY(self): 
		return self._y
	
	def getRadius(self): 
		return self._r
		
	def getAngle(self): 
		return self._angle
	
	def angle2str(self):
		"""Convert degrees to weather symbol"""
		if self._angle == 0: return 'E'
		elif self._angle == 180: return 'W'
		elif self._angle == 90: return 'N'
		elif self._angle == 270: return 'S'
		else: sys.exit('Error: This angle is not implemented yet.')
		
	@staticmethod
	def str2angle(wsymb):
		"""Convert weather symbol to degrees"""
		if wsymb == 'E': return 0
		elif wsymb == 'W': return 180
		elif wsymb == 'N': return 90
		elif wsymb == 'S': return 270
		else: sys.exit('Error: This weather symbol is not implemented yet.')
		
	
		