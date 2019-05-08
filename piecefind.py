# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 08:25:04 2019

@author: sanka
"""

"The first thing you need to do is to be able to recognize and find edge and \
corner pieces, then move them to where you want them."

"For a given position of the cube, there are 12 edges. They'll be designated \
for example: F1U3 is the edge consisting of the F1 and U3 panels. This edge \
can also be named U3F1. I won't build a function which, given such an edge \
position, tells you which colors are on that edge because that's basically just \
querying our list (in the case of F1U3, it'd be [cube[0][1],cube[2][3]])."

"Just as you'd expect, the same convention is used for the 8 corners. For example, \
F2R0U6."


"Function edgefind: given a particular pair of edge colors, find it on the cube\
and return that location with orientation specified."

def edgefind(cubestate, x, y):
    if cubestate[0][5] == x and cubestate[1][3] == y:
        return [0, 1]
    if cubestate[0][1] == x and cubestate[2][3] == y:
        return [0, 2]
    if cubestate[0][3] == x and cubestate[4][1] == y:
        return [0, 4]
    if cubestate[0][7] == x and cubestate[5][1] == y:
        return [0, 5]
    if cubestate[1][1] == x and cubestate[2][7] == y:
        return [1, 2]
    if cubestate[1][7] == x and cubestate[5][5] == y:
        return [1, 5]
    if cubestate[4][3] == x and cubestate[2][1] == y:
        return [4, 2]
    if cubestate[4][5] == x and cubestate[5][3] == y:
        return [4, 5]
    if cubestate[3][1] == x and cubestate[4][7] == y:
        return [3, 4]
    if cubestate[3][3] == x and cubestate[2][5] == y:
        return [3, 2]
    if cubestate[3][5] == x and cubestate[5][7] == y:
        return [3, 5]
    if cubestate[3][7] == x and cubestate[1][5] == y:
        return [3, 1]
    
    if cubestate[0][5] == y and cubestate[1][3] == x:
        return [1, 0]
    if cubestate[0][1] == y and cubestate[2][3] == x:
        return [2, 0]
    if cubestate[0][3] == y and cubestate[4][1] == x:
        return [4, 0]
    if cubestate[0][7] == y and cubestate[5][1] == x:
        return [5, 0]
    if cubestate[1][1] == y and cubestate[2][7] == x:
        return [2, 1]
    if cubestate[1][7] == y and cubestate[5][5] == x:
        return [5, 1]
    if cubestate[4][3] == y and cubestate[2][1] == x:
        return [2, 4]
    if cubestate[4][5] == y and cubestate[5][3] == x:
        return [5, 4]
    if cubestate[3][1] == y and cubestate[4][7] == x:
        return [4, 3]
    if cubestate[3][3] == y and cubestate[2][5] == x:
        return [2, 3]
    if cubestate[3][5] == y and cubestate[5][7] == x:
        return [5, 3]
    if cubestate[3][7] == y and cubestate[1][5] == x:
        return [1, 3]
    
"Do the same thing for corners. It will be assumed that the colors x, y, z are\
given in a counterclockwise (right-handed) order."    

def cornerfind(cubestate, x, y, z):
    if cubestate[0][2] == x and cubestate[1][0] == y and cubestate[2][6] == z:
        return [0, 1, 2]
    if cubestate[0][2] == y and cubestate[1][0] == z and cubestate[2][6] == x:
        return [2, 0, 1]
    if cubestate[0][2] == z and cubestate[1][0] == x and cubestate[2][6] == y:
        return [1, 2, 0]
    
    if cubestate[2][2] == x and cubestate[3][0] == y and cubestate[4][6] == z:
        return [2, 3, 4]
    if cubestate[2][2] == y and cubestate[3][0] == z and cubestate[4][6] == x:
        return [3, 4, 2]
    if cubestate[2][2] == z and cubestate[3][0] == x and cubestate[4][6] == y:
        return [4, 2, 3]
    
    if cubestate[4][2] == x and cubestate[5][0] == y and cubestate[0][6] == z:
        return [4, 5, 0]
    if cubestate[4][2] == y and cubestate[5][0] == z and cubestate[0][6] == x:
        return [5, 0, 4]
    if cubestate[4][2] == z and cubestate[5][0] == x and cubestate[0][6] == y:
        return [0, 4, 5]
    
    if cubestate[1][2] == x and cubestate[2][8] == y and cubestate[3][6] == z:
        return [1, 2, 3]
    if cubestate[1][2] == y and cubestate[2][8] == z and cubestate[3][6] == x:
        return [2, 3, 1]
    if cubestate[1][2] == z and cubestate[2][8] == x and cubestate[3][6] == y:
        return [3, 1, 2]
    
    if cubestate[3][2] == x and cubestate[4][8] == y and cubestate[5][6] == z:
        return [3, 4, 5]
    if cubestate[3][2] == y and cubestate[4][8] == z and cubestate[5][6] == x:
        return [4, 5, 3]
    if cubestate[3][2] == z and cubestate[4][8] == x and cubestate[5][6] == y:
        return [5, 3, 4]
    
    if cubestate[5][2] == x and cubestate[0][8] == y and cubestate[1][6] == z:
        return [5, 0, 1]
    if cubestate[5][2] == y and cubestate[0][8] == z and cubestate[1][6] == x:
        return [0, 1, 5]
    if cubestate[5][2] == z and cubestate[0][8] == x and cubestate[1][6] == y:
        return [1, 5, 0]
    
    if cubestate[0][0] == x and cubestate[2][0] == y and cubestate[4][0] == z:
        return [0, 2, 4]
    if cubestate[0][0] == y and cubestate[2][0] == z and cubestate[4][0] == x:
        return [2, 4, 0]
    if cubestate[0][0] == z and cubestate[2][0] == x and cubestate[4][0] == y:
        return [4, 0, 2]
    
    if cubestate[1][8] == x and cubestate[3][8] == y and cubestate[5][8] == z:
        return [1, 3, 5]
    if cubestate[1][8] == y and cubestate[3][8] == z and cubestate[5][8] == x:
        return [3, 5, 1]
    if cubestate[1][8] == z and cubestate[3][8] == x and cubestate[5][8] == y:
        return [5, 1, 3]