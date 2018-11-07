# DustSucker2000 Simulator
This software aims to simulate how our new vacuum cleaner moves.

## Dependencies
Only tested in Cygwin with Python 3 on Windows 
(but should be platform independent).

## Usage
All lengths are measured in meters and the angle is defined as
in the unit circle (i.e. 0 degrees is east, 90 degrees is north etc).

### Input format
- Line 0: Lx Ly (The dimensions of the room
- Line 1: wsymb x y (The initial conditions of the DustSucker2000
- Line 2: commands (The commands to execute in serial)

### Supported commands
- A: Move forward 1 meter
- L: Turn left 90 degrees
- R: Turn right 90 degrees

## Example
### Input
- Line 0: 6 7
- Line 1: N 3 2
- Line 2: RARAARARA

### Terminal command
`cat test.txt | python src/main.py`

### Result
Creates a room with a width of 6 m and height of 7 m. 
The original position of the cleaner is at 3 m from left
and 2 m from bottom corner that the cleaner can fit in.
Resulting position: N 3 1.

## To do
Due to time limitation there is still some work to do on the simulator:
- Implement exceptions for all classes
- Implement automated unit testing
- Implement a vector class that handles the cleaner position and direction
- Implement logging for info, debugging and warnings
- Implement building-script that creates a runnable executable.
- Fix documentation for non-documented methods and also add javadoc or doxygen-syntax