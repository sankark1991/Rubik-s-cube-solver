# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:38:11 2019

@author: sanka
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:46:01 2019

@author: sanka
"""

import basicturns
import piecefind

"I decided that it will be a lot easier to code the z cross + CE pairs method\
as it relies far less on intuition and heuristics."

face0 = list(map(int, input('Enter cube face 0: ')))
face1 = list(map(int, input('Enter cube face 1: ')))
face2 = list(map(int, input('Enter cube face 2: ')))
face3 = list(map(int, input('Enter cube face 3: ')))
face4 = list(map(int, input('Enter cube face 4: ')))
face5 = list(map(int, input('Enter cube face 5: ')))
cubestate = [face0, face1, face2, face3, face4, face5]
cubestate = list(map(list, cubestate))
moves1 = []

#424302510
#030310540
#322125211
#343033512
#553044451
#154052241
#cubestate = [[4, 2, 4, 3, 0, 2, 5, 1, 0], [0, 3, 0, 3, 1, 0, 5, 4, 0], [3, 2, 2, 1, 2, 5, 2, 1, 1], [3, 4, 3, 0, 3, 3, 5, 1, 2], [5, 5, 3, 0, 4, 4, 4, 5, 1], [1, 5, 4, 0, 5, 2, 2, 4, 1]]

"The first step is to get the four relevant edges all onto the z face, in the\
correct orientation."

for i in [1, 2, 4, 5]:
    z = edgefind(cubestate, 0, i)
    "2 turns: edge is on the white face in wrong orientation."
    if z[1] == 0:
        if z[0] == 1:
            if cubestate[0][1] != 0:
                cubestate = Rturn(cubestate)
                cubestate = Uturn(cubestate)
                moves1.extend(['R', 'U'])
            elif cubestate[0][7] != 0:
                cubestate = Rprimeturn(cubestate)
                cubestate = Dprimeturn(cubestate)
                moves1.extend(['R`', 'D`'])
            else:
                cubestate = Rturn(cubestate)
                cubestate = Fprimeturn(cubestate)
                cubestate = Uturn(cubestate)
                moves1.extend(['R', 'F`', 'U'])               
        if z[0] == 2:
            if cubestate[0][3] != 0:
                cubestate = Uturn(cubestate)
                cubestate = Lturn(cubestate)
                moves1.extend(['U', 'L'])
            elif cubestate[0][5] != 0:
                cubestate = Uprimeturn(cubestate)
                cubestate = Rprimeturn(cubestate)
                moves1.extend(['U`', 'R`'])
            else:
                cubestate = Uturn(cubestate)
                cubestate = Fprimeturn(cubestate)
                cubestate = Lturn(cubestate)
                moves1.extend(['U', 'F`', 'L'])
        if z[0] == 4:
            if cubestate[0][7] != 0:
                cubestate = Lturn(cubestate)
                cubestate = Dturn(cubestate)
                moves1.extend(['L', 'D'])
            elif cubestate[0][1] != 0:
                cubestate = Lprimeturn(cubestate)
                cubestate = Uprimeturn(cubestate)
                moves1.extend(['L`', 'U`'])
            else:
                cubestate = Lturn(cubestate)
                cubestate = Fprimeturn(cubestate)
                cubestate = Dturn(cubestate)
                moves1.extend(['L', 'F`', 'D'])         
        if z[0] == 5:
            if cubestate[0][5] != 0:
                cubestate = Dturn(cubestate)
                cubestate = Rturn(cubestate)
                moves1.extend(['D', 'R'])
            elif cubestate[0][3] != 0:
                cubestate = Dprimeturn(cubestate)
                cubestate = Lprimeturn(cubestate)
                moves1.extend(['D`', 'L`'])
            else:
                cubestate = Dturn(cubestate)
                cubestate = Fprimeturn(cubestate)
                cubestate = Rturn(cubestate)
                moves1.extend(['D', 'F`', 'R']) 
    "2 turns: edge is on the opposite face with the white panel on an adjacent face."
    if z[1] == 3:
        if z[0] == 1:
            while cubestate[0][1] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            if cubestate[0][5] == 0:
                cubestate = Rprimeturn(cubestate)
                cubestate = Uturn(cubestate)
                cubestate = Rturn(cubestate)
                moves1.extend(['R`', 'U', 'R'])
            else:
                cubestate = Rprimeturn(cubestate)
                cubestate = Uturn(cubestate)
                moves1.extend(['R`', 'U'])
        if z[0] == 2:
            while cubestate[0][3] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            if cubestate[0][1] == 0:
                cubestate = Uprimeturn(cubestate)
                cubestate = Lturn(cubestate)
                cubestate = Uturn(cubestate)
                moves1.extend(['U`', 'L', 'U'])
            else:
                cubestate = Uprimeturn(cubestate)
                cubestate = Lturn(cubestate)
                moves1.extend(['U`', 'L'])
        if z[0] == 4:
            while cubestate[0][7] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            if cubestate[0][3] == 0:
                cubestate = Lprimeturn(cubestate)
                cubestate = Dturn(cubestate)
                cubestate = Lturn(cubestate)
                moves1.extend(['L`', 'D', 'L'])
            else:
                cubestate = Lprimeturn(cubestate)
                cubestate = Dturn(cubestate)
                moves1.extend(['L`', 'D'])
        if z[0] == 5:
            while cubestate[0][5] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            if cubestate[0][7] == 0:
                cubestate = Dprimeturn(cubestate)
                cubestate = Rturn(cubestate)
                cubestate = Dturn(cubestate)
                moves1.extend(['D`', 'R', 'D'])
            else:
                cubestate = Dprimeturn(cubestate)
                cubestate = Rturn(cubestate)
                moves1.extend(['D`', 'R'])          
    "1 turn: white panel is on the opposite face."
    if z[0] == 3:
        if z[1] == 1:
            while cubestate[0][5] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = R2turn(cubestate)
            moves1.append('R2')
        if z[1] == 2:
            while cubestate[0][1] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = U2turn(cubestate)
            moves1.append('U2')
        if z[1] == 4:
            while cubestate[0][3] == 0:
                Fturn(cubestate)
                moves1.append('F')
            L2turn(cubestate)
            moves1.append('L2')
        if z[1] == 5:
            while cubestate[0][7] == 0:
                cubestate = Fturn(cubestate)
                moves1.extend(['F'])
            cubestate = D2turn(cubestate)
            moves1.append('D2')
    "1 turn: edge is on two adjacent faces."
    if z[0] == 1:
        if z[1] == 2:
            while cubestate[0][1] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Uturn(cubestate)
            moves1.append('U')
        if z[1] == 5:
            while cubestate[0][7] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Dprimeturn(cubestate)
            moves1.append('D`')      
    if z[0] == 2:
        if z[1] == 1:
            while cubestate[0][5] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Rprimeturn(cubestate)
            moves1.append('R`')
        if z[1] == 4:
            while cubestate[0][3] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Lturn(cubestate)
            moves1.append('L')
    if z[0] == 4:
        if z[1] == 2:
            while cubestate[0][1] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Uprimeturn(cubestate)
            moves1.append('U`')
        if z[1] == 5:
            while cubestate[0][7] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Dturn(cubestate)
            moves1.append('D')        
    if z[0] == 5:
        if z[1] == 1:
            while cubestate[0][5] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Rturn(cubestate)
            moves1.append('R')
        if z[1] == 4:
            while cubestate[0][3] == 0:
                cubestate = Fturn(cubestate)
                moves1.append('F')
            cubestate = Lprimeturn(cubestate)
            moves1.append('L`')

"Now shorten up the list of moves by removing redundancies."
for i in range(len(moves1)-2):
    if moves1[i] == 'F' and moves1[i+1] == 'F' and moves1[i+2] == 'F':
        moves1[i] = 'F`'
        moves1.pop(i+1)
        moves1.pop(i+1)
    elif moves1[i] == 'F' and moves1[i+1] == 'F':
        moves1[i] = 'F2'
        moves1.pop(i+1)

print(moves1)

"The next step is to permute the four cross edges correctly."

moves2 = []
"First, get the [0,1] edge to the right position."
"Case 1: it is on the 2 face"
if cubestate[2][3] == 1:
    cubestate = Fturn(cubestate)
    moves2.append('F')
"Case 2: it is on the 4 face"
if cubestate[4][1] == 1:
    cubestate = F2turn(cubestate)
    moves2.append('F2')
"Case 3: it is on the 5 face"
if cubestate[5][1] == 1:
    cubestate = Fprimeturn(cubestate)
    moves2.append('F`')
    
"Now, there are six possibilities for the positions of the three other edges."
if cubestate[2][3] == 5 and cubestate[5][1] == 2:
    if moves2[0] == 'F2':
        moves2.pop(0)
        moves2.extend(['R', 'F2', 'R`', 'F2', 'R'])
        cubestate = F2turn(cubestate)
        cubestate = Rturn(cubestate)
        cubestate = F2turn(cubestate)
        cubestate = Rprimeturn(cubestate)
        cubestate = F2turn(cubestate)
        cubestate = Rturn(cubestate)
    else:
        moves2.extend(['U', 'F2', 'U`', 'F2', 'U'])
        cubestate = Uturn(cubestate)
        cubestate = F2turn(cubestate)
        cubestate = Uprimeturn(cubestate)
        cubestate = F2turn(cubestate)
        cubestate = Uturn(cubestate)
        
if cubestate[2][3] == 5 and cubestate[4][1] == 2:
    cubestate = Fturn(cubestate)
    if moves2[0] == 'F`':
        moves2.pop(0)
    elif moves2[0] == 'F2':
        moves2.pop(0)
        moves2.append('F`')
    elif moves2[0] == 'F':
        moves2.pop(0)
        moves2.append('F2')
    else:
        moves2.append('F')
    moves2.extend(['R', 'F`', 'R`', 'F', 'R'])
    cubestate = Rturn(cubestate)
    cubestate = Fprimeturn(cubestate)
    cubestate = Rprimeturn(cubestate)
    cubestate = Fturn(cubestate)
    cubestate = Rturn(cubestate)
    
if cubestate[2][3] == 4 and cubestate[4][1] == 5:
    cubestate = Fprimeturn(cubestate)
    if moves2[0] == 'F':
        moves2.pop(0)
    elif moves2[0] == 'F2':
        moves2.pop(0)
        moves2.append('F')
    elif moves2[0] == 'F`':
        moves2.pop(0)
        moves2.append('F2')
    else:
        moves2.append('F`')
    moves2.extend(['R`', 'F', 'R', 'F`', 'R`'])
    cubestate = Rprimeturn(cubestate)
    cubestate = Fturn(cubestate)
    cubestate = Rturn(cubestate)
    cubestate = Fprimeturn(cubestate)
    cubestate = Rprimeturn(cubestate)
        
if cubestate[2][3] == 4 and cubestate[4][1] == 2:
    moves2.extend(['U', 'F', 'U`', 'F`', 'U'])
    cubestate = Uturn(cubestate)
    cubestate = Fturn(cubestate)
    cubestate = Uprimeturn(cubestate)
    cubestate = Fprimeturn(cubestate)
    cubestate = Uturn(cubestate)
    
if cubestate[4][1] == 5 and cubestate[5][1] == 4:
    moves2.extend(['L', 'F', 'L`', 'F`', 'L'])
    cubestate = Lturn(cubestate)
    cubestate = Fturn(cubestate)
    cubestate = Lprimeturn(cubestate)
    cubestate = Fprimeturn(cubestate)
    cubestate = Lturn(cubestate)
    
print(moves2)