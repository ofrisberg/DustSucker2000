import sys
		
class InputParser:
	"""InputParser-class
	
	This class parses the standard input according to the desired format.
	"""
	def __init__(self):
		self._lines = []
		for line in sys.stdin.readlines():
			self._lines.append(line.rstrip("\n"))
		
		if len(self._lines) != 3:
			sys.exit("Error: Expected three lines of input")

	def getParsed(self):
		"""Get the parsed input parameters (Lx,Ly,x,y,commands)"""
		Lx, Ly = self._parseRoomDimensions()
		wsymb, x, y = self._parseInitialConditions()
		commands = self._lines[2]
		return (Lx,Ly,wsymb,x,y,commands)
		
		
	def _parseRoomDimensions(self):
		line = self._lines[0]
		nrs = line.split(' ')
		if len(nrs) != 2:
			sys.exit("Error: Expected two integers on line 0")
		return (self._parseInt(nrs[0]),self._parseInt(nrs[1]))
		
	def _parseInitialConditions(self):
		line = self._lines[1]
		nrs = line.split(' ')
		if len(nrs) != 3:
			sys.exit("Error: Expected wsymb and two integers on line 1")
		return (nrs[0],self._parseInt(nrs[1]),self._parseInt(nrs[2]))
			
			
			
	def _parseInt(self,nr):
		try:
			return int(nr)
		except ValueError:
			sys.exit('Error: '+nr+' is not a number')