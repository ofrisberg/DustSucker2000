import inputparser,simulator,vacuumcleaner

def main():
	"""The runnable program"""
	
	print("DustSucker2000 Simulator by Olle Frisberg")
	print("")
	
	print("This software aims to simulate how our new vacuum cleaner moves.")
	print("Input format:")
	print("Line 0: <Lx> <Ly> (The dimensions of the room")
	print("Line 1: <wsymb> <x> <y> (The initial direction and coordinates of the DustSucker2000")
	print("Line 2: <commands> (The commands to execute in serial)")
	print("Supported commands:")
	print("A: Move forward 1 meter")
	print("L: Turn left 90 degrees")
	print("R: Turn right 90 degrees")
	print("")
	
	# Parse the input
	ip = inputparser.InputParser()
	Lx,Ly,wsymb,x,y,commands = ip.getParsed()
	
	# Create the cleaner object
	vc = vacuumcleaner.VacuumCleaner(wsymb,x,y)
	
	# Uncomment this to show parsed input
	#print(Lx,Ly,vc.getAngle(),x,y,commands)
	
	
	sim = simulator.Simulator(Lx,Ly,vc) # Create a simulator object
	sim.start(commands) # Start simulation
	res = sim.getResult() # Get simulation result
	
	print("Result: "+res)
	

if __name__ == '__main__':
	main()