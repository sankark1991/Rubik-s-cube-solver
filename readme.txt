These are the files for a Rubik's cube solver program I am building. For now the goal is simply to solve the cube
with no glaring inefficiencies via a corner-edge pair method. In future I may try to increase efficiency by optimizing 
heuristic scores, or I might use this algorithm to generate test data and train a neural net to come up with a more 
efficient solution method. This last possible project seems quite challenging.

%%%%%%%%%%%%%%%%%%%% DESCRIPTION OF SCRIPTS %%%%%%%%%%%%%%%%%%%%%

cubefunctions.py - Defines the class "cubestate", its characteristics (for example, cubestate.F is the front face as a namedtuples), and the associated methods (face turns, whole cube turns, piece-finding, and movelist consolidation).

testmixes.py - Five sample cube mixes, used for testing every new component of this project.

whitecross_2.0.py - A new and improved version of whitecross.py. The function whitecross(cubestate) takes the input cubestate, executes a sequence of turns to correctly place the four edges on the F face, and returns that sequence of moves as a list.

(In progress) F2L_corneredgepair - A script for solving an individual corner edge pair in the F2L stage. Executed four times, this should take a whitecross-ed cube and output a cube with the first two layers solved. I am still fixing major bugs and test-driving this file.

%%%%%%%%%%%%%%%%%%%% OLD OR REDUNDANT FILES %%%%%%%%%%%%%%%%%%%%%

basicturns.py - A cubestate is stored as a list, and this script defines the basic turn functions. This is an implementation 
of the physical task that a human does.

piecefind.py - This script defines the function which finds a specified piece. This is an implementation of the simplest 
level of pattern recognition that a human does.

whitecross.py - Puts the four edges that are meant to be on the front face (the 01, 02, 04, and 05 edges) in their correct 
position and orientation. The cube state should be entered one face at a time, as a simple string of 9 digits taken from
the set {0, 1, 2, 3, 4, 5}.

moveconsolidation.py - A script for consolidating a sequence of moves into a shorter (but equivalent) list. This has since been incorporated into cubefunctions.py.
