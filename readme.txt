These are the files for a Rubik's cube solver program I am building. For now the goal is simply to solve the cube
with no glaring inefficiencies via a corner-edge pair method. In future I may try to increase efficiency by optimizing 
heuristic scores, or I might use this algorithm to generate test data and train a neural net to come up with a more 
efficient solution method. This last possible project seems quite challenging.

%%%%%%%%%%%%%%%%%%%% NOTATION %%%%%%%%%%%%%%%%%%%%%%

"The six faces of the cube are referred to as F=front, R=right, U=up, B=back, \
L=left, D=down. In algebraic notation, any of these six letters refers to a \
rotation of the corresponding face. For example, R = rotate R clockwise, R' = \
rotate R counterclockwise, and R2 = rotate R 180 degrees."

"There are also full cube re-orientations, given by x, y, and z which correspond \
to rotating the R, U, and F face clockwise without holding the rest of the cube \
constant. Similarly define x', y', z', x2, y2, z2. These won't be necessary but \
they might be useful later for efficiency."

"It will be assumed that the cube state is given as a 6-element list, \
and each of these elements is a 9-element list whose entries are drawn from \
the set {z, x, y, z', x', y'}. These six variables are supposed to represent \
the six colors on whatever cube you're using, and it's assumed that the mapping \
follows a right-handed convention. I'm going to imagine x means right, y means \
up, and z means coming out of the page."

"On my own Rubik's cube, I have x=white, y=red, z=blue, x'=yellow, y'=orange, \
z'=green (up to symmetries by the 24-element group of re-orientations, of course)."

"The order in which the 54 colors are given is very important. Here's going to \
be my convention. The six lists give the colors on the F, R, U, B, L, D faces, \
in that order. The reason for this is that if you sequentially re-orient the cube\
left, down, left, down, left, down then you will see the faces in precisely this\
order and end up back at the F face in the same orientation you started with."

"Within each face, the 9 panels will be given as on a phone dialpad, starting \
in the top left corner and proceeding along each row in turn."

%%%%%%%%%%%%%%%%%%%% DESCRIPTION OF SCRIPTS %%%%%%%%%%%%%%%%%%%%%

basicturns.py - A cubestate is stored as a list, and this script defines the basic turn functions. This is an implementation 
of the physical task that a human does.

piecefind.py - This script defines the function which finds a specified piece. This is an implementation of the simplest 
level of pattern recognition that a human does.

whitecross.py - Puts the four edges that are meant to be on the front face (the 01, 02, 04, and 05 edges) in their correct 
position and orientation. The cube state should be entered one face at a time, as a simple string of 9 digits taken from
the set {0, 1, 2, 3, 4, 5}.