# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:52:46 2019

@author: sanka
"""

import collections
import cubefunctions
import whitecross_2
import F2L_corneredgepair
import last_layer
import random

def cubesolve(cube):
    whitecross(cube)
    F2L(cube)
    lastlayer(cube)
    print("Solution: "+"".join(cube.moves))
    print("Number of moves: "+str(len(cube.moves)))
    
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
        
failedlist = []

'Testmix0: DF`UD`B`L`UF`L2R`U2F`B2DF2BL`BF2UR`DB`DF`'
testmix0 = ['D', 'F`', 'U', 'D`', 'B`', 'L`', 'U', 'F`', 'L2', 'R`', 'U2', 'F`', 'B2', 'D', 'F2', 'B', 'L`', 'B', 'F2', 'U', 'R`', 'D', 'B`', 'D', 'F`']
Front0= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back0= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up0= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down0= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left0= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right0= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist0 = Facelist(F=Front0,B=Back0,U=Up0,D=Down0,L=Left0,R=Right0)
testcube0 = cubestate(Facelist0)
testcube0.movesexecutor(testmix0)
testcube0.moves.clear()

print('Testmix0: DF`UD`B`L`UF`L2R`U2F`B2DF2BL`BF2UR`DB`DF`')
cubesolve(testcube0)
if testifsolved(testcube0): pass
else: failedlist.append(str(0))
print('\n')

'Testmix1: RLB2F2LU`L2RL`U2LUL2RLB`D`BR`LB2R2L`R`L2'
testmix1 = ['R', 'L', 'B2', 'F2', 'L', 'U`', 'L2', 'R', 'L`', 'U2', 'L', 'U', 'L2', 'R', 'L', 'B`', 'D`', 'B', 'R`', 'L', 'B2', 'R2', 'L`', 'R`', 'L2']
Front1= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back1= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up1= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down1= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left1= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right1= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist1 = Facelist(F=Front1,B=Back1,U=Up1,D=Down1,L=Left1,R=Right1)
testcube1 = cubestate(Facelist1)
testcube1.movesexecutor(testmix1)
testcube1.moves.clear()

print('Testmix1: RLB2F2LU`L2RL`U2LUL2RLB`D`BR`LB2R2L`R`L2')
cubesolve(testcube1)
if testifsolved(testcube1): pass
else: failedlist.append(str(1))
print('\n')

'Testmix2: F`B`FB`L2BD2R2D`U2D2R`BR2B`F`U2F`U2F2U2L2F`DB`'
testmix2 = ['F`', 'B`', 'F', 'B`', 'L2', 'B', 'D2', 'R2', 'D`', 'U2', 'D2', 'R`', 'B', 'R2', 'B`', 'F`', 'U2', 'F`', 'U2', 'F2', 'U2', 'L2', 'F`', 'D', 'B`']
Front2= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back2= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up2= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down2= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left2= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right2= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist2 = Facelist(F=Front2,B=Back2,U=Up2,D=Down2,L=Left2,R=Right2)
testcube2 = cubestate(Facelist2)
testcube2.movesexecutor(testmix2)
testcube2.moves.clear()

print('Testmix2: F`B`FB`L2BD2R2D`U2D2R`BR2B`F`U2F`U2F2U2L2F`DB`')
cubesolve(testcube2)
if testifsolved(testcube2): pass
else: failedlist.append(str(2))
print('\n')

'Testmix3: LUFD`R`B2R2B`F2L2RB2R2UR2U`RD`U`F2LU2R`BL2'
testmix3 = ['L', 'U', 'F', 'D`', 'R`', 'B2', 'R2', 'B`', 'F2', 'L2', 'R', 'B2', 'R2', 'U', 'R2', 'U`', 'R', 'D`', 'U`', 'F2', 'L', 'U2', 'R`', 'B', 'L2']
Front3= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back3= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up3= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down3= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left3= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right3= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist3 = Facelist(F=Front3,B=Back3,U=Up3,D=Down3,L=Left3,R=Right3)
testcube3 = cubestate(Facelist3)
testcube3.movesexecutor(testmix3)
testcube3.moves.clear()

print('Testmix3: LUFD`R`B2R2B`F2L2RB2R2UR2U`RD`U`F2LU2R`BL2')
cubesolve(testcube3)
if testifsolved(testcube3): pass
else: failedlist.append(str(3))
print('\n')

'Testmix4: D`R`D2BF2D2R`LR`UD`B`R`B`DF`DUR2L`R`L`BR`L`'
testmix4 = ['D`', 'R`', 'D2', 'B', 'F2', 'D2', 'R`', 'L', 'R`', 'U', 'D`', 'B`', 'R`', 'B`', 'D', 'F`', 'D', 'U', 'R2', 'L`', 'R`', 'L`', 'B', 'R`', 'L`']
Front4= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back4= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up4= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down4= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left4= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right4= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist4 = Facelist(F=Front4,B=Back4,U=Up4,D=Down4,L=Left4,R=Right4)
testcube4 = cubestate(Facelist4)
testcube4.movesexecutor(testmix4)
testcube4.moves.clear()

print('Testmix4: D`R`D2BF2D2R`LR`UD`B`R`B`DF`DUR2L`R`L`BR`L`')
cubesolve(testcube4)
if testifsolved(testcube4): pass
else: failedlist.append(str(4))
print('\n')

'Testmix5: U2D2U`L`B2DRD2FLUF`B2RUDF`L`R2L2F`DFDB'
testmix5 = ['U2', 'D2', 'U`', 'L`', 'B2', 'D', 'R', 'D2', 'F', 'L', 'U', 'F`', 'B2', 'R', 'U', 'D', 'F`', 'L`', 'R2', 'L2', 'F`', 'D', 'F', 'D', 'B']
Front5= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back5= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up5= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down5= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left5= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right5= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist5 = Facelist(F=Front5,B=Back5,U=Up5,D=Down5,L=Left5,R=Right5)
testcube5 = cubestate(Facelist5)
testcube5.movesexecutor(testmix5)
testcube5.moves.clear()

print('Testmix5: U2D2U`L`B2DRD2FLUF`B2RUDF`L`R2L2F`DFDB')
cubesolve(testcube5)
if testifsolved(testcube5): pass
else: failedlist.append(str(5))
print('\n')

'Testmix6: D`R`DB`D`F2U`F`B`FD`B2D`F`LU2L`FL`F2BR`D`B2L`'
testmix6 = ['D`', 'R`', 'D', 'B`', 'D`', 'F2', 'U`', 'F`', 'B`', 'F', 'D`', 'B2', 'D`', 'F`', 'L', 'U2', 'L`', 'F', 'L`', 'F2', 'B', 'R`', 'D`', 'B2', 'L`']
Front6= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back6= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up6= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down6= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left6= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right6= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist6 = Facelist(F=Front6,B=Back6,U=Up6,D=Down6,L=Left6,R=Right6)
testcube6 = cubestate(Facelist6)
testcube6.movesexecutor(testmix6)
testcube6.moves.clear()

print('Testmix6: D`R`DB`D`F2U`F`B`FD`B2D`F`LU2L`FL`F2BR`D`B2L`')
cubesolve(testcube6)
if testifsolved(testcube6): pass
else: failedlist.append(str(6))
print('\n')

'Testmix7: U`FU2F2LF`LF2L2R`L`U2D2U2DU2DULU2F`UFU2R2'
testmix7 = ['U`', 'F', 'U2', 'F2', 'L', 'F`', 'L', 'F2', 'L2', 'R`', 'L`', 'U2', 'D2', 'U2', 'D', 'U2', 'D', 'U', 'L', 'U2', 'F`', 'U', 'F', 'U2', 'R2']
Front7= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back7= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up7= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down7= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left7= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right7= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist7 = Facelist(F=Front7,B=Back7,U=Up7,D=Down7,L=Left7,R=Right7)
testcube7 = cubestate(Facelist7)
testcube7.movesexecutor(testmix7)
testcube7.moves.clear()

print('Testmix7: U`FU2F2LF`LF2L2R`L`U2D2U2DU2DULU2F`UFU2R2')
cubesolve(testcube7)
if testifsolved(testcube7): pass
else: failedlist.append(str(7))
print('\n')

'Testmix8: D2U2D2R2D2R`U`RU`L2UD`B2R`DFUR2BF2B2DR`UR'
testmix8 = ['D2', 'U2', 'D2', 'R2', 'D2', 'R`', 'U`', 'R', 'U`', 'L2', 'U', 'D`', 'B2', 'R`', 'D', 'F', 'U', 'R2', 'B', 'F2', 'B2', 'D', 'R`', 'U', 'R']
Front8= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back8= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up8= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down8= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left8= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right8= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist8 = Facelist(F=Front8,B=Back8,U=Up8,D=Down8,L=Left8,R=Right8)
testcube8 = cubestate(Facelist8)
testcube8.movesexecutor(testmix8)
testcube8.moves.clear()

print('Testmix8: D2U2D2R2D2R`U`RU`L2UD`B2R`DFUR2BF2B2DR`UR')
cubesolve(testcube8)
if testifsolved(testcube8): pass
else: failedlist.append(str(8))
print('\n')

'Testmix9: R2DB`L2B2LBF2UR2L`B2F`BD`RD`RLUD`RUF2D`'
testmix9 = ['R2', 'D', 'B`', 'L2', 'B2', 'L', 'B', 'F2', 'U', 'R2', 'L`', 'B2', 'F`', 'B', 'D`', 'R', 'D`', 'R', 'L', 'U', 'D`', 'R', 'U', 'F2', 'D`']
Front9= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back9= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up9= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down9= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left9= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right9= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist9 = Facelist(F=Front9,B=Back9,U=Up9,D=Down9,L=Left9,R=Right9)
testcube9 = cubestate(Facelist9)
testcube9.movesexecutor(testmix9)
testcube9.moves.clear()

print('Testmix9: R2DB`L2B2LBF2UR2L`B2F`BD`RD`RLUD`RUF2D`')
cubesolve(testcube9)
if testifsolved(testcube9): pass
else: failedlist.append(str(9))
print('\n')

'Testmix10: F2U2LUFU2F`D`F`L`R`UF`DFU2F2B2D2B2R2B2DB`F'
testmix10 = ['F2', 'U2', 'L', 'U', 'F', 'U2', 'F`', 'D`', 'F`', 'L`', 'R`', 'U', 'F`', 'D', 'F', 'U2', 'F2', 'B2', 'D2', 'B2', 'R2', 'B2', 'D', 'B`', 'F']
Front10= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back10= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up10= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down10= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left10= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right10= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist10 = Facelist(F=Front10,B=Back10,U=Up10,D=Down10,L=Left10,R=Right10)
testcube10 = cubestate(Facelist10)
testcube10.movesexecutor(testmix10)
testcube10.moves.clear()

print('Testmix10: F2U2LUFU2F`D`F`L`R`UF`DFU2F2B2D2B2R2B2DB`F')
cubesolve(testcube10)
if testifsolved(testcube10): pass
else: failedlist.append(str(10))
print('\n')

'Testmix11: F2B2F`B`DF2U2LFLUD`U2D2F2L2BR2D`R2L`B`RB2D2'
testmix11 = ['F2', 'B2', 'F`', 'B`', 'D', 'F2', 'U2', 'L', 'F', 'L', 'U', 'D`', 'U2', 'D2', 'F2', 'L2', 'B', 'R2', 'D`', 'R2', 'L`', 'B`', 'R', 'B2', 'D2']
Front11= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back11= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up11= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down11= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left11= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right11= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist11 = Facelist(F=Front11,B=Back11,U=Up11,D=Down11,L=Left11,R=Right11)
testcube11 = cubestate(Facelist11)
testcube11.movesexecutor(testmix11)
testcube11.moves.clear()

print('Testmix11: F2B2F`B`DF2U2LFLUD`U2D2F2L2BR2D`R2L`B`RB2D2')
cubesolve(testcube11)
if testifsolved(testcube11): pass
else: failedlist.append(str(11))
print('\n')

'Testmix12: D`R2L`U2DFU2F`B`F`LFDBD2URL2FUD`R2D`F2U2'
testmix12 = ['D`', 'R2', 'L`', 'U2', 'D', 'F', 'U2', 'F`', 'B`', 'F`', 'L', 'F', 'D', 'B', 'D2', 'U', 'R', 'L2', 'F', 'U', 'D`', 'R2', 'D`', 'F2', 'U2']
Front12= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back12= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up12= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down12= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left12= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right12= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist12 = Facelist(F=Front12,B=Back12,U=Up12,D=Down12,L=Left12,R=Right12)
testcube12 = cubestate(Facelist12)
testcube12.movesexecutor(testmix12)
testcube12.moves.clear()

print('Testmix12: D`R2L`U2DFU2F`B`F`LFDBD2URL2FUD`R2D`F2U2')
cubesolve(testcube12)
if testifsolved(testcube12): pass
else: failedlist.append(str(12))
print('\n')

'Testmix13: D`R2BDBDF2L`UD`B2FL`U`RD`B2R2L`U2D`BFL`R'
testmix13 = ['D`', 'R2', 'B', 'D', 'B', 'D', 'F2', 'L`', 'U', 'D`', 'B2', 'F', 'L`', 'U`', 'R', 'D`', 'B2', 'R2', 'L`', 'U2', 'D`', 'B', 'F', 'L`', 'R']
Front13= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back13= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up13= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down13= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left13= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right13= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist13 = Facelist(F=Front13,B=Back13,U=Up13,D=Down13,L=Left13,R=Right13)
testcube13 = cubestate(Facelist13)
testcube13.movesexecutor(testmix13)
testcube13.moves.clear()

print('Testmix13: D`R2BDBDF2L`UD`B2FL`U`RD`B2R2L`U2D`BFL`R')
cubesolve(testcube13)
if testifsolved(testcube13): pass
else: failedlist.append(str(13))
print('\n')

'Testmix14: U2LF2DBR`L2R`D2R`BF`LFUR2LU`F`D2B2D2R2U`D'
testmix14 = ['U2', 'L', 'F2', 'D', 'B', 'R`', 'L2', 'R`', 'D2', 'R`', 'B', 'F`', 'L', 'F', 'U', 'R2', 'L', 'U`', 'F`', 'D2', 'B2', 'D2', 'R2', 'U`', 'D']
Front14= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back14= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up14= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down14= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left14= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right14= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist14 = Facelist(F=Front14,B=Back14,U=Up14,D=Down14,L=Left14,R=Right14)
testcube14 = cubestate(Facelist14)
testcube14.movesexecutor(testmix14)
testcube14.moves.clear()

print('Testmix14: U2LF2DBR`L2R`D2R`BF`LFUR2LU`F`D2B2D2R2U`D')
cubesolve(testcube14)
if testifsolved(testcube14): pass
else: failedlist.append(str(14))
print('\n')

'Testmix15: L2U`FD2U`R2L2F2D2B2F`B`F2U`L2F2B`L`FU2R`U`D`FD2'
testmix15 = ['L2', 'U`', 'F', 'D2', 'U`', 'R2', 'L2', 'F2', 'D2', 'B2', 'F`', 'B`', 'F2', 'U`', 'L2', 'F2', 'B`', 'L`', 'F', 'U2', 'R`', 'U`', 'D`', 'F', 'D2']
Front15= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back15= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up15= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down15= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left15= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right15= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist15 = Facelist(F=Front15,B=Back15,U=Up15,D=Down15,L=Left15,R=Right15)
testcube15 = cubestate(Facelist15)
testcube15.movesexecutor(testmix15)
testcube15.moves.clear()

print('Testmix15: L2U`FD2U`R2L2F2D2B2F`B`F2U`L2F2B`L`FU2R`U`D`FD2')
cubesolve(testcube15)
if testifsolved(testcube15): pass
else: failedlist.append(str(15))
print('\n')

'Testmix16: L`F`L2F2U`RUD`FD2FD2RU`FD`UD`B2R`D2U`D`RL2'
testmix16 = ['L`', 'F`', 'L2', 'F2', 'U`', 'R', 'U', 'D`', 'F', 'D2', 'F', 'D2', 'R', 'U`', 'F', 'D`', 'U', 'D`', 'B2', 'R`', 'D2', 'U`', 'D`', 'R', 'L2']
Front16= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back16= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up16= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down16= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left16= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right16= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist16 = Facelist(F=Front16,B=Back16,U=Up16,D=Down16,L=Left16,R=Right16)
testcube16 = cubestate(Facelist16)
testcube16.movesexecutor(testmix16)
testcube16.moves.clear()

print('Testmix16: L`F`L2F2U`RUD`FD2FD2RU`FD`UD`B2R`D2U`D`RL2')
cubesolve(testcube16)
if testifsolved(testcube16): pass
else: failedlist.append(str(16))
print('\n')

'Testmix17: U2FL`B2F`U`R2B2R2DU2FDURULFLBLBLB2R'
testmix17 = ['U2', 'F', 'L`', 'B2', 'F`', 'U`', 'R2', 'B2', 'R2', 'D', 'U2', 'F', 'D', 'U', 'R', 'U', 'L', 'F', 'L', 'B', 'L', 'B', 'L', 'B2', 'R']
Front17= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back17= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up17= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down17= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left17= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right17= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist17 = Facelist(F=Front17,B=Back17,U=Up17,D=Down17,L=Left17,R=Right17)
testcube17 = cubestate(Facelist17)
testcube17.movesexecutor(testmix17)
testcube17.moves.clear()

print('Testmix17: U2FL`B2F`U`R2B2R2DU2FDURULFLBLBLB2R')
cubesolve(testcube17)
if testifsolved(testcube17): pass
else: failedlist.append(str(17))
print('\n')

'Testmix18: D`B`R2B`L`FB2R2U2L2R2BRU`L2B2L2F2UR`DUF`B`D2'
testmix18 = ['D`', 'B`', 'R2', 'B`', 'L`', 'F', 'B2', 'R2', 'U2', 'L2', 'R2', 'B', 'R', 'U`', 'L2', 'B2', 'L2', 'F2', 'U', 'R`', 'D', 'U', 'F`', 'B`', 'D2']
Front18= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back18= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up18= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down18= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left18= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right18= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist18 = Facelist(F=Front18,B=Back18,U=Up18,D=Down18,L=Left18,R=Right18)
testcube18 = cubestate(Facelist18)
testcube18.movesexecutor(testmix18)
testcube18.moves.clear()

print('Testmix18: D`B`R2B`L`FB2R2U2L2R2BRU`L2B2L2F2UR`DUF`B`D2')
cubesolve(testcube18)
if testifsolved(testcube18): pass
else: failedlist.append(str(18))
print('\n')

'Testmix19: L2U2LRU`L`B`RDRLB`D2B2DU`FB`D`U2D2FU2L2R`'
testmix19 = ['L2', 'U2', 'L', 'R', 'U`', 'L`', 'B`', 'R', 'D', 'R', 'L', 'B`', 'D2', 'B2', 'D', 'U`', 'F', 'B`', 'D`', 'U2', 'D2', 'F', 'U2', 'L2', 'R`']
Front19= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back19= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up19= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down19= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left19= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right19= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist19 = Facelist(F=Front19,B=Back19,U=Up19,D=Down19,L=Left19,R=Right19)
testcube19 = cubestate(Facelist19)
testcube19.movesexecutor(testmix19)
testcube19.moves.clear()

print('Testmix19: L2U2LRU`L`B`RDRLB`D2B2DU`FB`D`U2D2FU2L2R`')
cubesolve(testcube19)
if testifsolved(testcube19): pass
else: failedlist.append(str(19))
print('\n')

'Testmix20: U`RL2F`L`F`BL2R`DUR2B`F2B2F`U2FDF`B2FU`F2B`'
testmix20 = ['U`', 'R', 'L2', 'F`', 'L`', 'F`', 'B', 'L2', 'R`', 'D', 'U', 'R2', 'B`', 'F2', 'B2', 'F`', 'U2', 'F', 'D', 'F`', 'B2', 'F', 'U`', 'F2', 'B`']
Front20= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back20= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up20= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down20= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left20= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right20= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist20 = Facelist(F=Front20,B=Back20,U=Up20,D=Down20,L=Left20,R=Right20)
testcube20 = cubestate(Facelist20)
testcube20.movesexecutor(testmix20)
testcube20.moves.clear()

print('Testmix20: U`RL2F`L`F`BL2R`DUR2B`F2B2F`U2FDF`B2FU`F2B`')
cubesolve(testcube20)
if testifsolved(testcube20): pass
else: failedlist.append(str(20))
print('\n')

'Testmix21: F2BFUL`F2B2R2D`F2L`BFB`F`U`L2RL`R`L2U2R2B`L2'
testmix21 = ['F2', 'B', 'F', 'U', 'L`', 'F2', 'B2', 'R2', 'D`', 'F2', 'L`', 'B', 'F', 'B`', 'F`', 'U`', 'L2', 'R', 'L`', 'R`', 'L2', 'U2', 'R2', 'B`', 'L2']
Front21= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back21= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up21= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down21= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left21= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right21= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist21 = Facelist(F=Front21,B=Back21,U=Up21,D=Down21,L=Left21,R=Right21)
testcube21 = cubestate(Facelist21)
testcube21.movesexecutor(testmix21)
testcube21.moves.clear()

print('Testmix21: F2BFUL`F2B2R2D`F2L`BFB`F`U`L2RL`R`L2U2R2B`L2')
cubesolve(testcube21)
if testifsolved(testcube21): pass
else: failedlist.append(str(21))
print('\n')

'Testmix22: U2R`UF`B2L2F`B2F`DU2LR2BD`F`BDRU2D2F2BR`L2'
testmix22 = ['U2', 'R`', 'U', 'F`', 'B2', 'L2', 'F`', 'B2', 'F`', 'D', 'U2', 'L', 'R2', 'B', 'D`', 'F`', 'B', 'D', 'R', 'U2', 'D2', 'F2', 'B', 'R`', 'L2']
Front22= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back22= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up22= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down22= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left22= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right22= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist22 = Facelist(F=Front22,B=Back22,U=Up22,D=Down22,L=Left22,R=Right22)
testcube22 = cubestate(Facelist22)
testcube22.movesexecutor(testmix22)
testcube22.moves.clear()

print('Testmix22: U2R`UF`B2L2F`B2F`DU2LR2BD`F`BDRU2D2F2BR`L2')
cubesolve(testcube22)
if testifsolved(testcube22): pass
else: failedlist.append(str(22))
print('\n')

'Testmix23: FU`D`RDU2F`D`F2L`U2F`U`RB`DRL2B`L2UL2U2F2U`'
testmix23 = ['F', 'U`', 'D`', 'R', 'D', 'U2', 'F`', 'D`', 'F2', 'L`', 'U2', 'F`', 'U`', 'R', 'B`', 'D', 'R', 'L2', 'B`', 'L2', 'U', 'L2', 'U2', 'F2', 'U`']
Front23= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back23= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up23= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down23= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left23= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right23= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist23 = Facelist(F=Front23,B=Back23,U=Up23,D=Down23,L=Left23,R=Right23)
testcube23 = cubestate(Facelist23)
testcube23.movesexecutor(testmix23)
testcube23.moves.clear()

print('Testmix23: FU`D`RDU2F`D`F2L`U2F`U`RB`DRL2B`L2UL2U2F2U`')
cubesolve(testcube23)
if testifsolved(testcube23): pass
else: failedlist.append(str(23))
print('\n')

'Testmix24: L2BR2B`F2LF`L`BF2L2F`D`BD`F`UF2L`F`L2R`BL2B'
testmix24 = ['L2', 'B', 'R2', 'B`', 'F2', 'L', 'F`', 'L`', 'B', 'F2', 'L2', 'F`', 'D`', 'B', 'D`', 'F`', 'U', 'F2', 'L`', 'F`', 'L2', 'R`', 'B', 'L2', 'B']
Front24= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back24= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up24= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down24= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left24= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right24= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist24 = Facelist(F=Front24,B=Back24,U=Up24,D=Down24,L=Left24,R=Right24)
testcube24 = cubestate(Facelist24)
testcube24.movesexecutor(testmix24)
testcube24.moves.clear()

print('Testmix24: L2BR2B`F2LF`L`BF2L2F`D`BD`F`UF2L`F`L2R`BL2B')
cubesolve(testcube24)
if testifsolved(testcube24): pass
else: failedlist.append(str(24))
print('\n')

'Testmix25: R2LB2DF`BF2U`R2D`B`D`B`F2U2FU`DB`F2LRB`RD`'
testmix25 = ['R2', 'L', 'B2', 'D', 'F`', 'B', 'F2', 'U`', 'R2', 'D`', 'B`', 'D`', 'B`', 'F2', 'U2', 'F', 'U`', 'D', 'B`', 'F2', 'L', 'R', 'B`', 'R', 'D`']
Front25= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back25= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up25= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down25= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left25= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right25= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist25 = Facelist(F=Front25,B=Back25,U=Up25,D=Down25,L=Left25,R=Right25)
testcube25 = cubestate(Facelist25)
testcube25.movesexecutor(testmix25)
testcube25.moves.clear()

print('Testmix25: R2LB2DF`BF2U`R2D`B`D`B`F2U2FU`DB`F2LRB`RD`')
cubesolve(testcube25)
if testifsolved(testcube25): pass
else: failedlist.append(str(25))
print('\n')

'Testmix26: DB`F`L2B`R2L2B2L2F`B`D`R2UD2B2RLB2FD`RL`UF`'
testmix26 = ['D', 'B`', 'F`', 'L2', 'B`', 'R2', 'L2', 'B2', 'L2', 'F`', 'B`', 'D`', 'R2', 'U', 'D2', 'B2', 'R', 'L', 'B2', 'F', 'D`', 'R', 'L`', 'U', 'F`']
Front26= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back26= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up26= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down26= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left26= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right26= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist26 = Facelist(F=Front26,B=Back26,U=Up26,D=Down26,L=Left26,R=Right26)
testcube26 = cubestate(Facelist26)
testcube26.movesexecutor(testmix26)
testcube26.moves.clear()

print('Testmix26: DB`F`L2B`R2L2B2L2F`B`D`R2UD2B2RLB2FD`RL`UF`')
cubesolve(testcube26)
if testifsolved(testcube26): pass
else: failedlist.append(str(26))
print('\n')

'Testmix27: D2U`L2UL`R`B`F`L2R2URD2R`DB`DR2U2L2R2D`UR`B'
testmix27 = ['D2', 'U`', 'L2', 'U', 'L`', 'R`', 'B`', 'F`', 'L2', 'R2', 'U', 'R', 'D2', 'R`', 'D', 'B`', 'D', 'R2', 'U2', 'L2', 'R2', 'D`', 'U', 'R`', 'B']
Front27= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back27= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up27= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down27= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left27= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right27= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist27 = Facelist(F=Front27,B=Back27,U=Up27,D=Down27,L=Left27,R=Right27)
testcube27 = cubestate(Facelist27)
testcube27.movesexecutor(testmix27)
testcube27.moves.clear()

print('Testmix27: D2U`L2UL`R`B`F`L2R2URD2R`DB`DR2U2L2R2D`UR`B')
cubesolve(testcube27)
if testifsolved(testcube27): pass
else: failedlist.append(str(27))
print('\n')

'Testmix28: L2B`R2U`R`BR2BD2FU2D2F`UR`D2F2B2R`DU`L2BRD`'
testmix28 = ['L2', 'B`', 'R2', 'U`', 'R`', 'B', 'R2', 'B', 'D2', 'F', 'U2', 'D2', 'F`', 'U', 'R`', 'D2', 'F2', 'B2', 'R`', 'D', 'U`', 'L2', 'B', 'R', 'D`']
Front28= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back28= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up28= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down28= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left28= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right28= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist28 = Facelist(F=Front28,B=Back28,U=Up28,D=Down28,L=Left28,R=Right28)
testcube28 = cubestate(Facelist28)
testcube28.movesexecutor(testmix28)
testcube28.moves.clear()

print('Testmix28: L2B`R2U`R`BR2BD2FU2D2F`UR`D2F2B2R`DU`L2BRD`')
cubesolve(testcube28)
if testifsolved(testcube28): pass
else: failedlist.append(str(28))
print('\n')

'Testmix29: U2R2DF2L`FU`LBDF2BR`L2UD2BFL`R`L`UFU2R'
testmix29 = ['U2', 'R2', 'D', 'F2', 'L`', 'F', 'U`', 'L', 'B', 'D', 'F2', 'B', 'R`', 'L2', 'U', 'D2', 'B', 'F', 'L`', 'R`', 'L`', 'U', 'F', 'U2', 'R']
Front29= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back29= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up29= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down29= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left29= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right29= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist29 = Facelist(F=Front29,B=Back29,U=Up29,D=Down29,L=Left29,R=Right29)
testcube29 = cubestate(Facelist29)
testcube29.movesexecutor(testmix29)
testcube29.moves.clear()

print('Testmix29: U2R2DF2L`FU`LBDF2BR`L2UD2BFL`R`L`UFU2R')
cubesolve(testcube29)
if testifsolved(testcube29): pass
else: failedlist.append(str(29))
print('\n')

'Testmix30: DFD`BR2L`FD2FU`RUFL2B2LF2DR`B`R`UL`F2L`'
testmix30 = ['D', 'F', 'D`', 'B', 'R2', 'L`', 'F', 'D2', 'F', 'U`', 'R', 'U', 'F', 'L2', 'B2', 'L', 'F2', 'D', 'R`', 'B`', 'R`', 'U', 'L`', 'F2', 'L`']
Front30= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back30= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up30= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down30= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left30= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right30= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist30 = Facelist(F=Front30,B=Back30,U=Up30,D=Down30,L=Left30,R=Right30)
testcube30 = cubestate(Facelist30)
testcube30.movesexecutor(testmix30)
testcube30.moves.clear()

print('Testmix30: DFD`BR2L`FD2FU`RUFL2B2LF2DR`B`R`UL`F2L`')
cubesolve(testcube30)
if testifsolved(testcube30): pass
else: failedlist.append(str(30))
print('\n')

'Testmix31: L`FBR2LU`F`L`B2D`F2U`D2FD2RLF`DR`BF2DRD2'
testmix31 = ['L`', 'F', 'B', 'R2', 'L', 'U`', 'F`', 'L`', 'B2', 'D`', 'F2', 'U`', 'D2', 'F', 'D2', 'R', 'L', 'F`', 'D', 'R`', 'B', 'F2', 'D', 'R', 'D2']
Front31= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back31= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up31= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down31= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left31= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right31= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist31 = Facelist(F=Front31,B=Back31,U=Up31,D=Down31,L=Left31,R=Right31)
testcube31 = cubestate(Facelist31)
testcube31.movesexecutor(testmix31)
testcube31.moves.clear()

print('Testmix31: L`FBR2LU`F`L`B2D`F2U`D2FD2RLF`DR`BF2DRD2')
cubesolve(testcube31)
if testifsolved(testcube31): pass
else: failedlist.append(str(31))
print('\n')

'Testmix32: F2UR2B`L`UR`B2D2BR2L`U`RB`RU`L2BR2U2L`B2LB`'
testmix32 = ['F2', 'U', 'R2', 'B`', 'L`', 'U', 'R`', 'B2', 'D2', 'B', 'R2', 'L`', 'U`', 'R', 'B`', 'R', 'U`', 'L2', 'B', 'R2', 'U2', 'L`', 'B2', 'L', 'B`']
Front32= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back32= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up32= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down32= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left32= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right32= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist32 = Facelist(F=Front32,B=Back32,U=Up32,D=Down32,L=Left32,R=Right32)
testcube32 = cubestate(Facelist32)
testcube32.movesexecutor(testmix32)
testcube32.moves.clear()

print('Testmix32: F2UR2B`L`UR`B2D2BR2L`U`RB`RU`L2BR2U2L`B2LB`')
cubesolve(testcube32)
if testifsolved(testcube32): pass
else: failedlist.append(str(32))
print('\n')

'Testmix33: L2B`F2DU2L2R`B`L`F`B2R2D`R2D2R`L2BLR`BL2UD2U`'
testmix33 = ['L2', 'B`', 'F2', 'D', 'U2', 'L2', 'R`', 'B`', 'L`', 'F`', 'B2', 'R2', 'D`', 'R2', 'D2', 'R`', 'L2', 'B', 'L', 'R`', 'B', 'L2', 'U', 'D2', 'U`']
Front33= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back33= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up33= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down33= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left33= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right33= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist33 = Facelist(F=Front33,B=Back33,U=Up33,D=Down33,L=Left33,R=Right33)
testcube33 = cubestate(Facelist33)
testcube33.movesexecutor(testmix33)
testcube33.moves.clear()

print('Testmix33: L2B`F2DU2L2R`B`L`F`B2R2D`R2D2R`L2BLR`BL2UD2U`')
cubesolve(testcube33)
if testifsolved(testcube33): pass
else: failedlist.append(str(33))
print('\n')

'Testmix34: L`B`D`BR`LR2D2B`R`L2R2B`F`U2D`B`L`U2DUL2R2L`B2'
testmix34 = ['L`', 'B`', 'D`', 'B', 'R`', 'L', 'R2', 'D2', 'B`', 'R`', 'L2', 'R2', 'B`', 'F`', 'U2', 'D`', 'B`', 'L`', 'U2', 'D', 'U', 'L2', 'R2', 'L`', 'B2']
Front34= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back34= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up34= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down34= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left34= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right34= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist34 = Facelist(F=Front34,B=Back34,U=Up34,D=Down34,L=Left34,R=Right34)
testcube34 = cubestate(Facelist34)
testcube34.movesexecutor(testmix34)
testcube34.moves.clear()

print('Testmix34: L`B`D`BR`LR2D2B`R`L2R2B`F`U2D`B`L`U2DUL2R2L`B2')
cubesolve(testcube34)
if testifsolved(testcube34): pass
else: failedlist.append(str(34))
print('\n')

'Testmix35: DU2D2RLU`D2FU2F`D2B`LR`B`FL2FL`BLF2D2R`B2'
testmix35 = ['D', 'U2', 'D2', 'R', 'L', 'U`', 'D2', 'F', 'U2', 'F`', 'D2', 'B`', 'L', 'R`', 'B`', 'F', 'L2', 'F', 'L`', 'B', 'L', 'F2', 'D2', 'R`', 'B2']
Front35= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back35= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up35= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down35= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left35= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right35= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist35 = Facelist(F=Front35,B=Back35,U=Up35,D=Down35,L=Left35,R=Right35)
testcube35 = cubestate(Facelist35)
testcube35.movesexecutor(testmix35)
testcube35.moves.clear()

print('Testmix35: DU2D2RLU`D2FU2F`D2B`LR`B`FL2FL`BLF2D2R`B2')
cubesolve(testcube35)
if testifsolved(testcube35): pass
else: failedlist.append(str(35))
print('\n')

'Testmix36: UFBRB2R`BFU`RD`R`U`D2B`L2U2L`FURU`DU2D`'
testmix36 = ['U', 'F', 'B', 'R', 'B2', 'R`', 'B', 'F', 'U`', 'R', 'D`', 'R`', 'U`', 'D2', 'B`', 'L2', 'U2', 'L`', 'F', 'U', 'R', 'U`', 'D', 'U2', 'D`']
Front36= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back36= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up36= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down36= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left36= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right36= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist36 = Facelist(F=Front36,B=Back36,U=Up36,D=Down36,L=Left36,R=Right36)
testcube36 = cubestate(Facelist36)
testcube36.movesexecutor(testmix36)
testcube36.moves.clear()

print('Testmix36: UFBRB2R`BFU`RD`R`U`D2B`L2U2L`FURU`DU2D`')
cubesolve(testcube36)
if testifsolved(testcube36): pass
else: failedlist.append(str(36))
print('\n')

'Testmix37: FL2R2UD2U2DFB`LR2LFU2R`B`L`R2L2B2L`FD`R2L'
testmix37 = ['F', 'L2', 'R2', 'U', 'D2', 'U2', 'D', 'F', 'B`', 'L', 'R2', 'L', 'F', 'U2', 'R`', 'B`', 'L`', 'R2', 'L2', 'B2', 'L`', 'F', 'D`', 'R2', 'L']
Front37= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back37= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up37= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down37= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left37= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right37= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist37 = Facelist(F=Front37,B=Back37,U=Up37,D=Down37,L=Left37,R=Right37)
testcube37 = cubestate(Facelist37)
testcube37.movesexecutor(testmix37)
testcube37.moves.clear()

print('Testmix37: FL2R2UD2U2DFB`LR2LFU2R`B`L`R2L2B2L`FD`R2L')
cubesolve(testcube37)
if testifsolved(testcube37): pass
else: failedlist.append(str(37))
print('\n')

'Testmix38: R`B2R2UF`DU2R2D`R2DF2UR`U2D2R`U2F`ULR`D`FL2'
testmix38 = ['R`', 'B2', 'R2', 'U', 'F`', 'D', 'U2', 'R2', 'D`', 'R2', 'D', 'F2', 'U', 'R`', 'U2', 'D2', 'R`', 'U2', 'F`', 'U', 'L', 'R`', 'D`', 'F', 'L2']
Front38= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back38= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up38= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down38= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left38= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right38= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist38 = Facelist(F=Front38,B=Back38,U=Up38,D=Down38,L=Left38,R=Right38)
testcube38 = cubestate(Facelist38)
testcube38.movesexecutor(testmix38)
testcube38.moves.clear()

print('Testmix38: R`B2R2UF`DU2R2D`R2DF2UR`U2D2R`U2F`ULR`D`FL2')
cubesolve(testcube38)
if testifsolved(testcube38): pass
else: failedlist.append(str(38))
print('\n')

'Testmix39: B2D`R`U`LURD`B`FB`L2B`D`R2D`R`UF2BR`L2FD`U2'
testmix39 = ['B2', 'D`', 'R`', 'U`', 'L', 'U', 'R', 'D`', 'B`', 'F', 'B`', 'L2', 'B`', 'D`', 'R2', 'D`', 'R`', 'U', 'F2', 'B', 'R`', 'L2', 'F', 'D`', 'U2']
Front39= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back39= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up39= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down39= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left39= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right39= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist39 = Facelist(F=Front39,B=Back39,U=Up39,D=Down39,L=Left39,R=Right39)
testcube39 = cubestate(Facelist39)
testcube39.movesexecutor(testmix39)
testcube39.moves.clear()

print('Testmix39: B2D`R`U`LURD`B`FB`L2B`D`R2D`R`UF2BR`L2FD`U2')
cubesolve(testcube39)
if testifsolved(testcube39): pass
else: failedlist.append(str(39))
print('\n')

'Testmix40: F2B2F`L2F`BLR2BL`R2DF2U2F`DR2DB`FU`R2LB2R`'
testmix40 = ['F2', 'B2', 'F`', 'L2', 'F`', 'B', 'L', 'R2', 'B', 'L`', 'R2', 'D', 'F2', 'U2', 'F`', 'D', 'R2', 'D', 'B`', 'F', 'U`', 'R2', 'L', 'B2', 'R`']
Front40= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back40= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up40= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down40= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left40= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right40= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist40 = Facelist(F=Front40,B=Back40,U=Up40,D=Down40,L=Left40,R=Right40)
testcube40 = cubestate(Facelist40)
testcube40.movesexecutor(testmix40)
testcube40.moves.clear()

print('Testmix40: F2B2F`L2F`BLR2BL`R2DF2U2F`DR2DB`FU`R2LB2R`')
cubesolve(testcube40)
if testifsolved(testcube40): pass
else: failedlist.append(str(40))
print('\n')

'Testmix41: D`RLBLR2U2L`R`U2RU2R2ULB2LB`RBL2FB`R2L`'
testmix41 = ['D`', 'R', 'L', 'B', 'L', 'R2', 'U2', 'L`', 'R`', 'U2', 'R', 'U2', 'R2', 'U', 'L', 'B2', 'L', 'B`', 'R', 'B', 'L2', 'F', 'B`', 'R2', 'L`']
Front41= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back41= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up41= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down41= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left41= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right41= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist41 = Facelist(F=Front41,B=Back41,U=Up41,D=Down41,L=Left41,R=Right41)
testcube41 = cubestate(Facelist41)
testcube41.movesexecutor(testmix41)
testcube41.moves.clear()

print('Testmix41: D`RLBLR2U2L`R`U2RU2R2ULB2LB`RBL2FB`R2L`')
cubesolve(testcube41)
if testifsolved(testcube41): pass
else: failedlist.append(str(41))
print('\n')

'Testmix42: D2R`B`F2D`B2F2BL`U`F`U2F2DB`L2B`LUF2L`U`FUF`'
testmix42 = ['D2', 'R`', 'B`', 'F2', 'D`', 'B2', 'F2', 'B', 'L`', 'U`', 'F`', 'U2', 'F2', 'D', 'B`', 'L2', 'B`', 'L', 'U', 'F2', 'L`', 'U`', 'F', 'U', 'F`']
Front42= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back42= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up42= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down42= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left42= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right42= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist42 = Facelist(F=Front42,B=Back42,U=Up42,D=Down42,L=Left42,R=Right42)
testcube42 = cubestate(Facelist42)
testcube42.movesexecutor(testmix42)
testcube42.moves.clear()

print('Testmix42: D2R`B`F2D`B2F2BL`U`F`U2F2DB`L2B`LUF2L`U`FUF`')
cubesolve(testcube42)
if testifsolved(testcube42): pass
else: failedlist.append(str(42))
print('\n')

'Testmix43: DUF2DU`L`B`RLFU2DUD`RDF`U`R2BL`U2L`F2B2'
testmix43 = ['D', 'U', 'F2', 'D', 'U`', 'L`', 'B`', 'R', 'L', 'F', 'U2', 'D', 'U', 'D`', 'R', 'D', 'F`', 'U`', 'R2', 'B', 'L`', 'U2', 'L`', 'F2', 'B2']
Front43= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back43= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up43= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down43= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left43= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right43= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist43 = Facelist(F=Front43,B=Back43,U=Up43,D=Down43,L=Left43,R=Right43)
testcube43 = cubestate(Facelist43)
testcube43.movesexecutor(testmix43)
testcube43.moves.clear()

print('Testmix43: DUF2DU`L`B`RLFU2DUD`RDF`U`R2BL`U2L`F2B2')
cubesolve(testcube43)
if testifsolved(testcube43): pass
else: failedlist.append(str(43))
print('\n')

'Testmix44: BR`L`B`F2BRL`UL2B`F`B2F2BL`RL2R`U2RLR`D2B2'
testmix44 = ['B', 'R`', 'L`', 'B`', 'F2', 'B', 'R', 'L`', 'U', 'L2', 'B`', 'F`', 'B2', 'F2', 'B', 'L`', 'R', 'L2', 'R`', 'U2', 'R', 'L', 'R`', 'D2', 'B2']
Front44= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back44= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up44= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down44= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left44= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right44= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist44 = Facelist(F=Front44,B=Back44,U=Up44,D=Down44,L=Left44,R=Right44)
testcube44 = cubestate(Facelist44)
testcube44.movesexecutor(testmix44)
testcube44.moves.clear()

print('Testmix44: BR`L`B`F2BRL`UL2B`F`B2F2BL`RL2R`U2RLR`D2B2')
cubesolve(testcube44)
if testifsolved(testcube44): pass
else: failedlist.append(str(44))
print('\n')

'Testmix45: B`LU2D2U`R`B`D`RB2LULB2R`L2BRD2U2L2RU`F`B2'
testmix45 = ['B`', 'L', 'U2', 'D2', 'U`', 'R`', 'B`', 'D`', 'R', 'B2', 'L', 'U', 'L', 'B2', 'R`', 'L2', 'B', 'R', 'D2', 'U2', 'L2', 'R', 'U`', 'F`', 'B2']
Front45= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back45= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up45= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down45= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left45= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right45= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist45 = Facelist(F=Front45,B=Back45,U=Up45,D=Down45,L=Left45,R=Right45)
testcube45 = cubestate(Facelist45)
testcube45.movesexecutor(testmix45)
testcube45.moves.clear()

print('Testmix45: B`LU2D2U`R`B`D`RB2LULB2R`L2BRD2U2L2RU`F`B2')
cubesolve(testcube45)
if testifsolved(testcube45): pass
else: failedlist.append(str(45))
print('\n')

'Testmix46: UF`DF`DU2R`LB`FL2U`LF`U`RB`L2FU`LF`U2FB2'
testmix46 = ['U', 'F`', 'D', 'F`', 'D', 'U2', 'R`', 'L', 'B`', 'F', 'L2', 'U`', 'L', 'F`', 'U`', 'R', 'B`', 'L2', 'F', 'U`', 'L', 'F`', 'U2', 'F', 'B2']
Front46= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back46= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up46= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down46= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left46= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right46= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist46 = Facelist(F=Front46,B=Back46,U=Up46,D=Down46,L=Left46,R=Right46)
testcube46 = cubestate(Facelist46)
testcube46.movesexecutor(testmix46)
testcube46.moves.clear()

print('Testmix46: UF`DF`DU2R`LB`FL2U`LF`U`RB`L2FU`LF`U2FB2')
cubesolve(testcube46)
if testifsolved(testcube46): pass
else: failedlist.append(str(46))
print('\n')

'Testmix47: F2UR2B2L2B2R`B`R2D`BR`U2FL`R`B`R2DUL2RU2L`B2'
testmix47 = ['F2', 'U', 'R2', 'B2', 'L2', 'B2', 'R`', 'B`', 'R2', 'D`', 'B', 'R`', 'U2', 'F', 'L`', 'R`', 'B`', 'R2', 'D', 'U', 'L2', 'R', 'U2', 'L`', 'B2']
Front47= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back47= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up47= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down47= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left47= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right47= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist47 = Facelist(F=Front47,B=Back47,U=Up47,D=Down47,L=Left47,R=Right47)
testcube47 = cubestate(Facelist47)
testcube47.movesexecutor(testmix47)
testcube47.moves.clear()

print('Testmix47: F2UR2B2L2B2R`B`R2D`BR`U2FL`R`B`R2DUL2RU2L`B2')
cubesolve(testcube47)
if testifsolved(testcube47): pass
else: failedlist.append(str(47))
print('\n')

'Testmix48: L2U2L2F2L2F2B`FU`FU2F2DF`DUDB2R`U`L2R`L`BF2'
testmix48 = ['L2', 'U2', 'L2', 'F2', 'L2', 'F2', 'B`', 'F', 'U`', 'F', 'U2', 'F2', 'D', 'F`', 'D', 'U', 'D', 'B2', 'R`', 'U`', 'L2', 'R`', 'L`', 'B', 'F2']
Front48= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back48= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up48= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down48= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left48= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right48= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist48 = Facelist(F=Front48,B=Back48,U=Up48,D=Down48,L=Left48,R=Right48)
testcube48 = cubestate(Facelist48)
testcube48.movesexecutor(testmix48)
testcube48.moves.clear()

print('Testmix48: L2U2L2F2L2F2B`FU`FU2F2DF`DUDB2R`U`L2R`L`BF2')
cubesolve(testcube48)
if testifsolved(testcube48): pass
else: failedlist.append(str(48))
print('\n')

'Testmix49: D2UR`L2U2R`UD2F2B2R2UD`R`BFDR`L2FU`DB2R2U'
testmix49 = ['D2', 'U', 'R`', 'L2', 'U2', 'R`', 'U', 'D2', 'F2', 'B2', 'R2', 'U', 'D`', 'R`', 'B', 'F', 'D', 'R`', 'L2', 'F', 'U`', 'D', 'B2', 'R2', 'U']
Front49= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back49= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up49= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down49= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left49= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right49= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist49 = Facelist(F=Front49,B=Back49,U=Up49,D=Down49,L=Left49,R=Right49)
testcube49 = cubestate(Facelist49)
testcube49.movesexecutor(testmix49)
testcube49.moves.clear()

print('Testmix49: D2UR`L2U2R`UD2F2B2R2UD`R`BFDR`L2FU`DB2R2U')
cubesolve(testcube49)
if testifsolved(testcube49): pass
else: failedlist.append(str(49))
print('\n')

'Testmix50: B2F`L2BDUL2U2F`L2RB`R`DU`F2B`DR2DB2D2F2D2F'
testmix50 = ['B2', 'F`', 'L2', 'B', 'D', 'U', 'L2', 'U2', 'F`', 'L2', 'R', 'B`', 'R`', 'D', 'U`', 'F2', 'B`', 'D', 'R2', 'D', 'B2', 'D2', 'F2', 'D2', 'F']
Front50= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back50= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up50= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down50= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left50= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right50= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist50 = Facelist(F=Front50,B=Back50,U=Up50,D=Down50,L=Left50,R=Right50)
testcube50 = cubestate(Facelist50)
testcube50.movesexecutor(testmix50)
testcube50.moves.clear()

print('Testmix50: B2F`L2BDUL2U2F`L2RB`R`DU`F2B`DR2DB2D2F2D2F')
cubesolve(testcube50)
if testifsolved(testcube50): pass
else: failedlist.append(str(50))
print('\n')

'Testmix51: F`U`L2R`DU2R2B`L2RD`B2FB`F2U2R2U`L`U`F2L2F`D2F'
testmix51 = ['F`', 'U`', 'L2', 'R`', 'D', 'U2', 'R2', 'B`', 'L2', 'R', 'D`', 'B2', 'F', 'B`', 'F2', 'U2', 'R2', 'U`', 'L`', 'U`', 'F2', 'L2', 'F`', 'D2', 'F']
Front51= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back51= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up51= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down51= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left51= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right51= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist51 = Facelist(F=Front51,B=Back51,U=Up51,D=Down51,L=Left51,R=Right51)
testcube51 = cubestate(Facelist51)
testcube51.movesexecutor(testmix51)
testcube51.moves.clear()

print('Testmix51: F`U`L2R`DU2R2B`L2RD`B2FB`F2U2R2U`L`U`F2L2F`D2F')
cubesolve(testcube51)
if testifsolved(testcube51): pass
else: failedlist.append(str(51))
print('\n')

'Testmix52: B2RUDR2BR`U`L2BF2UD2ULUF2L2B`L`B2F2L`B2D'
testmix52 = ['B2', 'R', 'U', 'D', 'R2', 'B', 'R`', 'U`', 'L2', 'B', 'F2', 'U', 'D2', 'U', 'L', 'U', 'F2', 'L2', 'B`', 'L`', 'B2', 'F2', 'L`', 'B2', 'D']
Front52= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back52= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up52= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down52= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left52= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right52= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist52 = Facelist(F=Front52,B=Back52,U=Up52,D=Down52,L=Left52,R=Right52)
testcube52 = cubestate(Facelist52)
testcube52.movesexecutor(testmix52)
testcube52.moves.clear()

print('Testmix52: B2RUDR2BR`U`L2BF2UD2ULUF2L2B`L`B2F2L`B2D')
cubesolve(testcube52)
if testifsolved(testcube52): pass
else: failedlist.append(str(52))
print('\n')

'Testmix53: B2L2U2D`U2D2U2L`FB2L2RBLFU2RB`D`RD2R`L`BL`'
testmix53 = ['B2', 'L2', 'U2', 'D`', 'U2', 'D2', 'U2', 'L`', 'F', 'B2', 'L2', 'R', 'B', 'L', 'F', 'U2', 'R', 'B`', 'D`', 'R', 'D2', 'R`', 'L`', 'B', 'L`']
Front53= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back53= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up53= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down53= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left53= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right53= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist53 = Facelist(F=Front53,B=Back53,U=Up53,D=Down53,L=Left53,R=Right53)
testcube53 = cubestate(Facelist53)
testcube53.movesexecutor(testmix53)
testcube53.moves.clear()

print('Testmix53: B2L2U2D`U2D2U2L`FB2L2RBLFU2RB`D`RD2R`L`BL`')
cubesolve(testcube53)
if testifsolved(testcube53): pass
else: failedlist.append(str(53))
print('\n')

'Testmix54: F2B2RL2U2RL2RL`U`RB`RDR2LB`R`BD2U`F`UD`F`'
testmix54 = ['F2', 'B2', 'R', 'L2', 'U2', 'R', 'L2', 'R', 'L`', 'U`', 'R', 'B`', 'R', 'D', 'R2', 'L', 'B`', 'R`', 'B', 'D2', 'U`', 'F`', 'U', 'D`', 'F`']
Front54= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back54= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up54= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down54= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left54= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right54= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist54 = Facelist(F=Front54,B=Back54,U=Up54,D=Down54,L=Left54,R=Right54)
testcube54 = cubestate(Facelist54)
testcube54.movesexecutor(testmix54)
testcube54.moves.clear()

print('Testmix54: F2B2RL2U2RL2RL`U`RB`RDR2LB`R`BD2U`F`UD`F`')
cubesolve(testcube54)
if testifsolved(testcube54): pass
else: failedlist.append(str(54))
print('\n')

'Testmix55: B2RB2D2B2L2BL2U`D`U`F`B2FDU`L2UR`U`R2B`F`BF2'
testmix55 = ['B2', 'R', 'B2', 'D2', 'B2', 'L2', 'B', 'L2', 'U`', 'D`', 'U`', 'F`', 'B2', 'F', 'D', 'U`', 'L2', 'U', 'R`', 'U`', 'R2', 'B`', 'F`', 'B', 'F2']
Front55= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back55= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up55= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down55= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left55= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right55= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist55 = Facelist(F=Front55,B=Back55,U=Up55,D=Down55,L=Left55,R=Right55)
testcube55 = cubestate(Facelist55)
testcube55.movesexecutor(testmix55)
testcube55.moves.clear()

print('Testmix55: B2RB2D2B2L2BL2U`D`U`F`B2FDU`L2UR`U`R2B`F`BF2')
cubesolve(testcube55)
if testifsolved(testcube55): pass
else: failedlist.append(str(55))
print('\n')

'Testmix56: RD`BR`L2R`U2R2D`BF`DFD2RL`ULR`D2B2D2RLR`'
testmix56 = ['R', 'D`', 'B', 'R`', 'L2', 'R`', 'U2', 'R2', 'D`', 'B', 'F`', 'D', 'F', 'D2', 'R', 'L`', 'U', 'L', 'R`', 'D2', 'B2', 'D2', 'R', 'L', 'R`']
Front56= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back56= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up56= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down56= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left56= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right56= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist56 = Facelist(F=Front56,B=Back56,U=Up56,D=Down56,L=Left56,R=Right56)
testcube56 = cubestate(Facelist56)
testcube56.movesexecutor(testmix56)
testcube56.moves.clear()

print('Testmix56: RD`BR`L2R`U2R2D`BF`DFD2RL`ULR`D2B2D2RLR`')
cubesolve(testcube56)
if testifsolved(testcube56): pass
else: failedlist.append(str(56))
print('\n')

'Testmix57: F`D2B`D`B2L`UL2B2R2U`D`UR`B2R2U`FU2F`U2F2URL'
testmix57 = ['F`', 'D2', 'B`', 'D`', 'B2', 'L`', 'U', 'L2', 'B2', 'R2', 'U`', 'D`', 'U', 'R`', 'B2', 'R2', 'U`', 'F', 'U2', 'F`', 'U2', 'F2', 'U', 'R', 'L']
Front57= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back57= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up57= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down57= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left57= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right57= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist57 = Facelist(F=Front57,B=Back57,U=Up57,D=Down57,L=Left57,R=Right57)
testcube57 = cubestate(Facelist57)
testcube57.movesexecutor(testmix57)
testcube57.moves.clear()

print('Testmix57: F`D2B`D`B2L`UL2B2R2U`D`UR`B2R2U`FU2F`U2F2URL')
cubesolve(testcube57)
if testifsolved(testcube57): pass
else: failedlist.append(str(57))
print('\n')

'Testmix58: R2B2RD2R`D`B`L2B`L2R2D`UFLB2L`B`F2B`D2BRUR`'
testmix58 = ['R2', 'B2', 'R', 'D2', 'R`', 'D`', 'B`', 'L2', 'B`', 'L2', 'R2', 'D`', 'U', 'F', 'L', 'B2', 'L`', 'B`', 'F2', 'B`', 'D2', 'B', 'R', 'U', 'R`']
Front58= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back58= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up58= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down58= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left58= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right58= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist58 = Facelist(F=Front58,B=Back58,U=Up58,D=Down58,L=Left58,R=Right58)
testcube58 = cubestate(Facelist58)
testcube58.movesexecutor(testmix58)
testcube58.moves.clear()

print('Testmix58: R2B2RD2R`D`B`L2B`L2R2D`UFLB2L`B`F2B`D2BRUR`')
cubesolve(testcube58)
if testifsolved(testcube58): pass
else: failedlist.append(str(58))
print('\n')

'Testmix59: RL2F`D`R`B2L`B`L`B2R2BF`LF2L`U`R`DURD2RL`B`'
testmix59 = ['R', 'L2', 'F`', 'D`', 'R`', 'B2', 'L`', 'B`', 'L`', 'B2', 'R2', 'B', 'F`', 'L', 'F2', 'L`', 'U`', 'R`', 'D', 'U', 'R', 'D2', 'R', 'L`', 'B`']
Front59= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back59= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up59= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down59= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left59= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right59= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist59 = Facelist(F=Front59,B=Back59,U=Up59,D=Down59,L=Left59,R=Right59)
testcube59 = cubestate(Facelist59)
testcube59.movesexecutor(testmix59)
testcube59.moves.clear()

print('Testmix59: RL2F`D`R`B2L`B`L`B2R2BF`LF2L`U`R`DURD2RL`B`')
cubesolve(testcube59)
if testifsolved(testcube59): pass
else: failedlist.append(str(59))
print('\n')

'Testmix60: LB`F`D2R2L`BRU2L`F2U2F`LR2U2D2U`F`URD2B`LB'
testmix60 = ['L', 'B`', 'F`', 'D2', 'R2', 'L`', 'B', 'R', 'U2', 'L`', 'F2', 'U2', 'F`', 'L', 'R2', 'U2', 'D2', 'U`', 'F`', 'U', 'R', 'D2', 'B`', 'L', 'B']
Front60= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back60= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up60= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down60= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left60= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right60= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist60 = Facelist(F=Front60,B=Back60,U=Up60,D=Down60,L=Left60,R=Right60)
testcube60 = cubestate(Facelist60)
testcube60.movesexecutor(testmix60)
testcube60.moves.clear()

print('Testmix60: LB`F`D2R2L`BRU2L`F2U2F`LR2U2D2U`F`URD2B`LB')
cubesolve(testcube60)
if testifsolved(testcube60): pass
else: failedlist.append(str(60))
print('\n')

'Testmix61: DR2B2L`B`D2B2RL2U2F2U`D2RLFU2R`UFU2F2U2LU`'
testmix61 = ['D', 'R2', 'B2', 'L`', 'B`', 'D2', 'B2', 'R', 'L2', 'U2', 'F2', 'U`', 'D2', 'R', 'L', 'F', 'U2', 'R`', 'U', 'F', 'U2', 'F2', 'U2', 'L', 'U`']
Front61= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back61= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up61= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down61= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left61= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right61= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist61 = Facelist(F=Front61,B=Back61,U=Up61,D=Down61,L=Left61,R=Right61)
testcube61 = cubestate(Facelist61)
testcube61.movesexecutor(testmix61)
testcube61.moves.clear()

print('Testmix61: DR2B2L`B`D2B2RL2U2F2U`D2RLFU2R`UFU2F2U2LU`')
cubesolve(testcube61)
if testifsolved(testcube61): pass
else: failedlist.append(str(61))
print('\n')

'Testmix62: LFD`U2RDR2BR2U`LUR2LB`LF`L`RUL`B2L`F`L2'
testmix62 = ['L', 'F', 'D`', 'U2', 'R', 'D', 'R2', 'B', 'R2', 'U`', 'L', 'U', 'R2', 'L', 'B`', 'L', 'F`', 'L`', 'R', 'U', 'L`', 'B2', 'L`', 'F`', 'L2']
Front62= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back62= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up62= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down62= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left62= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right62= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist62 = Facelist(F=Front62,B=Back62,U=Up62,D=Down62,L=Left62,R=Right62)
testcube62 = cubestate(Facelist62)
testcube62.movesexecutor(testmix62)
testcube62.moves.clear()

print('Testmix62: LFD`U2RDR2BR2U`LUR2LB`LF`L`RUL`B2L`F`L2')
cubesolve(testcube62)
if testifsolved(testcube62): pass
else: failedlist.append(str(62))
print('\n')

'Testmix63: DU`L`BL`R`U`RBR2UF`DUL`BLF2B2F2B`R`L`R2L2'
testmix63 = ['D', 'U`', 'L`', 'B', 'L`', 'R`', 'U`', 'R', 'B', 'R2', 'U', 'F`', 'D', 'U', 'L`', 'B', 'L', 'F2', 'B2', 'F2', 'B`', 'R`', 'L`', 'R2', 'L2']
Front63= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back63= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up63= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down63= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left63= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right63= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist63 = Facelist(F=Front63,B=Back63,U=Up63,D=Down63,L=Left63,R=Right63)
testcube63 = cubestate(Facelist63)
testcube63.movesexecutor(testmix63)
testcube63.moves.clear()

print('Testmix63: DU`L`BL`R`U`RBR2UF`DUL`BLF2B2F2B`R`L`R2L2')
cubesolve(testcube63)
if testifsolved(testcube63): pass
else: failedlist.append(str(63))
print('\n')

'Testmix64: LU`L2FLF2U2L2RUFULB2R2B`D`RU`RB`D`FDU'
testmix64 = ['L', 'U`', 'L2', 'F', 'L', 'F2', 'U2', 'L2', 'R', 'U', 'F', 'U', 'L', 'B2', 'R2', 'B`', 'D`', 'R', 'U`', 'R', 'B`', 'D`', 'F', 'D', 'U']
Front64= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back64= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up64= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down64= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left64= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right64= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist64 = Facelist(F=Front64,B=Back64,U=Up64,D=Down64,L=Left64,R=Right64)
testcube64 = cubestate(Facelist64)
testcube64.movesexecutor(testmix64)
testcube64.moves.clear()

print('Testmix64: LU`L2FLF2U2L2RUFULB2R2B`D`RU`RB`D`FDU')
cubesolve(testcube64)
if testifsolved(testcube64): pass
else: failedlist.append(str(64))
print('\n')

'Testmix65: B2FD`BD2UF`BL2BD2U2L`UR2ULR2L`RULRL2F'
testmix65 = ['B2', 'F', 'D`', 'B', 'D2', 'U', 'F`', 'B', 'L2', 'B', 'D2', 'U2', 'L`', 'U', 'R2', 'U', 'L', 'R2', 'L`', 'R', 'U', 'L', 'R', 'L2', 'F']
Front65= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back65= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up65= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down65= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left65= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right65= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist65 = Facelist(F=Front65,B=Back65,U=Up65,D=Down65,L=Left65,R=Right65)
testcube65 = cubestate(Facelist65)
testcube65.movesexecutor(testmix65)
testcube65.moves.clear()

print('Testmix65: B2FD`BD2UF`BL2BD2U2L`UR2ULR2L`RULRL2F')
cubesolve(testcube65)
if testifsolved(testcube65): pass
else: failedlist.append(str(65))
print('\n')

'Testmix66: U`FB`R2DR2DB`FL2R`UF`DFL2U2LB2F`B`D`F`U`R2'
testmix66 = ['U`', 'F', 'B`', 'R2', 'D', 'R2', 'D', 'B`', 'F', 'L2', 'R`', 'U', 'F`', 'D', 'F', 'L2', 'U2', 'L', 'B2', 'F`', 'B`', 'D`', 'F`', 'U`', 'R2']
Front66= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back66= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up66= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down66= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left66= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right66= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist66 = Facelist(F=Front66,B=Back66,U=Up66,D=Down66,L=Left66,R=Right66)
testcube66 = cubestate(Facelist66)
testcube66.movesexecutor(testmix66)
testcube66.moves.clear()

print('Testmix66: U`FB`R2DR2DB`FL2R`UF`DFL2U2LB2F`B`D`F`U`R2')
cubesolve(testcube66)
if testifsolved(testcube66): pass
else: failedlist.append(str(66))
print('\n')

'Testmix67: D`B`DR`B`L`U`LFBL2BL`URL2F2D2F2U`D2B2LR`L2'
testmix67 = ['D`', 'B`', 'D', 'R`', 'B`', 'L`', 'U`', 'L', 'F', 'B', 'L2', 'B', 'L`', 'U', 'R', 'L2', 'F2', 'D2', 'F2', 'U`', 'D2', 'B2', 'L', 'R`', 'L2']
Front67= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back67= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up67= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down67= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left67= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right67= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist67 = Facelist(F=Front67,B=Back67,U=Up67,D=Down67,L=Left67,R=Right67)
testcube67 = cubestate(Facelist67)
testcube67.movesexecutor(testmix67)
testcube67.moves.clear()

print('Testmix67: D`B`DR`B`L`U`LFBL2BL`URL2F2D2F2U`D2B2LR`L2')
cubesolve(testcube67)
if testifsolved(testcube67): pass
else: failedlist.append(str(67))
print('\n')

'Testmix68: ULBLR2DFB`D2BR2BDB`R`D2B`L`U`DU`R2DB2R2'
testmix68 = ['U', 'L', 'B', 'L', 'R2', 'D', 'F', 'B`', 'D2', 'B', 'R2', 'B', 'D', 'B`', 'R`', 'D2', 'B`', 'L`', 'U`', 'D', 'U`', 'R2', 'D', 'B2', 'R2']
Front68= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back68= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up68= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down68= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left68= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right68= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist68 = Facelist(F=Front68,B=Back68,U=Up68,D=Down68,L=Left68,R=Right68)
testcube68 = cubestate(Facelist68)
testcube68.movesexecutor(testmix68)
testcube68.moves.clear()

print('Testmix68: ULBLR2DFB`D2BR2BDB`R`D2B`L`U`DU`R2DB2R2')
cubesolve(testcube68)
if testifsolved(testcube68): pass
else: failedlist.append(str(68))
print('\n')

'Testmix69: B2FD2U2F`D`F2DUR`LFDBFBRU`F`D2B`D`RB2F2'
testmix69 = ['B2', 'F', 'D2', 'U2', 'F`', 'D`', 'F2', 'D', 'U', 'R`', 'L', 'F', 'D', 'B', 'F', 'B', 'R', 'U`', 'F`', 'D2', 'B`', 'D`', 'R', 'B2', 'F2']
Front69= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back69= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up69= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down69= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left69= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right69= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist69 = Facelist(F=Front69,B=Back69,U=Up69,D=Down69,L=Left69,R=Right69)
testcube69 = cubestate(Facelist69)
testcube69.movesexecutor(testmix69)
testcube69.moves.clear()

print('Testmix69: B2FD2U2F`D`F2DUR`LFDBFBRU`F`D2B`D`RB2F2')
cubesolve(testcube69)
if testifsolved(testcube69): pass
else: failedlist.append(str(69))
print('\n')

'Testmix70: B2LFL`B2L`F2U`LR`D2F2L2FU`D`BD`UL`RUL2FL2'
testmix70 = ['B2', 'L', 'F', 'L`', 'B2', 'L`', 'F2', 'U`', 'L', 'R`', 'D2', 'F2', 'L2', 'F', 'U`', 'D`', 'B', 'D`', 'U', 'L`', 'R', 'U', 'L2', 'F', 'L2']
Front70= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back70= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up70= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down70= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left70= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right70= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist70 = Facelist(F=Front70,B=Back70,U=Up70,D=Down70,L=Left70,R=Right70)
testcube70 = cubestate(Facelist70)
testcube70.movesexecutor(testmix70)
testcube70.moves.clear()

print('Testmix70: B2LFL`B2L`F2U`LR`D2F2L2FU`D`BD`UL`RUL2FL2')
cubesolve(testcube70)
if testifsolved(testcube70): pass
else: failedlist.append(str(70))
print('\n')

'Testmix71: F`DFD2R2D2F`DBF`D2R2D`F2L`R`D2BF2BR`L`F2U2L`'
testmix71 = ['F`', 'D', 'F', 'D2', 'R2', 'D2', 'F`', 'D', 'B', 'F`', 'D2', 'R2', 'D`', 'F2', 'L`', 'R`', 'D2', 'B', 'F2', 'B', 'R`', 'L`', 'F2', 'U2', 'L`']
Front71= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back71= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up71= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down71= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left71= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right71= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist71 = Facelist(F=Front71,B=Back71,U=Up71,D=Down71,L=Left71,R=Right71)
testcube71 = cubestate(Facelist71)
testcube71.movesexecutor(testmix71)
testcube71.moves.clear()

print('Testmix71: F`DFD2R2D2F`DBF`D2R2D`F2L`R`D2BF2BR`L`F2U2L`')
cubesolve(testcube71)
if testifsolved(testcube71): pass
else: failedlist.append(str(71))
print('\n')

'Testmix72: FB2LU`DUF`B`FD2BD2UL2RL`F2U2R`B2R2DFL`R2'
testmix72 = ['F', 'B2', 'L', 'U`', 'D', 'U', 'F`', 'B`', 'F', 'D2', 'B', 'D2', 'U', 'L2', 'R', 'L`', 'F2', 'U2', 'R`', 'B2', 'R2', 'D', 'F', 'L`', 'R2']
Front72= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back72= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up72= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down72= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left72= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right72= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist72 = Facelist(F=Front72,B=Back72,U=Up72,D=Down72,L=Left72,R=Right72)
testcube72 = cubestate(Facelist72)
testcube72.movesexecutor(testmix72)
testcube72.moves.clear()

print('Testmix72: FB2LU`DUF`B`FD2BD2UL2RL`F2U2R`B2R2DFL`R2')
cubesolve(testcube72)
if testifsolved(testcube72): pass
else: failedlist.append(str(72))
print('\n')

'Testmix73: U2F2B2RLU`LUF2L2ULB2F`BR`B`RUF2U2D`F`B`R`'
testmix73 = ['U2', 'F2', 'B2', 'R', 'L', 'U`', 'L', 'U', 'F2', 'L2', 'U', 'L', 'B2', 'F`', 'B', 'R`', 'B`', 'R', 'U', 'F2', 'U2', 'D`', 'F`', 'B`', 'R`']
Front73= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back73= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up73= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down73= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left73= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right73= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist73 = Facelist(F=Front73,B=Back73,U=Up73,D=Down73,L=Left73,R=Right73)
testcube73 = cubestate(Facelist73)
testcube73.movesexecutor(testmix73)
testcube73.moves.clear()

print('Testmix73: U2F2B2RLU`LUF2L2ULB2F`BR`B`RUF2U2D`F`B`R`')
cubesolve(testcube73)
if testifsolved(testcube73): pass
else: failedlist.append(str(73))
print('\n')

'Testmix74: LR2L2U2R2B`L`RBR`LRB`F2DR`L2U2F2B2L`B2L2R2D`'
testmix74 = ['L', 'R2', 'L2', 'U2', 'R2', 'B`', 'L`', 'R', 'B', 'R`', 'L', 'R', 'B`', 'F2', 'D', 'R`', 'L2', 'U2', 'F2', 'B2', 'L`', 'B2', 'L2', 'R2', 'D`']
Front74= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back74= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up74= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down74= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left74= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right74= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist74 = Facelist(F=Front74,B=Back74,U=Up74,D=Down74,L=Left74,R=Right74)
testcube74 = cubestate(Facelist74)
testcube74.movesexecutor(testmix74)
testcube74.moves.clear()

print('Testmix74: LR2L2U2R2B`L`RBR`LRB`F2DR`L2U2F2B2L`B2L2R2D`')
cubesolve(testcube74)
if testifsolved(testcube74): pass
else: failedlist.append(str(74))
print('\n')

'Testmix75: DBFLU`LR`DF`D`RDR`U`D`FDR2D`U2D`RU2R`B`'
testmix75 = ['D', 'B', 'F', 'L', 'U`', 'L', 'R`', 'D', 'F`', 'D`', 'R', 'D', 'R`', 'U`', 'D`', 'F', 'D', 'R2', 'D`', 'U2', 'D`', 'R', 'U2', 'R`', 'B`']
Front75= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back75= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up75= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down75= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left75= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right75= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist75 = Facelist(F=Front75,B=Back75,U=Up75,D=Down75,L=Left75,R=Right75)
testcube75 = cubestate(Facelist75)
testcube75.movesexecutor(testmix75)
testcube75.moves.clear()

print('Testmix75: DBFLU`LR`DF`D`RDR`U`D`FDR2D`U2D`RU2R`B`')
cubesolve(testcube75)
if testifsolved(testcube75): pass
else: failedlist.append(str(75))
print('\n')

'Testmix76: RB`LU`D2F`UD`FU2RB`D`UL`B`R`B2L2RB`D2FLU`'
testmix76 = ['R', 'B`', 'L', 'U`', 'D2', 'F`', 'U', 'D`', 'F', 'U2', 'R', 'B`', 'D`', 'U', 'L`', 'B`', 'R`', 'B2', 'L2', 'R', 'B`', 'D2', 'F', 'L', 'U`']
Front76= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back76= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up76= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down76= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left76= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right76= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist76 = Facelist(F=Front76,B=Back76,U=Up76,D=Down76,L=Left76,R=Right76)
testcube76 = cubestate(Facelist76)
testcube76.movesexecutor(testmix76)
testcube76.moves.clear()

print('Testmix76: RB`LU`D2F`UD`FU2RB`D`UL`B`R`B2L2RB`D2FLU`')
cubesolve(testcube76)
if testifsolved(testcube76): pass
else: failedlist.append(str(76))
print('\n')

'Testmix77: B`R`L2F`B`RBDF`B2LU`R`L2FUR2BFD2U`R2D2R`D'
testmix77 = ['B`', 'R`', 'L2', 'F`', 'B`', 'R', 'B', 'D', 'F`', 'B2', 'L', 'U`', 'R`', 'L2', 'F', 'U', 'R2', 'B', 'F', 'D2', 'U`', 'R2', 'D2', 'R`', 'D']
Front77= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back77= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up77= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down77= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left77= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right77= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist77 = Facelist(F=Front77,B=Back77,U=Up77,D=Down77,L=Left77,R=Right77)
testcube77 = cubestate(Facelist77)
testcube77.movesexecutor(testmix77)
testcube77.moves.clear()

print('Testmix77: B`R`L2F`B`RBDF`B2LU`R`L2FUR2BFD2U`R2D2R`D')
cubesolve(testcube77)
if testifsolved(testcube77): pass
else: failedlist.append(str(77))
print('\n')

'Testmix78: U2F2UD`URBL`F2DFDBD`BR2B2RL2R2LBF`LB`'
testmix78 = ['U2', 'F2', 'U', 'D`', 'U', 'R', 'B', 'L`', 'F2', 'D', 'F', 'D', 'B', 'D`', 'B', 'R2', 'B2', 'R', 'L2', 'R2', 'L', 'B', 'F`', 'L', 'B`']
Front78= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back78= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up78= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down78= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left78= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right78= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist78 = Facelist(F=Front78,B=Back78,U=Up78,D=Down78,L=Left78,R=Right78)
testcube78 = cubestate(Facelist78)
testcube78.movesexecutor(testmix78)
testcube78.moves.clear()

print('Testmix78: U2F2UD`URBL`F2DFDBD`BR2B2RL2R2LBF`LB`')
cubesolve(testcube78)
if testifsolved(testcube78): pass
else: failedlist.append(str(78))
print('\n')

'Testmix79: D2F2D`B2FBD2F2L`R`D2RU`LUD2URLBDB`LUR`'
testmix79 = ['D2', 'F2', 'D`', 'B2', 'F', 'B', 'D2', 'F2', 'L`', 'R`', 'D2', 'R', 'U`', 'L', 'U', 'D2', 'U', 'R', 'L', 'B', 'D', 'B`', 'L', 'U', 'R`']
Front79= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back79= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up79= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down79= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left79= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right79= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist79 = Facelist(F=Front79,B=Back79,U=Up79,D=Down79,L=Left79,R=Right79)
testcube79 = cubestate(Facelist79)
testcube79.movesexecutor(testmix79)
testcube79.moves.clear()

print('Testmix79: D2F2D`B2FBD2F2L`R`D2RU`LUD2URLBDB`LUR`')
cubesolve(testcube79)
if testifsolved(testcube79): pass
else: failedlist.append(str(79))
print('\n')

'Testmix80: U2L`F`B2LULF`U`F2U`F`DBDFD`BF2L`U2F`D2B2L2'
testmix80 = ['U2', 'L`', 'F`', 'B2', 'L', 'U', 'L', 'F`', 'U`', 'F2', 'U`', 'F`', 'D', 'B', 'D', 'F', 'D`', 'B', 'F2', 'L`', 'U2', 'F`', 'D2', 'B2', 'L2']
Front80= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back80= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up80= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down80= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left80= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right80= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist80 = Facelist(F=Front80,B=Back80,U=Up80,D=Down80,L=Left80,R=Right80)
testcube80 = cubestate(Facelist80)
testcube80.movesexecutor(testmix80)
testcube80.moves.clear()

print('Testmix80: U2L`F`B2LULF`U`F2U`F`DBDFD`BF2L`U2F`D2B2L2')
cubesolve(testcube80)
if testifsolved(testcube80): pass
else: failedlist.append(str(80))
print('\n')

'Testmix81: U`D2BLB2F`B`R`D2FU2L`FL`F`UL`R2DR2B`R`UL`B`'
testmix81 = ['U`', 'D2', 'B', 'L', 'B2', 'F`', 'B`', 'R`', 'D2', 'F', 'U2', 'L`', 'F', 'L`', 'F`', 'U', 'L`', 'R2', 'D', 'R2', 'B`', 'R`', 'U', 'L`', 'B`']
Front81= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back81= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up81= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down81= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left81= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right81= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist81 = Facelist(F=Front81,B=Back81,U=Up81,D=Down81,L=Left81,R=Right81)
testcube81 = cubestate(Facelist81)
testcube81.movesexecutor(testmix81)
testcube81.moves.clear()

print('Testmix81: U`D2BLB2F`B`R`D2FU2L`FL`F`UL`R2DR2B`R`UL`B`')
cubesolve(testcube81)
if testifsolved(testcube81): pass
else: failedlist.append(str(81))
print('\n')

'Testmix82: F2U2RB2FL`B2R2L`B2LF2L2R`D2R2DB2LB2L`F`U2F2U2'
testmix82 = ['F2', 'U2', 'R', 'B2', 'F', 'L`', 'B2', 'R2', 'L`', 'B2', 'L', 'F2', 'L2', 'R`', 'D2', 'R2', 'D', 'B2', 'L', 'B2', 'L`', 'F`', 'U2', 'F2', 'U2']
Front82= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back82= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up82= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down82= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left82= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right82= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist82 = Facelist(F=Front82,B=Back82,U=Up82,D=Down82,L=Left82,R=Right82)
testcube82 = cubestate(Facelist82)
testcube82.movesexecutor(testmix82)
testcube82.moves.clear()

print('Testmix82: F2U2RB2FL`B2R2L`B2LF2L2R`D2R2DB2LB2L`F`U2F2U2')
cubesolve(testcube82)
if testifsolved(testcube82): pass
else: failedlist.append(str(82))
print('\n')

'Testmix83: UL`F`LR`B`L2U`DB`RURL2R2L2BL`FD`R`UL`UR`'
testmix83 = ['U', 'L`', 'F`', 'L', 'R`', 'B`', 'L2', 'U`', 'D', 'B`', 'R', 'U', 'R', 'L2', 'R2', 'L2', 'B', 'L`', 'F', 'D`', 'R`', 'U', 'L`', 'U', 'R`']
Front83= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back83= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up83= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down83= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left83= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right83= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist83 = Facelist(F=Front83,B=Back83,U=Up83,D=Down83,L=Left83,R=Right83)
testcube83 = cubestate(Facelist83)
testcube83.movesexecutor(testmix83)
testcube83.moves.clear()

print('Testmix83: UL`F`LR`B`L2U`DB`RURL2R2L2BL`FD`R`UL`UR`')
cubesolve(testcube83)
if testifsolved(testcube83): pass
else: failedlist.append(str(83))
print('\n')

'Testmix84: U`R`U2F2D2FB2LU`LUR2D2F2URUR2U2F`BF`UR2L'
testmix84 = ['U`', 'R`', 'U2', 'F2', 'D2', 'F', 'B2', 'L', 'U`', 'L', 'U', 'R2', 'D2', 'F2', 'U', 'R', 'U', 'R2', 'U2', 'F`', 'B', 'F`', 'U', 'R2', 'L']
Front84= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back84= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up84= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down84= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left84= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right84= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist84 = Facelist(F=Front84,B=Back84,U=Up84,D=Down84,L=Left84,R=Right84)
testcube84 = cubestate(Facelist84)
testcube84.movesexecutor(testmix84)
testcube84.moves.clear()

print('Testmix84: U`R`U2F2D2FB2LU`LUR2D2F2URUR2U2F`BF`UR2L')
cubesolve(testcube84)
if testifsolved(testcube84): pass
else: failedlist.append(str(84))
print('\n')

'Testmix85: D`BRU`L`B`F2U`L2F2B`RDB2D2B2LB`D`B2R`B`RD2R`'
testmix85 = ['D`', 'B', 'R', 'U`', 'L`', 'B`', 'F2', 'U`', 'L2', 'F2', 'B`', 'R', 'D', 'B2', 'D2', 'B2', 'L', 'B`', 'D`', 'B2', 'R`', 'B`', 'R', 'D2', 'R`']
Front85= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back85= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up85= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down85= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left85= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right85= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist85 = Facelist(F=Front85,B=Back85,U=Up85,D=Down85,L=Left85,R=Right85)
testcube85 = cubestate(Facelist85)
testcube85.movesexecutor(testmix85)
testcube85.moves.clear()

print('Testmix85: D`BRU`L`B`F2U`L2F2B`RDB2D2B2LB`D`B2R`B`RD2R`')
cubesolve(testcube85)
if testifsolved(testcube85): pass
else: failedlist.append(str(85))
print('\n')

'Testmix86: U2FL`RUFU`L2U`LU2F2BF2B`FU`R`L`R`D2B`R2DU2'
testmix86 = ['U2', 'F', 'L`', 'R', 'U', 'F', 'U`', 'L2', 'U`', 'L', 'U2', 'F2', 'B', 'F2', 'B`', 'F', 'U`', 'R`', 'L`', 'R`', 'D2', 'B`', 'R2', 'D', 'U2']
Front86= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back86= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up86= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down86= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left86= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right86= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist86 = Facelist(F=Front86,B=Back86,U=Up86,D=Down86,L=Left86,R=Right86)
testcube86 = cubestate(Facelist86)
testcube86.movesexecutor(testmix86)
testcube86.moves.clear()

print('Testmix86: U2FL`RUFU`L2U`LU2F2BF2B`FU`R`L`R`D2B`R2DU2')
cubesolve(testcube86)
if testifsolved(testcube86): pass
else: failedlist.append(str(86))
print('\n')

'Testmix87: FD2F2U2RU2DBFU2F`B`LB2F2D`RUR`U`D2RL`R2L2'
testmix87 = ['F', 'D2', 'F2', 'U2', 'R', 'U2', 'D', 'B', 'F', 'U2', 'F`', 'B`', 'L', 'B2', 'F2', 'D`', 'R', 'U', 'R`', 'U`', 'D2', 'R', 'L`', 'R2', 'L2']
Front87= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back87= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up87= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down87= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left87= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right87= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist87 = Facelist(F=Front87,B=Back87,U=Up87,D=Down87,L=Left87,R=Right87)
testcube87 = cubestate(Facelist87)
testcube87.movesexecutor(testmix87)
testcube87.moves.clear()

print('Testmix87: FD2F2U2RU2DBFU2F`B`LB2F2D`RUR`U`D2RL`R2L2')
cubesolve(testcube87)
if testifsolved(testcube87): pass
else: failedlist.append(str(87))
print('\n')

'Testmix88: URL2B2L2UD`U`FBR2U`F2LFL`U`RD2U2F`L2FBD`'
testmix88 = ['U', 'R', 'L2', 'B2', 'L2', 'U', 'D`', 'U`', 'F', 'B', 'R2', 'U`', 'F2', 'L', 'F', 'L`', 'U`', 'R', 'D2', 'U2', 'F`', 'L2', 'F', 'B', 'D`']
Front88= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back88= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up88= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down88= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left88= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right88= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist88 = Facelist(F=Front88,B=Back88,U=Up88,D=Down88,L=Left88,R=Right88)
testcube88 = cubestate(Facelist88)
testcube88.movesexecutor(testmix88)
testcube88.moves.clear()

print('Testmix88: URL2B2L2UD`U`FBR2U`F2LFL`U`RD2U2F`L2FBD`')
cubesolve(testcube88)
if testifsolved(testcube88): pass
else: failedlist.append(str(88))
print('\n')

'Testmix89: B2LF2L`B`F`B2DB`LU2R`D2R`DF2UL2F`L2F2U`DFD`'
testmix89 = ['B2', 'L', 'F2', 'L`', 'B`', 'F`', 'B2', 'D', 'B`', 'L', 'U2', 'R`', 'D2', 'R`', 'D', 'F2', 'U', 'L2', 'F`', 'L2', 'F2', 'U`', 'D', 'F', 'D`']
Front89= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back89= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up89= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down89= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left89= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right89= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist89 = Facelist(F=Front89,B=Back89,U=Up89,D=Down89,L=Left89,R=Right89)
testcube89 = cubestate(Facelist89)
testcube89.movesexecutor(testmix89)
testcube89.moves.clear()

print('Testmix89: B2LF2L`B`F`B2DB`LU2R`D2R`DF2UL2F`L2F2U`DFD`')
cubesolve(testcube89)
if testifsolved(testcube89): pass
else: failedlist.append(str(89))
print('\n')

'Testmix90: R2U2DU`DUL`U`R`UD`R`D`F2DF`LR2BF2L2F`B2L`U'
testmix90 = ['R2', 'U2', 'D', 'U`', 'D', 'U', 'L`', 'U`', 'R`', 'U', 'D`', 'R`', 'D`', 'F2', 'D', 'F`', 'L', 'R2', 'B', 'F2', 'L2', 'F`', 'B2', 'L`', 'U']
Front90= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back90= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up90= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down90= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left90= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right90= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist90 = Facelist(F=Front90,B=Back90,U=Up90,D=Down90,L=Left90,R=Right90)
testcube90 = cubestate(Facelist90)
testcube90.movesexecutor(testmix90)
testcube90.moves.clear()

print('Testmix90: R2U2DU`DUL`U`R`UD`R`D`F2DF`LR2BF2L2F`B2L`U')
cubesolve(testcube90)
if testifsolved(testcube90): pass
else: failedlist.append(str(90))
print('\n')

'Testmix91: F`UR2B`L`F2DB`R`B2R`D2F2D2B2D2UD2RUD`BDR`U2'
testmix91 = ['F`', 'U', 'R2', 'B`', 'L`', 'F2', 'D', 'B`', 'R`', 'B2', 'R`', 'D2', 'F2', 'D2', 'B2', 'D2', 'U', 'D2', 'R', 'U', 'D`', 'B', 'D', 'R`', 'U2']
Front91= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back91= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up91= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down91= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left91= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right91= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist91 = Facelist(F=Front91,B=Back91,U=Up91,D=Down91,L=Left91,R=Right91)
testcube91 = cubestate(Facelist91)
testcube91.movesexecutor(testmix91)
testcube91.moves.clear()

print('Testmix91: F`UR2B`L`F2DB`R`B2R`D2F2D2B2D2UD2RUD`BDR`U2')
cubesolve(testcube91)
if testifsolved(testcube91): pass
else: failedlist.append(str(91))
print('\n')

'Testmix92: F`D2F`L2B`LU2RBLR`L`BD`U2D2B2L2R2U2R2L2U`R`L'
testmix92 = ['F`', 'D2', 'F`', 'L2', 'B`', 'L', 'U2', 'R', 'B', 'L', 'R`', 'L`', 'B', 'D`', 'U2', 'D2', 'B2', 'L2', 'R2', 'U2', 'R2', 'L2', 'U`', 'R`', 'L']
Front92= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back92= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up92= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down92= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left92= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right92= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist92 = Facelist(F=Front92,B=Back92,U=Up92,D=Down92,L=Left92,R=Right92)
testcube92 = cubestate(Facelist92)
testcube92.movesexecutor(testmix92)
testcube92.moves.clear()

print('Testmix92: F`D2F`L2B`LU2RBLR`L`BD`U2D2B2L2R2U2R2L2U`R`L')
cubesolve(testcube92)
if testifsolved(testcube92): pass
else: failedlist.append(str(92))
print('\n')

'Testmix93: U`D2FL`B`D`U`R`B2LR2D2B`L2F2LB2D2BL2UD`B2R`L'
testmix93 = ['U`', 'D2', 'F', 'L`', 'B`', 'D`', 'U`', 'R`', 'B2', 'L', 'R2', 'D2', 'B`', 'L2', 'F2', 'L', 'B2', 'D2', 'B', 'L2', 'U', 'D`', 'B2', 'R`', 'L']
Front93= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back93= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up93= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down93= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left93= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right93= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist93 = Facelist(F=Front93,B=Back93,U=Up93,D=Down93,L=Left93,R=Right93)
testcube93 = cubestate(Facelist93)
testcube93.movesexecutor(testmix93)
testcube93.moves.clear()

print('Testmix93: U`D2FL`B`D`U`R`B2LR2D2B`L2F2LB2D2BL2UD`B2R`L')
cubesolve(testcube93)
if testifsolved(testcube93): pass
else: failedlist.append(str(93))
print('\n')

'Testmix94: B`L`B`F2LFD`F`LF`L`BLF2D`R2UD2BL`RB`F`U`L2'
testmix94 = ['B`', 'L`', 'B`', 'F2', 'L', 'F', 'D`', 'F`', 'L', 'F`', 'L`', 'B', 'L', 'F2', 'D`', 'R2', 'U', 'D2', 'B', 'L`', 'R', 'B`', 'F`', 'U`', 'L2']
Front94= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back94= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up94= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down94= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left94= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right94= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist94 = Facelist(F=Front94,B=Back94,U=Up94,D=Down94,L=Left94,R=Right94)
testcube94 = cubestate(Facelist94)
testcube94.movesexecutor(testmix94)
testcube94.moves.clear()

print('Testmix94: B`L`B`F2LFD`F`LF`L`BLF2D`R2UD2BL`RB`F`U`L2')
cubesolve(testcube94)
if testifsolved(testcube94): pass
else: failedlist.append(str(94))
print('\n')

'Testmix95: R2L2U2D2B2F`U`L2F2D2BL2UF2DBR2U`R2U2LU`LR2L`'
testmix95 = ['R2', 'L2', 'U2', 'D2', 'B2', 'F`', 'U`', 'L2', 'F2', 'D2', 'B', 'L2', 'U', 'F2', 'D', 'B', 'R2', 'U`', 'R2', 'U2', 'L', 'U`', 'L', 'R2', 'L`']
Front95= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back95= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up95= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down95= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left95= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right95= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist95 = Facelist(F=Front95,B=Back95,U=Up95,D=Down95,L=Left95,R=Right95)
testcube95 = cubestate(Facelist95)
testcube95.movesexecutor(testmix95)
testcube95.moves.clear()

print('Testmix95: R2L2U2D2B2F`U`L2F2D2BL2UF2DBR2U`R2U2LU`LR2L`')
cubesolve(testcube95)
if testifsolved(testcube95): pass
else: failedlist.append(str(95))
print('\n')

'Testmix96: D2UD2R`U2L2R2L2F`B`RL`F2D2F2U2D`B2D2B`R2B`F`L2U'
testmix96 = ['D2', 'U', 'D2', 'R`', 'U2', 'L2', 'R2', 'L2', 'F`', 'B`', 'R', 'L`', 'F2', 'D2', 'F2', 'U2', 'D`', 'B2', 'D2', 'B`', 'R2', 'B`', 'F`', 'L2', 'U']
Front96= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back96= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up96= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down96= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left96= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right96= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist96 = Facelist(F=Front96,B=Back96,U=Up96,D=Down96,L=Left96,R=Right96)
testcube96 = cubestate(Facelist96)
testcube96.movesexecutor(testmix96)
testcube96.moves.clear()

print('Testmix96: D2UD2R`U2L2R2L2F`B`RL`F2D2F2U2D`B2D2B`R2B`F`L2U')
cubesolve(testcube96)
if testifsolved(testcube96): pass
else: failedlist.append(str(96))
print('\n')

'Testmix97: D2B2L2F`B`L2BR`U2F2D2B`L2B`DF`UF`UL`RUR2D2U`'
testmix97 = ['D2', 'B2', 'L2', 'F`', 'B`', 'L2', 'B', 'R`', 'U2', 'F2', 'D2', 'B`', 'L2', 'B`', 'D', 'F`', 'U', 'F`', 'U', 'L`', 'R', 'U', 'R2', 'D2', 'U`']
Front97= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back97= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up97= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down97= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left97= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right97= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist97 = Facelist(F=Front97,B=Back97,U=Up97,D=Down97,L=Left97,R=Right97)
testcube97 = cubestate(Facelist97)
testcube97.movesexecutor(testmix97)
testcube97.moves.clear()

print('Testmix97: D2B2L2F`B`L2BR`U2F2D2B`L2B`DF`UF`UL`RUR2D2U`')
cubesolve(testcube97)
if testifsolved(testcube97): pass
else: failedlist.append(str(97))
print('\n')

'Testmix98: D`B2FB`DF2L`R`DF`U`L2F`DF2B2FDF`BDR`U`D2B2'
testmix98 = ['D`', 'B2', 'F', 'B`', 'D', 'F2', 'L`', 'R`', 'D', 'F`', 'U`', 'L2', 'F`', 'D', 'F2', 'B2', 'F', 'D', 'F`', 'B', 'D', 'R`', 'U`', 'D2', 'B2']
Front98= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back98= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up98= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down98= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left98= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right98= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist98 = Facelist(F=Front98,B=Back98,U=Up98,D=Down98,L=Left98,R=Right98)
testcube98 = cubestate(Facelist98)
testcube98.movesexecutor(testmix98)
testcube98.moves.clear()

print('Testmix98: D`B2FB`DF2L`R`DF`U`L2F`DF2B2FDF`BDR`U`D2B2')
cubesolve(testcube98)
if testifsolved(testcube98): pass
else: failedlist.append(str(98))
print('\n')

'Testmix99: D2B`F`L`FL2U`FU`R`U`F2U2D2R`L`BFU2R`L2UF2D2B`'
testmix99 = ['D2', 'B`', 'F`', 'L`', 'F', 'L2', 'U`', 'F', 'U`', 'R`', 'U`', 'F2', 'U2', 'D2', 'R`', 'L`', 'B', 'F', 'U2', 'R`', 'L2', 'U', 'F2', 'D2', 'B`']
Front99= Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back99= Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up99= Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down99= Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left99= Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right99= Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist99 = Facelist(F=Front99,B=Back99,U=Up99,D=Down99,L=Left99,R=Right99)
testcube99 = cubestate(Facelist99)
testcube99.movesexecutor(testmix99)
testcube99.moves.clear()

print('Testmix99: D2B`F`L`FL2U`FU`R`U`F2U2D2R`L`BFU2R`L2UF2D2B`')
cubesolve(testcube99)
if testifsolved(testcube99): pass
else: failedlist.append(str(99))
print('\n')

print(failedlist)