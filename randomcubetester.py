# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:29:56 2019

@author: sanka
"""

import random
import cubefunctions
import whitecross_2
import F2L_corneredgepair
import last_layer

def cubesolve(cube):
    whitecross(cube)
    F2L(cube)
    lastlayer(cube)
    #print("Solution: "+"".join(cube.moves))
    #print("Number of moves: "+str(len(cube.moves)))
    
def testifsolved(cube):
    solved = True
    for i in cube.F:
        if i != cube.F.mm:
            solved = False
        else:
            continue
    for i in cube.B:
        if i != cube.B.mm:
            solved = False
        else:
            continue
    for i in cube.U:
        if i != cube.U.mm:
            solved = False
        else:
            continue
    for i in cube.D:
        if i != cube.D.mm:
            solved = False
        else:
            continue
    for i in cube.L:
        if i != cube.L.mm:
            solved = False
        else:
            continue
    for i in cube.R:
        if i != cube.R.mm:
            solved = False
        else:
            continue
    return solved
    if solved:
        print("Solution checks out!")
    else:
        print("Solution failed!")

def mixgenerator():
    nums = []
    moves = []
    nums.append(random.randint(1,18))
    for i in range(24):
        j = random.randint(1,18)
        while True:
            cond1 = ((j - nums[i]) % 6 == 0)
            cond2 = (j % 2 == 1) and ((j-nums[i]) % 6 == 1)
            cond3 = (j % 2 == 0) and ((nums[i]-j) % 6 == 1)
            if not (cond1 or cond2 or cond3):
                break            
            j = random.randint(1,18)
        nums.append(j)
    for x in nums:
        if x == 1:
            moves.append('F')
        elif x == 2:
            moves.append('B')
        elif x == 3:
            moves.append('U')
        elif x == 4:
            moves.append('D')
        elif x == 5:
            moves.append('L')
        elif x == 6:
            moves.append('R')
        elif x == 7:
            moves.append('F`')
        elif x == 8:
            moves.append('B`')
        elif x == 9:
            moves.append('U`')
        elif x == 10:
            moves.append('D`')
        elif x == 11:
            moves.append('L`')
        elif x == 12:
            moves.append('R`')
        elif x == 13:
            moves.append('F2')
        elif x == 14:
            moves.append('B2')
        elif x == 15:
            moves.append('U2')
        elif x == 16:
            moves.append('D2')
        elif x == 17:
            moves.append('L2')
        elif x == 18:
            moves.append('R2')
    return moves

failedlist = []

###Change this number to change the number of simulations.
count = 1000
###
total = 0
for n in range(count):
    A = mixgenerator()
    movestr = ''.join(A)
    m = str(n)
    #print("Testmix"+m+": "+movestr+"\n")
    testmix = ['D', 'F`', 'U', 'D`', 'B`', 'L`', 'U', 'F`', 'L2', 'R`', 'U2', 'F`', 'B2', 'D', 'F2', 'B', 'L`', 'B', 'F2', 'U', 'R`', 'D', 'B`', 'D', 'F`']
    Front0= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
    Back0= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
    Up0= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
    Down0= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
    Left0= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
    Right0= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
    Facelist0 = Facelist(F=Front0,B=Back0,U=Up0,D=Down0,L=Left0,R=Right0)
    testcube0 = cubestate(Facelist0)
    testcube0.movesexecutor(A)
    testcube0.moves.clear()
    cubesolve(testcube0)
    total += len(testcube0.moves)
    if testifsolved(testcube0): pass
    else: failedlist.append(str(m))
avg = total/count
print("\n")
print("Mixes which failed: "+str(failedlist))
print("Average number of moves required: "+str(avg))