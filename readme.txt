These are the files for a Rubik's cube solver program I am building. For now the goal is simply to solve the cube
with no glaring inefficiencies via a corner-edge pair method. In future I may try to increase efficiency by optimizing 
heuristic scores, or I might use this algorithm to generate test data and train a neural net to come up with a more 
efficient solution method. This last possible project seems quite challenging.

This project has given me great respect for the storage capacity of the human mind and the nature of intuition/learning. When I solve the Rubik's cube, I use intuition and instinct, rather than recalling memorized algorithms. I thought I could fairly easily write a cube-solver that mimics my own thought process. After writing over a thousand lines of code (hard-coding in cases) I've produced a cube solver that is FAR less move-efficient than I am myself. I now believe that my own self-perceived "intuition" can only be the result of several hundreds of (unconsciously) memorized configurations, which can only be achieved through thousands or tens of thousands of practice solves.

It suddenly makes sense to me why people are turning to learning algorithms, i.e. neural nets.

%%%%%%%%%%%%%%%%%%%% DESCRIPTION OF SCRIPTS %%%%%%%%%%%%%%%%%%%%%

cubefunctions.py - Defines the class "cubestate", its characteristics (for example, cubestate.F is the front face as a namedtuples), and the associated methods (face turns, whole cube turns, piece-finding, movelist consolidation, the PLL algorithms, and a method which executes a given list of turns).

whitecross_2.0.py - A new and improved version of whitecross.py. The function whitecross(cubestate) takes the input cubestate, executes a sequence of turns to correctly place the four edges on the F face, and stores those moves in the list cubestate.moves.

F2L_corneredgepair.py - A script for solving an individual corner edge pair in the F2L stage. There's a basic function "F2L_ce_pair()" which solves the corner-edge pair in the FRD position. Then the function "F2L()", which takes an input cubestate with the white cross on the D face, solves the F2L on that cube and stores the sequence of moves in the list cubestate.moves.

lastlayer.py - A script for solving the OLL step and PLL step, i.e. solving the entire last layer of the cube.

testmixgenerator.py - I got tired of manually generated test cases. So I wrote a script which generates 100 random testmixes and then writes the code to test those testmixes and puts it in a file called random_mixes.txt.

testsuite.py - This is the file where I'm pasting in the code from random_mixes.txt, along with some preamble (the code should be pasted after the ##### part). After the latest round of debugging I've tested about 500 random mixes and with a 100% success rate.

%%%%%%%%%%%%%%%%%%%% OLD OR REDUNDANT FILES %%%%%%%%%%%%%%%%%%%%%

basicturns.py - A cubestate is stored as a list, and this script defines the basic turn functions. This is an implementation 
of the physical task that a human does.

piecefind.py - This script defines the function which finds a specified piece. This is an implementation of the simplest 
level of pattern recognition that a human does.

whitecross.py - Puts the four edges that are meant to be on the front face (the 01, 02, 04, and 05 edges) in their correct 
position and orientation. The cube state should be entered one face at a time, as a simple string of 9 digits taken from
the set {0, 1, 2, 3, 4, 5}.

moveconsolidation.py - A script for consolidating a sequence of moves into a shorter (but equivalent) list. This has since been incorporated into cubefunctions.py.

testmixes.py - Defines a function to solve a test cube, as well as a function which tests whether a given cube is solved or not. Fifteen sample cube mixes, and runs the full solve algorithm on all of them. As of now the algorithm successfully solves all fifteen samples, though I will run more tests to catch any other bugs.
