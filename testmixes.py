# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:45:57 2019

@author: sanka
"""

import collections
import cubefunctions
import whitecross_2
import F2L_corneredgepair
import last_layer
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
            
            

def movesexecutor(cube, moves):
    while len(moves) != 0:
        A = moves.pop(0)
        if A == 'U':
            cube.Uturn()
        elif A == 'U`':
            cube.Uprimeturn()
        elif A == 'U2':
            cube.U2turn()
        elif A == 'D':
            cube.Dturn()
        elif A == 'D`':
            cube.Dprimeturn()
        elif A == 'D2':
            cube.D2turn()
        elif A == 'F':
            cube.Fturn()
        elif A == 'F`':
            cube.Fprimeturn()
        elif A == 'F2':
            cube.F2turn()
        elif A == 'B':
            cube.Bturn()
        elif A == 'B`':
            cube.Bprimeturn()
        elif A == 'B2':
            cube.B2turn()
        elif A == 'R':
            cube.Rturn()
        elif A == 'R`':
            cube.Rprimeturn()
        elif A == 'R2':
            cube.R2turn()
        elif A == 'L':
            cube.Lturn()
        elif A == 'L`':
            cube.Lprimeturn()
        elif A == 'L2':
            cube.L2turn()
        elif A == 'x`':
            cube.FtoDturn()
        elif A == 'x':
            cube.FtoUturn()
        elif A == 'y':
            cube.FtoLturn()
        elif A == 'y`':
            cube.FtoRturn()
        else:
            print('Invalid move!')

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
            print("F face unsolved!")
            solved = False
        else:
            continue
    for i in cube.B:
        if i != cube.B.mm:
            print("B face unsolved!")
            solved = False
        else:
            continue
    for i in cube.U:
        if i != cube.U.mm:
            print("U face unsolved!")
            solved = False
        else:
            continue
    for i in cube.D:
        if i != cube.D.mm:
            print("D face unsolved!")
            solved = False
        else:
            continue
    for i in cube.L:
        if i != cube.L.mm:
            print("L face unsolved!")
            solved = False
        else:
            continue
    for i in cube.R:
        if i != cube.R.mm:
            print("R face unsolved!")
            solved = False
        else:
            continue
    if solved:
        print("Solution checks out!")
    else:
        print("Solution failed!")

"Testmix 0:"

Front0 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back0 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up0 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down0 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left0 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right0 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist0 = Facelist(F=Front0,B=Back0,U=Up0,D=Down0,L=Left0,R=Right0)
testcube0 = cubestate(Facelist0)

"Testmix 1: F'U'L'F'RF2R2UB'R'L'D'BR'B'F'LDU2R'U'FBLF2"

Front1 = Front(ul='o',um='o',ur='y',ml='y',mm='w',mr='w',dl='g',dm='g',dr='g')
Back1 = Back(ul='w',um='o',ur='y',ml='o',mm='y',mr='r',dl='o',dm='g',dr='b')
Up1 = Up(fl='b',fm='g',fr='o',ml='o',mm='b',mr='y',bl='b',bm='y',br='b')
Down1 = Down(fl='r',fm='r',fr='r',ml='y',mm='g',mr='w',bl='g',bm='w',br='w')
Left1 = Left(fu='y',fm='g',fd='y',mu='w',mm='o',md='r',bu='r',bm='b',bd='w')
Right1 = Right(fu='g',fm='b',fd='w',mu='b',mm='r',md='r',bu='r',bm='b',bd='o')
Facelist1 = Facelist(F=Front1,B=Back1,U=Up1,D=Down1,L=Left1,R=Right1)
testcube1 = cubestate(Facelist1)

"Testmix2: FRL'D'U2R'D'R'D'BD'B2RL'U'L2U'BL'R2UBF2R'B"

Front2 = Front(ul='w',um='w',ur='b',ml='y',mm='w',mr='y',dl='g',dm='o',dr='g')
Back2 = Back(ul='r',um='g',ur='w',ml='o',mm='y',mr='b',dl='g',dm='b',dr='y')
Up2 = Up(fl='g',fm='r',fr='r',ml='r',mm='b',mr='w',bl='b',bm='o',br='b')
Down2 = Down(fl='y',fm='w',fr='w',ml='y',mm='g',mr='g',bl='y',bm='w',br='b')
Left2 = Left(fu='r',fm='o',fd='o',mu='y',mm='o',md='b',bu='y',bm='b',bd='r')
Right2 = Right(fu='w',fm='g',fd='o',mu='g',mm='r',md='r',bu='o',bm='r',bd='o')
Facelist2 = Facelist(F=Front2,B=Back2,U=Up2,D=Down2,L=Left2,R=Right2)
testcube2 = cubestate(Facelist2)

"Testmix3: B'L'BR2LD'L2R'B2F2UB'F2DBF'RLD2F2U2DFB2L"

Front3 = Front(ul='y',um='w',ur='o',ml='o',mm='w',mr='w',dl='w',dm='b',dr='g')
Back3 = Back(ul='o',um='b',ur='w',ml='g',mm='y',mr='o',dl='r',dm='y',dr='w')
Up3 = Up(fl='g',fm='r',fr='y',ml='g',mm='b',mr='o',bl='w',bm='w',br='g')
Down3 = Down(fl='b',fm='r',fr='y',ml='y',mm='g',mr='r',bl='y',bm='b',br='o')
Left3 = Left(fu='o',fm='y',fd='r',mu='o',mm='o',md='r',bu='g',bm='y',bd='b')
Right3 = Right(fu='b',fm='g',fd='r',mu='b',mm='r',md='g',bu='r',bm='w',bd='b')
Facelist3 = Facelist(F=Front3,B=Back3,U=Up3,D=Down3,L=Left3,R=Right3)
testcube3 = cubestate(Facelist3)

"Testmix4: D'L2B'U'D2LF'B2DU2F'UB'FD2R'F'U'RLF'BLB'R'"

Front4 = Front(ul='y',um='g',ur='g',ml='o',mm='w',mr='g',dl='o',dm='b',dr='w')
Back4 = Back(ul='b',um='r',ur='r',ml='w',mm='y',mr='b',dl='b',dm='o',dr='y')
Up4 = Up(fl='o',fm='o',fr='o',ml='b',mm='b',mr='w',bl='r',bm='g',br='w')
Down4 = Down(fl='g',fm='y',fr='b',ml='y',mm='g',mr='w',bl='r',bm='y',br='g')
Left4 = Left(fu='b',fm='b',fd='y',mu='w',mm='o',md='r',bu='w',bm='o',bd='y')
Right4 = Right(fu='w',fm='y',fd='o',mu='r',mm='r',md='g',bu='g',bm='r',bd='r')
Facelist4 = Facelist(F=Front4,B=Back4,U=Up4,D=Down4,L=Left4,R=Right4)
testcube4 = cubestate(Facelist4)

"Testmix5: BL2BR2D'B2LDRF2B'R'B'DFLU2D2L2BL2U'R'D'L2"

Front5 = Front(ul='r',um='b',ur='o',ml='r',mm='w',mr='o',dl='o',dm='y',dr='b')
Back5 = Back(ul='g',um='r',ur='y',ml='b',mm='y',mr='y',dl='w',dm='w',dr='g')
Up5 = Up(fl='y',fm='o',fr='b',ml='g',mm='b',mr='y',bl='y',bm='g',br='r')
Down5 = Down(fl='w',fm='b',fr='y',ml='w',mm='g',mr='r',bl='r',bm='b',br='w')
Left5 = Left(fu='b',fm='y',fd='g',mu='o',mm='o',md='g',bu='o',bm='r',bd='b')
Right5 = Right(fu='w',fm='w',fd='o',mu='o',mm='r',md='w',bu='g',bm='g',bd='r')
Facelist5 = Facelist(F=Front5,B=Back5,U=Up5,D=Down5,L=Left5,R=Right5)
testcube5 = cubestate(Facelist5)

"Testmix6: B2UL'FLDUB'RDUB'FU2BUB'U'B'U'BR2UR2U2"
mix6F = "wwwbgwrrr"
mix6B = "ryobbbywb"
mix6U = "bggywowgb"
mix6D = "ygwoyogoy"
mix6L = "owgrobbyo"
mix6R = "orggryyrr"
  
Front6 = Front(ul=mix6F[0],um=mix6F[1],ur=mix6F[2],ml=mix6F[3],mm=mix6F[4],mr=mix6F[5],dl=mix6F[6],dm=mix6F[7],dr=mix6F[8])
Back6 = Back(ul=mix6B[0],um=mix6B[1],ur=mix6B[2],ml=mix6B[3],mm=mix6B[4],mr=mix6B[5],dl=mix6B[6],dm=mix6B[7],dr=mix6B[8])
Up6 = Up(fl=mix6U[0],fm=mix6U[1],fr=mix6U[2],ml=mix6U[3],mm=mix6U[4],mr=mix6U[5],bl=mix6U[6],bm=mix6U[7],br=mix6U[8])
Down6 = Down(fl=mix6D[0],fm=mix6D[1],fr=mix6D[2],ml=mix6D[3],mm=mix6D[4],mr=mix6D[5],bl=mix6D[6],bm=mix6D[7],br=mix6D[8])
Left6 = Left(fu=mix6L[0],fm=mix6L[1],fd=mix6L[2],mu=mix6L[3],mm=mix6L[4],md=mix6L[5],bu=mix6L[6],bm=mix6L[7],bd=mix6L[8])
Right6 = Right(fu=mix6R[0],fm=mix6R[1],fd=mix6R[2],mu=mix6R[3],mm=mix6R[4],md=mix6R[5],bu=mix6R[6],bm=mix6R[7],bd=mix6R[8])
Facelist6 = Facelist(F=Front6,B=Back6,U=Up6,D=Down6,L=Left6,R=Right6)
testcube6 = cubestate(Facelist6)


"Testmix7: F'B'D2L'R2D'RL2D'U'B2F2UF'LBU2R2L2U2L'B'L'F2D2"
mix7F = "bobwggybb"
mix7B = "bbybbywww"
mix7U = "rgrgwgwyg"
mix7D = "gryyywoor"
mix7L = "ybrwoooog"
mix7R = "wyorrrorg"

Front7 = Front(ul=mix7F[0],um=mix7F[1],ur=mix7F[2],ml=mix7F[3],mm=mix7F[4],mr=mix7F[5],dl=mix7F[6],dm=mix7F[7],dr=mix7F[8])
Back7 = Back(ul=mix7B[0],um=mix7B[1],ur=mix7B[2],ml=mix7B[3],mm=mix7B[4],mr=mix7B[5],dl=mix7B[6],dm=mix7B[7],dr=mix7B[8])
Up7 = Up(fl=mix7U[0],fm=mix7U[1],fr=mix7U[2],ml=mix7U[3],mm=mix7U[4],mr=mix7U[5],bl=mix7U[6],bm=mix7U[7],br=mix7U[8])
Down7 = Down(fl=mix7D[0],fm=mix7D[1],fr=mix7D[2],ml=mix7D[3],mm=mix7D[4],mr=mix7D[5],bl=mix7D[6],bm=mix7D[7],br=mix7D[8])
Left7 = Left(fu=mix7L[0],fm=mix7L[1],fd=mix7L[2],mu=mix7L[3],mm=mix7L[4],md=mix7L[5],bu=mix7L[6],bm=mix7L[7],bd=mix7L[8])
Right7 = Right(fu=mix7R[0],fm=mix7R[1],fd=mix7R[2],mu=mix7R[3],mm=mix7R[4],md=mix7R[5],bu=mix7R[6],bm=mix7R[7],bd=mix7R[8])
Facelist7 = Facelist(F=Front7,B=Back7,U=Up7,D=Down7,L=Left7,R=Right7)
testcube7 = cubestate(Facelist7)

"Testmix8: B2F'RUL2D2R'U2R'B2FD'U2R2U2L'DRF'U2D2R2D'U'R'"
mix8F = "bwwbgoowr"
mix8B = "yoggbyowb"
mix8U = "ygbbwrgbo"
mix8D = "wbwwyrwoy"
mix8L = "orgyorryb"
mix8R = "rggyrgyor"

Front8 = Front(ul=mix8F[0],um=mix8F[1],ur=mix8F[2],ml=mix8F[3],mm=mix8F[4],mr=mix8F[5],dl=mix8F[6],dm=mix8F[7],dr=mix8F[8])
Back8 = Back(ul=mix8B[0],um=mix8B[1],ur=mix8B[2],ml=mix8B[3],mm=mix8B[4],mr=mix8B[5],dl=mix8B[6],dm=mix8B[7],dr=mix8B[8])
Up8 = Up(fl=mix8U[0],fm=mix8U[1],fr=mix8U[2],ml=mix8U[3],mm=mix8U[4],mr=mix8U[5],bl=mix8U[6],bm=mix8U[7],br=mix8U[8])
Down8 = Down(fl=mix8D[0],fm=mix8D[1],fr=mix8D[2],ml=mix8D[3],mm=mix8D[4],mr=mix8D[5],bl=mix8D[6],bm=mix8D[7],br=mix8D[8])
Left8 = Left(fu=mix8L[0],fm=mix8L[1],fd=mix8L[2],mu=mix8L[3],mm=mix8L[4],md=mix8L[5],bu=mix8L[6],bm=mix8L[7],bd=mix8L[8])
Right8 = Right(fu=mix8R[0],fm=mix8R[1],fd=mix8R[2],mu=mix8R[3],mm=mix8R[4],md=mix8R[5],bu=mix8R[6],bm=mix8R[7],bd=mix8R[8])
Facelist8 = Facelist(F=Front8,B=Back8,U=Up8,D=Down8,L=Left8,R=Right8)
testcube8 = cubestate(Facelist8)

"Testmix9: D'UL2UD'L2R2F2L'U2B'F2L'R2UD2RL2BU'D2B2L'B2F"
mix9F = "rwwbgrwgy"
mix9B = "oyyobybgb"
mix9U = "yrrywwwbr"
mix9D = "bwggyworo"
mix9L = "borooyggw"
mix9R = "gboorbgry"

Front9 = Front(ul=mix9F[0],um=mix9F[1],ur=mix9F[2],ml=mix9F[3],mm=mix9F[4],mr=mix9F[5],dl=mix9F[6],dm=mix9F[7],dr=mix9F[8])
Back9 = Back(ul=mix9B[0],um=mix9B[1],ur=mix9B[2],ml=mix9B[3],mm=mix9B[4],mr=mix9B[5],dl=mix9B[6],dm=mix9B[7],dr=mix9B[8])
Up9 = Up(fl=mix9U[0],fm=mix9U[1],fr=mix9U[2],ml=mix9U[3],mm=mix9U[4],mr=mix9U[5],bl=mix9U[6],bm=mix9U[7],br=mix9U[8])
Down9 = Down(fl=mix9D[0],fm=mix9D[1],fr=mix9D[2],ml=mix9D[3],mm=mix9D[4],mr=mix9D[5],bl=mix9D[6],bm=mix9D[7],br=mix9D[8])
Left9 = Left(fu=mix9L[0],fm=mix9L[1],fd=mix9L[2],mu=mix9L[3],mm=mix9L[4],md=mix9L[5],bu=mix9L[6],bm=mix9L[7],bd=mix9L[8])
Right9 = Right(fu=mix9R[0],fm=mix9R[1],fd=mix9R[2],mu=mix9R[3],mm=mix9R[4],md=mix9R[5],bu=mix9R[6],bm=mix9R[7],bd=mix9R[8])
Facelist9 = Facelist(F=Front9,B=Back9,U=Up9,D=Down9,L=Left9,R=Right9)
testcube9 = cubestate(Facelist9)

"Testmix10: R'BR'BUR'L'BD'F2R'F'RL2U2F'L2RBD2R2F2ULR2"
mix10F = "gbgrgbwyb"
mix10B = "yorybryog"
mix10U = "oyrbwgrgb"
mix10D = "goorygoww"
mix10L = "ywoooybgb"
mix10R = "ywwwrrwbr"

Front10 = Front(ul=mix10F[0],um=mix10F[1],ur=mix10F[2],ml=mix10F[3],mm=mix10F[4],mr=mix10F[5],dl=mix10F[6],dm=mix10F[7],dr=mix10F[8])
Back10 = Back(ul=mix10B[0],um=mix10B[1],ur=mix10B[2],ml=mix10B[3],mm=mix10B[4],mr=mix10B[5],dl=mix10B[6],dm=mix10B[7],dr=mix10B[8])
Up10 = Up(fl=mix10U[0],fm=mix10U[1],fr=mix10U[2],ml=mix10U[3],mm=mix10U[4],mr=mix10U[5],bl=mix10U[6],bm=mix10U[7],br=mix10U[8])
Down10 = Down(fl=mix10D[0],fm=mix10D[1],fr=mix10D[2],ml=mix10D[3],mm=mix10D[4],mr=mix10D[5],bl=mix10D[6],bm=mix10D[7],br=mix10D[8])
Left10 = Left(fu=mix10L[0],fm=mix10L[1],fd=mix10L[2],mu=mix10L[3],mm=mix10L[4],md=mix10L[5],bu=mix10L[6],bm=mix10L[7],bd=mix10L[8])
Right10 = Right(fu=mix10R[0],fm=mix10R[1],fd=mix10R[2],mu=mix10R[3],mm=mix10R[4],md=mix10R[5],bu=mix10R[6],bm=mix10R[7],bd=mix10R[8])
Facelist10 = Facelist(F=Front10,B=Back10,U=Up10,D=Down10,L=Left10,R=Right10)
testcube10 = cubestate(Facelist10)

"Testmix11: LU2RU'B'U'F2D'L'D2U'R'D2L2U'D2L'R2D'R'B'L2R2D2U'"
mix11F = "woygggybo"
mix11B = "byrobwbrr"
mix11U = "ogorwwrbw"
mix11D = "rrwyyoyyy"
mix11L = "gwbwogwbo"
mix11R = "grborygbg"

Front11 = Front(ul=mix11F[0],um=mix11F[1],ur=mix11F[2],ml=mix11F[3],mm=mix11F[4],mr=mix11F[5],dl=mix11F[6],dm=mix11F[7],dr=mix11F[8])
Back11 = Back(ul=mix11B[0],um=mix11B[1],ur=mix11B[2],ml=mix11B[3],mm=mix11B[4],mr=mix11B[5],dl=mix11B[6],dm=mix11B[7],dr=mix11B[8])
Up11 = Up(fl=mix11U[0],fm=mix11U[1],fr=mix11U[2],ml=mix11U[3],mm=mix11U[4],mr=mix11U[5],bl=mix11U[6],bm=mix11U[7],br=mix11U[8])
Down11 = Down(fl=mix11D[0],fm=mix11D[1],fr=mix11D[2],ml=mix11D[3],mm=mix11D[4],mr=mix11D[5],bl=mix11D[6],bm=mix11D[7],br=mix11D[8])
Left11 = Left(fu=mix11L[0],fm=mix11L[1],fd=mix11L[2],mu=mix11L[3],mm=mix11L[4],md=mix11L[5],bu=mix11L[6],bm=mix11L[7],bd=mix11L[8])
Right11 = Right(fu=mix11R[0],fm=mix11R[1],fd=mix11R[2],mu=mix11R[3],mm=mix11R[4],md=mix11R[5],bu=mix11R[6],bm=mix11R[7],bd=mix11R[8])
Facelist11 = Facelist(F=Front11,B=Back11,U=Up11,D=Down11,L=Left11,R=Right11)
testcube11 = cubestate(Facelist11)

"Testmix12: U'L2U'B2U'BFL'BD2F'BRD'U2F2U'DB2L2RD2U2RL"
mix12F = "wgobgwwyb"
mix12B = "bbygbygwg"
mix12U = "ooyowryyr"
mix12D = "ogwyygrby"
mix12L = "gobwoorww"
mix12R = "brrbrrgro"

Front12 = Front(ul=mix12F[0],um=mix12F[1],ur=mix12F[2],ml=mix12F[3],mm=mix12F[4],mr=mix12F[5],dl=mix12F[6],dm=mix12F[7],dr=mix12F[8])
Back12 = Back(ul=mix12B[0],um=mix12B[1],ur=mix12B[2],ml=mix12B[3],mm=mix12B[4],mr=mix12B[5],dl=mix12B[6],dm=mix12B[7],dr=mix12B[8])
Up12 = Up(fl=mix12U[0],fm=mix12U[1],fr=mix12U[2],ml=mix12U[3],mm=mix12U[4],mr=mix12U[5],bl=mix12U[6],bm=mix12U[7],br=mix12U[8])
Down12 = Down(fl=mix12D[0],fm=mix12D[1],fr=mix12D[2],ml=mix12D[3],mm=mix12D[4],mr=mix12D[5],bl=mix12D[6],bm=mix12D[7],br=mix12D[8])
Left12 = Left(fu=mix12L[0],fm=mix12L[1],fd=mix12L[2],mu=mix12L[3],mm=mix12L[4],md=mix12L[5],bu=mix12L[6],bm=mix12L[7],bd=mix12L[8])
Right12 = Right(fu=mix12R[0],fm=mix12R[1],fd=mix12R[2],mu=mix12R[3],mm=mix12R[4],md=mix12R[5],bu=mix12R[6],bm=mix12R[7],bd=mix12R[8])
Facelist12 = Facelist(F=Front12,B=Back12,U=Up12,D=Down12,L=Left12,R=Right12)
testcube12 = cubestate(Facelist12)

"Testmix13: D2F'U'F'L2U'BL'DL'UDF'UB'U'B'L'DU2F'DR'U2L"
mix13F = "rgwbgbyry"
mix13B = "wrogborwy"
mix13U = "gorowrowg"
mix13D = "bybgyyboo"
mix13L = "ywobowbrw"
mix13R = "gyrbrgwyg"

Front13 = Front(ul=mix13F[0],um=mix13F[1],ur=mix13F[2],ml=mix13F[3],mm=mix13F[4],mr=mix13F[5],dl=mix13F[6],dm=mix13F[7],dr=mix13F[8])
Back13 = Back(ul=mix13B[0],um=mix13B[1],ur=mix13B[2],ml=mix13B[3],mm=mix13B[4],mr=mix13B[5],dl=mix13B[6],dm=mix13B[7],dr=mix13B[8])
Up13 = Up(fl=mix13U[0],fm=mix13U[1],fr=mix13U[2],ml=mix13U[3],mm=mix13U[4],mr=mix13U[5],bl=mix13U[6],bm=mix13U[7],br=mix13U[8])
Down13 = Down(fl=mix13D[0],fm=mix13D[1],fr=mix13D[2],ml=mix13D[3],mm=mix13D[4],mr=mix13D[5],bl=mix13D[6],bm=mix13D[7],br=mix13D[8])
Left13 = Left(fu=mix13L[0],fm=mix13L[1],fd=mix13L[2],mu=mix13L[3],mm=mix13L[4],md=mix13L[5],bu=mix13L[6],bm=mix13L[7],bd=mix13L[8])
Right13 = Right(fu=mix13R[0],fm=mix13R[1],fd=mix13R[2],mu=mix13R[3],mm=mix13R[4],md=mix13R[5],bu=mix13R[6],bm=mix13R[7],bd=mix13R[8])
Facelist13 = Facelist(F=Front13,B=Back13,U=Up13,D=Down13,L=Left13,R=Right13)
testcube13 = cubestate(Facelist13)

"Testmix14: F2DL2D2BU2BU2F'DB'U'R'D2LU2R2BUD'R'LDB2F2"
mix14F = "ygwggwgbb"
mix14B = "bbwybrgry"
mix14U = "gybbwgyog"
mix14D = "owooyoybb"
mix14L = "oowyoyrrr"
mix14R = "rrwwrwrgo"

Front14 = Front(ul=mix14F[0],um=mix14F[1],ur=mix14F[2],ml=mix14F[3],mm=mix14F[4],mr=mix14F[5],dl=mix14F[6],dm=mix14F[7],dr=mix14F[8])
Back14 = Back(ul=mix14B[0],um=mix14B[1],ur=mix14B[2],ml=mix14B[3],mm=mix14B[4],mr=mix14B[5],dl=mix14B[6],dm=mix14B[7],dr=mix14B[8])
Up14 = Up(fl=mix14U[0],fm=mix14U[1],fr=mix14U[2],ml=mix14U[3],mm=mix14U[4],mr=mix14U[5],bl=mix14U[6],bm=mix14U[7],br=mix14U[8])
Down14 = Down(fl=mix14D[0],fm=mix14D[1],fr=mix14D[2],ml=mix14D[3],mm=mix14D[4],mr=mix14D[5],bl=mix14D[6],bm=mix14D[7],br=mix14D[8])
Left14 = Left(fu=mix14L[0],fm=mix14L[1],fd=mix14L[2],mu=mix14L[3],mm=mix14L[4],md=mix14L[5],bu=mix14L[6],bm=mix14L[7],bd=mix14L[8])
Right14 = Right(fu=mix14R[0],fm=mix14R[1],fd=mix14R[2],mu=mix14R[3],mm=mix14R[4],md=mix14R[5],bu=mix14R[6],bm=mix14R[7],bd=mix14R[8])
Facelist14 = Facelist(F=Front14,B=Back14,U=Up14,D=Down14,L=Left14,R=Right14)
testcube14 = cubestate(Facelist14)

"Testmix15: B2L2U2R2L2BF2DUL2R'B2U'B2L'B2UR'UDL'R2BD2F'"
mix15F = "rgrogyowo"
mix15B = "rbwbbgwoo"
mix15U = "yogywwywb"
mix15D = "wobgyyrbg"
mix15L = "byggowgrb"
mix15R = "wryrrbory"

Front15 = Front(ul=mix15F[0],um=mix15F[1],ur=mix15F[2],ml=mix15F[3],mm=mix15F[4],mr=mix15F[5],dl=mix15F[6],dm=mix15F[7],dr=mix15F[8])
Back15 = Back(ul=mix15B[0],um=mix15B[1],ur=mix15B[2],ml=mix15B[3],mm=mix15B[4],mr=mix15B[5],dl=mix15B[6],dm=mix15B[7],dr=mix15B[8])
Up15 = Up(fl=mix15U[0],fm=mix15U[1],fr=mix15U[2],ml=mix15U[3],mm=mix15U[4],mr=mix15U[5],bl=mix15U[6],bm=mix15U[7],br=mix15U[8])
Down15 = Down(fl=mix15D[0],fm=mix15D[1],fr=mix15D[2],ml=mix15D[3],mm=mix15D[4],mr=mix15D[5],bl=mix15D[6],bm=mix15D[7],br=mix15D[8])
Left15 = Left(fu=mix15L[0],fm=mix15L[1],fd=mix15L[2],mu=mix15L[3],mm=mix15L[4],md=mix15L[5],bu=mix15L[6],bm=mix15L[7],bd=mix15L[8])
Right15 = Right(fu=mix15R[0],fm=mix15R[1],fd=mix15R[2],mu=mix15R[3],mm=mix15R[4],md=mix15R[5],bu=mix15R[6],bm=mix15R[7],bd=mix15R[8])
Facelist15 = Facelist(F=Front15,B=Back15,U=Up15,D=Down15,L=Left15,R=Right15)
testcube15 = cubestate(Facelist15)

"Testmix16: L2F2B2DR2FD2F2B'R'DL2BDURL2BD2LR2FLUL2"
mix16F = "rrgbgyygb"
mix16B = "oobbbwwoy"
mix16U = "wyogwwgwr"
mix16D = "grwgywbyb"
mix16L = "grrooyyoo"
mix16R = "wbrbrgyro"

Front16 = Front(ul=mix16F[0],um=mix16F[1],ur=mix16F[2],ml=mix16F[3],mm=mix16F[4],mr=mix16F[5],dl=mix16F[6],dm=mix16F[7],dr=mix16F[8])
Back16 = Back(ul=mix16B[0],um=mix16B[1],ur=mix16B[2],ml=mix16B[3],mm=mix16B[4],mr=mix16B[5],dl=mix16B[6],dm=mix16B[7],dr=mix16B[8])
Up16 = Up(fl=mix16U[0],fm=mix16U[1],fr=mix16U[2],ml=mix16U[3],mm=mix16U[4],mr=mix16U[5],bl=mix16U[6],bm=mix16U[7],br=mix16U[8])
Down16 = Down(fl=mix16D[0],fm=mix16D[1],fr=mix16D[2],ml=mix16D[3],mm=mix16D[4],mr=mix16D[5],bl=mix16D[6],bm=mix16D[7],br=mix16D[8])
Left16 = Left(fu=mix16L[0],fm=mix16L[1],fd=mix16L[2],mu=mix16L[3],mm=mix16L[4],md=mix16L[5],bu=mix16L[6],bm=mix16L[7],bd=mix16L[8])
Right16 = Right(fu=mix16R[0],fm=mix16R[1],fd=mix16R[2],mu=mix16R[3],mm=mix16R[4],md=mix16R[5],bu=mix16R[6],bm=mix16R[7],bd=mix16R[8])
Facelist16 = Facelist(F=Front16,B=Back16,U=Up16,D=Down16,L=Left16,R=Right16)
testcube16 = cubestate(Facelist16)

"Testmix17: F'L2BD'U'B'RF'L2D2L'F2U'R'B2D2FDU2L'BF2RD'"
mix17F = "wwwwgbwog"
mix17B = "boyrbrybb"
mix17U = "rrrywgwgr"
mix17D = "gyowygoyy"
mix17L = "boogoboyb"
mix17R = "goywrrgbr"

Front17 = Front(ul=mix17F[0],um=mix17F[1],ur=mix17F[2],ml=mix17F[3],mm=mix17F[4],mr=mix17F[5],dl=mix17F[6],dm=mix17F[7],dr=mix17F[8])
Back17 = Back(ul=mix17B[0],um=mix17B[1],ur=mix17B[2],ml=mix17B[3],mm=mix17B[4],mr=mix17B[5],dl=mix17B[6],dm=mix17B[7],dr=mix17B[8])
Up17 = Up(fl=mix17U[0],fm=mix17U[1],fr=mix17U[2],ml=mix17U[3],mm=mix17U[4],mr=mix17U[5],bl=mix17U[6],bm=mix17U[7],br=mix17U[8])
Down17 = Down(fl=mix17D[0],fm=mix17D[1],fr=mix17D[2],ml=mix17D[3],mm=mix17D[4],mr=mix17D[5],bl=mix17D[6],bm=mix17D[7],br=mix17D[8])
Left17 = Left(fu=mix17L[0],fm=mix17L[1],fd=mix17L[2],mu=mix17L[3],mm=mix17L[4],md=mix17L[5],bu=mix17L[6],bm=mix17L[7],bd=mix17L[8])
Right17 = Right(fu=mix17R[0],fm=mix17R[1],fd=mix17R[2],mu=mix17R[3],mm=mix17R[4],md=mix17R[5],bu=mix17R[6],bm=mix17R[7],bd=mix17R[8])
Facelist17 = Facelist(F=Front17,B=Back17,U=Up17,D=Down17,L=Left17,R=Right17)
testcube17 = cubestate(Facelist17)

"Testmix18: FRU2B2R'U'RU2R'D'L2DF'DU'B2D2B'U'F'B2D2FD2L'"
mix18F = "rwgrgoboy"
mix18B = "wgyrbobbb"
mix18U = "ggwywrgyg"
mix18D = "wboryorwr"
mix18L = "ywoboyoby"
mix18R = "rwbgrgoyw"

Front18 = Front(ul=mix18F[0],um=mix18F[1],ur=mix18F[2],ml=mix18F[3],mm=mix18F[4],mr=mix18F[5],dl=mix18F[6],dm=mix18F[7],dr=mix18F[8])
Back18 = Back(ul=mix18B[0],um=mix18B[1],ur=mix18B[2],ml=mix18B[3],mm=mix18B[4],mr=mix18B[5],dl=mix18B[6],dm=mix18B[7],dr=mix18B[8])
Up18 = Up(fl=mix18U[0],fm=mix18U[1],fr=mix18U[2],ml=mix18U[3],mm=mix18U[4],mr=mix18U[5],bl=mix18U[6],bm=mix18U[7],br=mix18U[8])
Down18 = Down(fl=mix18D[0],fm=mix18D[1],fr=mix18D[2],ml=mix18D[3],mm=mix18D[4],mr=mix18D[5],bl=mix18D[6],bm=mix18D[7],br=mix18D[8])
Left18 = Left(fu=mix18L[0],fm=mix18L[1],fd=mix18L[2],mu=mix18L[3],mm=mix18L[4],md=mix18L[5],bu=mix18L[6],bm=mix18L[7],bd=mix18L[8])
Right18 = Right(fu=mix18R[0],fm=mix18R[1],fd=mix18R[2],mu=mix18R[3],mm=mix18R[4],md=mix18R[5],bu=mix18R[6],bm=mix18R[7],bd=mix18R[8])
Facelist18 = Facelist(F=Front18,B=Back18,U=Up18,D=Down18,L=Left18,R=Right18)
testcube18 = cubestate(Facelist18)

"Testmix19: FD2B2RB'U'LD'RFB'D2U'F'DB2UBD2R2UL2R'U2B2"
mix19F = "yoryggbwb"
mix19B = "wrwybwrrg"
mix19U = "bwyowbrgo"
mix19D = "ogobyobwy"
mix19L = "rrygorgbw"
mix19R = "gyworygbo"

Front19 = Front(ul=mix19F[0],um=mix19F[1],ur=mix19F[2],ml=mix19F[3],mm=mix19F[4],mr=mix19F[5],dl=mix19F[6],dm=mix19F[7],dr=mix19F[8])
Back19 = Back(ul=mix19B[0],um=mix19B[1],ur=mix19B[2],ml=mix19B[3],mm=mix19B[4],mr=mix19B[5],dl=mix19B[6],dm=mix19B[7],dr=mix19B[8])
Up19 = Up(fl=mix19U[0],fm=mix19U[1],fr=mix19U[2],ml=mix19U[3],mm=mix19U[4],mr=mix19U[5],bl=mix19U[6],bm=mix19U[7],br=mix19U[8])
Down19 = Down(fl=mix19D[0],fm=mix19D[1],fr=mix19D[2],ml=mix19D[3],mm=mix19D[4],mr=mix19D[5],bl=mix19D[6],bm=mix19D[7],br=mix19D[8])
Left19 = Left(fu=mix19L[0],fm=mix19L[1],fd=mix19L[2],mu=mix19L[3],mm=mix19L[4],md=mix19L[5],bu=mix19L[6],bm=mix19L[7],bd=mix19L[8])
Right19 = Right(fu=mix19R[0],fm=mix19R[1],fd=mix19R[2],mu=mix19R[3],mm=mix19R[4],md=mix19R[5],bu=mix19R[6],bm=mix19R[7],bd=mix19R[8])
Facelist19 = Facelist(F=Front19,B=Back19,U=Up19,D=Down19,L=Left19,R=Right19)
testcube19 = cubestate(Facelist19)

"Testmix20: DR'B'R2L2UR'D2R2UB2F2R'F'L2F2LR'B'FD2F'R'L'D2"
mix20F = "obgogwbgo"
mix20B = "bgoyboyyr"
mix20U = "grwbworrb"
mix20D = "yowryggby"
mix20L = "wbrwoywgo"
mix20R = "rrbyrwywg"

Front20 = Front(ul=mix20F[0],um=mix20F[1],ur=mix20F[2],ml=mix20F[3],mm=mix20F[4],mr=mix20F[5],dl=mix20F[6],dm=mix20F[7],dr=mix20F[8])
Back20 = Back(ul=mix20B[0],um=mix20B[1],ur=mix20B[2],ml=mix20B[3],mm=mix20B[4],mr=mix20B[5],dl=mix20B[6],dm=mix20B[7],dr=mix20B[8])
Up20 = Up(fl=mix20U[0],fm=mix20U[1],fr=mix20U[2],ml=mix20U[3],mm=mix20U[4],mr=mix20U[5],bl=mix20U[6],bm=mix20U[7],br=mix20U[8])
Down20 = Down(fl=mix20D[0],fm=mix20D[1],fr=mix20D[2],ml=mix20D[3],mm=mix20D[4],mr=mix20D[5],bl=mix20D[6],bm=mix20D[7],br=mix20D[8])
Left20 = Left(fu=mix20L[0],fm=mix20L[1],fd=mix20L[2],mu=mix20L[3],mm=mix20L[4],md=mix20L[5],bu=mix20L[6],bm=mix20L[7],bd=mix20L[8])
Right20 = Right(fu=mix20R[0],fm=mix20R[1],fd=mix20R[2],mu=mix20R[3],mm=mix20R[4],md=mix20R[5],bu=mix20R[6],bm=mix20R[7],bd=mix20R[8])
Facelist20 = Facelist(F=Front20,B=Back20,U=Up20,D=Down20,L=Left20,R=Right20)
testcube20 = cubestate(Facelist20)

"Testmix21: F'L'DRU'L2UB2FU'B2U2LBR'U2L2DUFR'U'L'DF"
testmix21 = ['F`','L`','D','R','U`','L2','U','B2','F','U`','B2','U2','L2','D','U','F','R`','U`','L`','D','F']
Front21 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back21 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up21 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down21 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left21 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right21 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist21 = Facelist(F=Front21,B=Back21,U=Up21,D=Down21,L=Left21,R=Right21)
testcube21 = cubestate(Facelist21)
movesexecutor(testcube21, testmix21)
testcube21.moves.clear()

"Testmix22: R2B`RBF`UL2R`DF`D`F`L`D2R`D2B2RBR`U`BF`DU"
testmix22 = ['R2', 'B`', 'R', 'B', 'F`', 'U', 'L2', 'R`', 'D', 'F`', 'D`', 'F`', 'L`', 'D2', 'R`', 'D2', 'B2', 'R', 'B', 'R`', 'U`', 'B', 'F`', 'D', 'U']
Front22 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back22 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up22 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down22 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left22 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right22 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist22 = Facelist(F=Front22,B=Back22,U=Up22,D=Down22,L=Left22,R=Right22)
testcube22 = cubestate(Facelist22)
movesexecutor(testcube22, testmix22)
testcube22.moves.clear()

"Testmix23: FB2F2R`BRLFU`D`B2F`RF`D`UB2U`LF2RB2UL`U"
testmix23 = ['F', 'B2', 'F2', 'R`', 'B', 'R', 'L', 'F', 'U`', 'D`', 'B2', 'F`', 'R', 'F`', 'D`', 'U', 'B2', 'U`', 'L', 'F2', 'R', 'B2', 'U', 'L`', 'U']
Front23 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back23 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up23 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down23 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left23 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right23 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist23 = Facelist(F=Front23,B=Back23,U=Up23,D=Down23,L=Left23,R=Right23)
testcube23 = cubestate(Facelist23)
movesexecutor(testcube23, testmix23)
testcube23.moves.clear()

"Testmix24: D2RLRUFLR2LF`B2L`R`LB2D2LR2UBF`L2R2L2R`"
testmix24 = ['D2', 'R', 'L', 'R', 'U', 'F', 'L', 'R2', 'L', 'F`', 'B2', 'L`', 'R`', 'L', 'B2', 'D2', 'L', 'R2', 'U', 'B', 'F`', 'L2', 'R2', 'L2', 'R`']
Front24 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back24 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up24 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down24 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left24 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right24 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist24 = Facelist(F=Front24,B=Back24,U=Up24,D=Down24,L=Left24,R=Right24)
testcube24 = cubestate(Facelist24)
movesexecutor(testcube24, testmix24)
testcube24.moves.clear()

"Testmix25: U2RB2R2D2F2BLFDB2LFD2R2BU`LD`FU2B`UL2U"
testmix25 = ['U2', 'R', 'B2', 'R2', 'D2', 'F2', 'B', 'L', 'F', 'D', 'B2', 'L', 'F', 'D2', 'R2', 'B', 'U`', 'L', 'D`', 'F', 'U2', 'B`', 'U', 'L2', 'U']

Front25 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back25 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up25 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down25 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left25 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right25 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist25 = Facelist(F=Front25,B=Back25,U=Up25,D=Down25,L=Left25,R=Right25)
testcube25 = cubestate(Facelist25)
movesexecutor(testcube25, testmix25)
testcube25.moves.clear()

"Testmix26: B2R2L`R2DF2UF`R`BDF`LFU`LRB2UF`L`UD2B2D"
testmix26 = ['B2', 'R2', 'L`', 'R2', 'D', 'F2', 'U', 'F`', 'R`', 'B', 'D', 'F`', 'L', 'F', 'U`', 'L', 'R', 'B2', 'U', 'F`', 'L`', 'U', 'D2', 'B2', 'D']

Front26 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back26 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up26 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down26 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left26 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right26 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist26 = Facelist(F=Front26,B=Back26,U=Up26,D=Down26,L=Left26,R=Right26)
testcube26 = cubestate(Facelist26)
movesexecutor(testcube26, testmix26)
testcube26.moves.clear()

"Testmix27: DURLB`U`LDL`R2DB`F2R`D`BL`R`U2DUFLDL"
testmix27 = ['D', 'U', 'R', 'L', 'B`', 'U`', 'L', 'D', 'L`', 'R2', 'D', 'B`', 'F2', 'R`', 'D`', 'B', 'L`', 'R`', 'U2', 'D', 'U', 'F', 'L', 'D', 'L']
Front27 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back27 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up27 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down27 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left27 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right27 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist27 = Facelist(F=Front27,B=Back27,U=Up27,D=Down27,L=Left27,R=Right27)
testcube27 = cubestate(Facelist27)
movesexecutor(testcube27, testmix27)
testcube27.moves.clear()

"Testmix28: DR2BL2U2F`DB`F2L`D2BDB2U`RD2U`DUR2FBF`L`"
testmix28 = ['D', 'R2', 'B', 'L2', 'U2', 'F`', 'D', 'B`', 'F2', 'L`', 'D2', 'B', 'D', 'B2', 'U`', 'R', 'D2', 'U`', 'D', 'U', 'R2', 'F', 'B', 'F`', 'L`']
Front28 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back28 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up28 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down28 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left28 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right28 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist28 = Facelist(F=Front28,B=Back28,U=Up28,D=Down28,L=Left28,R=Right28)
testcube28 = cubestate(Facelist28)
movesexecutor(testcube28, testmix28)
testcube28.moves.clear()

"Testmix29: DF`R`LB2U`R2BD`U`F2DF`L2R2L`B`RD`LD`R2U`R`B2"
testmix29 = ['D', 'F`', 'R`', 'L', 'B2', 'U`', 'R2', 'B', 'D`', 'U`', 'F2', 'D', 'F`', 'L2', 'R2', 'L`', 'B`', 'R', 'D`', 'L', 'D`', 'R2', 'U`', 'R`', 'B2']
Front29 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back29 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up29 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down29 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left29 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right29 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist29 = Facelist(F=Front29,B=Back29,U=Up29,D=Down29,L=Left29,R=Right29)
testcube29 = cubestate(Facelist29)
movesexecutor(testcube29, testmix29)
testcube29.moves.clear()

"Testmix30: U2D`L`B`UDFD2L`DRU2B`L`BU`R`L2UDL2B`UF`U`"
testmix30 = ['U2', 'D`', 'L`', 'B`', 'U', 'D', 'F', 'D2', 'L`', 'D', 'R', 'U2', 'B`', 'L`', 'B', 'U`', 'R`', 'L2', 'U', 'D', 'L2', 'B`', 'U', 'F`', 'U`']
Front30 = Front(ul='w',um='w',ur='w',ml='w',mm='w',mr='w',dl='w',dm='w',dr='w')
Back30 = Back(ul='y',um='y',ur='y',ml='y',mm='y',mr='y',dl='y',dm='y',dr='y')
Up30 = Up(fl='b',fm='b',fr='b',ml='b',mm='b',mr='b',bl='b',bm='b',br='b')
Down30 = Down(fl='g',fm='g',fr='g',ml='g',mm='g',mr='g',bl='g',bm='g',br='g')
Left30 = Left(fu='o',fm='o',fd='o',mu='o',mm='o',md='o',bu='o',bm='o',bd='o')
Right30 = Right(fu='r',fm='r',fd='r',mu='r',mm='r',md='r',bu='r',bm='r',bd='r')
Facelist30 = Facelist(F=Front30,B=Back30,U=Up30,D=Down30,L=Left30,R=Right30)
testcube30 = cubestate(Facelist30)
movesexecutor(testcube30, testmix30)
testcube30.moves.clear()

#   
#print("Testmix 1: F'U'L'F'RF2R2UB'R'L'D'BR'B'F'LDU2R'U'FBLF2") 
#cubesolve(testcube1)
#testifsolved(testcube1)
#print('\n')
#
#print("Testmix 2: FRL'D'U2R'D'R'D'BD'B2RL'U'L2U'BL'R2UBF2R'B") 
#cubesolve(testcube2)
#testifsolved(testcube2)
#print('\n')
#
#print("Testmix 3: B'L'BR2LD'L2R'B2F2UB'F2DBF'RLD2F2U2DFB2L") 
#cubesolve(testcube3)
#testifsolved(testcube3)
#print('\n')
#
#print("Testmix 4: D'L2B'U'D2LF'B2DU2F'UB'FD2R'F'U'RLF'BLB'R'") 
#cubesolve(testcube4)
#testifsolved(testcube4)
#print('\n')
#
#print("Testmix 5: BL2BR2D'B2LDRF2B'R'B'DFLU2D2L2BL2U'R'D'L2") 
#cubesolve(testcube5)
#testifsolved(testcube5)
#print('\n')
#
#print("Testmix 6: B2UL'FLDUB'RDUB'FU2BUB'U'B'U'BR2UR2U2") 
#cubesolve(testcube6)
#testifsolved(testcube6)
#print('\n')
#
#print("Testmix 7: F'B'D2L'R2D'RL2D'U'B2F2UF'LBU2R2L2U2L'B'L'F2D2") 
#cubesolve(testcube7)
#testifsolved(testcube7)
#print('\n')
#
#print("Testmix 8: B2F'RUL2D2R'U2R'B2FD'U2R2U2L'DRF'U2D2R2D'U'R'") 
#cubesolve(testcube8)
#testifsolved(testcube8)
#print('\n')
#
#print("Testmix9: D'UL2UD'L2R2F2L'U2B'F2L'R2UD2RL2BU'D2B2L'B2F") 
#cubesolve(testcube9)
#testifsolved(testcube9)
#print('\n')
#
#print("Testmix10: R'BR'BUR'L'BD'F2R'F'RL2U2F'L2RBD2R2F2ULR2") 
#cubesolve(testcube10)
#testifsolved(testcube10)
#print('\n')
#
#print("Testmix11: LU2RU'B'U'F2D'L'D2U'R'D2L2U'D2L'R2D'R'B'L2R2D2U'")
#cubesolve(testcube11)
#testifsolved(testcube11)
#print('\n')
#
#print("Testmix12: U'L2U'B2U'BFL'BD2F'BRD'U2F2U'DB2L2RD2U2RL")
#cubesolve(testcube12)
#testifsolved(testcube12)
#print('\n')
#
#print("Testmix13: D2F'U'F'L2U'BL'DL'UDF'UB'U'B'L'DU2F'DR'U2L")
#cubesolve(testcube13)
#testifsolved(testcube13)
#print('\n')
#
#print("Testmix14: F2DL2D2BU2BU2F'DB'U'R'D2LU2R2BUD'R'LDB2F2")
#cubesolve(testcube14)
#testifsolved(testcube14)
#print('\n')
#
#print("Testmix15: B2L2U2R2L2BF2DUL2R'B2U'B2L'B2UR'UDL'R2BD2F'")
#cubesolve(testcube15)
#testifsolved(testcube15)
#print('\n')
#
#print("Testmix16: L2F2B2DR2FD2F2B'R'DL2BDURL2BD2LR2FLUL2")
#cubesolve(testcube16)
#testifsolved(testcube16)
#print('\n')
#
#print("Testmix17: F'L2BD'U'B'RF'L2D2L'F2U'R'B2D2FDU2L'BF2RD'")
#cubesolve(testcube17)
#testifsolved(testcube17)
#print('\n')
#
#print("Testmix18: FRU2B2R'U'RU2R'D'L2DF'DU'B2D2B'U'F'B2D2FD2L'")
#cubesolve(testcube18)
#testifsolved(testcube18)
#print('\n')
#
#print("Testmix19: FD2B2RB'U'LD'RFB'D2U'F'DB2UBD2R2UL2R'U2B2")
#cubesolve(testcube19)
#testifsolved(testcube19)
#print('\n')
#
#print("Testmix20: DR'B'R2L2UR'D2R2UB2F2R'F'L2F2LR'B'FD2F'R'L'D2")
#cubesolve(testcube20)
#testifsolved(testcube20)
#print('\n')
#
print("Testmix21: F'L'DRU'L2UB2FU'B2U2LBR'U2L2DUFR'U'L'DF")
cubesolve(testcube21)
testifsolved(testcube21)
print('\n')

print("Testmix22: R2B`RBF`UL2R`DF`D`F`L`D2R`D2B2RBR`U`BF`DU")
cubesolve(testcube22)
testifsolved(testcube22)
print('\n')

print("Testmix23: FB2F2R`BRLFU`D`B2F`RF`D`UB2U`LF2RB2UL`U")
cubesolve(testcube23)
testifsolved(testcube23)
print('\n')

print("Testmix24: D2RLRUFLR2LF`B2L`R`LB2D2LR2UBF`L2R2L2R`")
cubesolve(testcube24)
testifsolved(testcube24)
print('\n')

print("Testmix25: U2RB2R2D2F2BLFDB2LFD2R2BU`LD`FU2B`UL2U")
cubesolve(testcube25)
testifsolved(testcube25)
print('\n')

print("Testmix26: B2R2L`R2DF2UF`R`BDF`LFU`LRB2UF`L`UD2B2D")
cubesolve(testcube26)
testifsolved(testcube26)
print('\n')

print("Testmix27: DURLB`U`LDL`R2DB`F2R`D`BL`R`U2DUFLDL")
cubesolve(testcube27)
testifsolved(testcube27)
print('\n')

print("Testmix28: DR2BL2U2F`DB`F2L`D2BDB2U`RD2U`DUR2FBF`L`")
cubesolve(testcube28)
testifsolved(testcube28)
print('\n')

print("Testmix29: DF`R`LB2U`R2BD`U`F2DF`L2R2L`B`RD`LD`R2U`R`B2")
cubesolve(testcube29)
testifsolved(testcube29)
print('\n')

print("Testmix30: U2D`L`B`UDFD2L`DRU2B`L`BU`R`L2UDL2B`UF`U`")
cubesolve(testcube30)
testifsolved(testcube30)
print('\n')