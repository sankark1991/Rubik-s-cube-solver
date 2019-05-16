# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:45:57 2019

@author: sanka
"""

import collections
import cubefunctions

"All of these mixes will be assuming the white face is F, red face is R, and \
blue face is U."

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

