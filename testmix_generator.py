# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:35:13 2019

@author: sanka
"""

import random

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

fout = open('random_mixes.txt', 'w')
for n in range(100):
    A = mixgenerator()
    movestr = ''.join(A)
    m = str(n)
    fout.write("'Testmix"+m+": "+movestr+"'\n")
    fout.write("testmix"+m+" = "+str(A)+"\n")
    fout.write("Front"+m+"= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')\n")
    fout.write("Back"+m+"= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')\n")
    fout.write("Up"+m+"= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')\n")
    fout.write("Down"+m+"= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')\n")
    fout.write("Left"+m+"= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')\n")
    fout.write("Right"+m+"= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')\n")
    fout.write("Facelist"+m+" = Facelist(F=Front"+m+",B=Back"+m+",U=Up"+m+",D=Down"+m+",L=Left"+m+",R=Right"+m+")\n")
    fout.write("testcube"+m+" = cubestate(Facelist"+m+")\n")
    fout.write("testcube"+m+".movesexecutor(testmix"+m+")\n")
    fout.write("testcube"+m+".moves.clear()\n")
    fout.write("\n")
    fout.write("print('Testmix"+m+": "+movestr+"')\n")
    fout.write("cubesolve(testcube"+m+")\n")
    fout.write("if testifsolved(testcube"+m+"): pass\n")
    fout.write("else: failedlist.append(str("+m+"))\n")
    fout.write("print("+repr("\n")+")")
    fout.write("\n\n")
fout.write("print(failedlist)")
fout.close()