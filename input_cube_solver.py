# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:13:46 2019

@author: sanka
"""

import cubefunctions as CS
import whitecross_2 as WC
import F2L_corneredgepair as F2L
import last_layer as LL

print("It doesn't matter whether you encode the six colors as 1, 2, 3, 4, 5, 6\
      or as r, g, b, y, w, o or whatever, so long as you stay consistent.")

print('Input Front face: ')
Ful = input('Up-Left Panel: ')
Fum = input('Up-Mid Panel: ')
Fur = input('Up-Right Panel: ')
Fml = input('Mid-Left Panel: ')
Fmm = input('Mid-Mid Panel: ')
Fmr = input('Mid-Right Panel: ')
Fdl = input('Down-Left Panel: ')
Fdm = input('Down-Mid Panel: ')
Fdr = input('Down-Right Panel: ')

print('Input Back face: ')
Bul = input('Up-Left Panel: ')
Bum = input('Up-Mid Panel: ')
Bur = input('Up-Right Panel: ')
Bml = input('Mid-Left Panel: ')
Bmm = input('Mid-Mid Panel: ')
Bmr = input('Mid-Right Panel: ')
Bdl = input('Down-Left Panel: ')
Bdm = input('Down-Mid Panel: ')
Bdr = input('Down-Right Panel: ')

print('Input Up face: ')
Ufl = input('Front-Left Panel: ')
Ufm = input('Front-Mid Panel: ')
Ufr = input('Front-Right Panel: ')
Uml = input('Mid-Left Panel: ')
Umm = input('Mid-Mid Panel: ')
Umr = input('Mid-Right Panel: ')
Ubl = input('Back-Left Panel: ')
Ubm = input('Back-Mid Panel: ')
Ubr = input('Back-Right Panel: ')

print('Input Down face: ')
Dfl = input('Front-Left Panel: ')
Dfm = input('Front-Mid Panel: ')
Dfr = input('Front-Right Panel: ')
Dml = input('Mid-Left Panel: ')
Dmm = input('Mid-Mid Panel: ')
Dmr = input('Mid-Right Panel: ')
Dbl = input('Back-Left Panel: ')
Dbm = input('Back-Mid Panel: ')
Dbr = input('Back-Right Panel: ')

print('Input Left face: ')
Lfu = input('Front-Up Panel: ')
Lfm = input('Front-Mid Panel: ')
Lfd = input('Front-Down Panel: ')
Lmu = input('Mid-Up Panel: ')
Lmm = input('Mid-Mid Panel: ')
Lmd = input('Mid-Down Panel: ')
Lbu = input('Back-Up Panel: ')
Lbm = input('Back-Mid Panel: ')
Lbd = input('Back-Down Panel: ')

print('Input Right face: ')
Rfu = input('Front-Up Panel: ')
Rfm = input('Front-Mid Panel: ')
Rfd = input('Front-Down Panel: ')
Rmu = input('Mid-Up Panel: ')
Rmm = input('Mid-Mid Panel: ')
Rmd = input('Mid-Down Panel: ')
Rbu = input('Back-Up Panel: ')
Rbm = input('Back-Mid Panel: ')
Rbd = input('Back-Down Panel: ')

Front0= CS.Front(ul=Ful,um=Fum,ur=Fur,ml=Fml,mm=Fmm,mr=Fmr,dl=Fdl,dm=Fdm,dr=Fdr)
Back0= CS.Back(ul=Bul,um=Bum,ur=Bur,ml=Bml,mm=Bmm,mr=Bmr,dl=Bdl,dm=Bdm,dr=Bdr)
Up0= CS.Up(fl=Ufl,fm=Ufm,fr=Ufr,ml=Uml,mm=Umm,mr=Umr,bl=Ubl,bm=Ubm,br=Ubr)
Down0= CS.Down(fl=Dfl,fm=Dfm,fr=Dfr,ml=Dml,mm=Dmm,mr=Dmr,bl=Dbl,bm=Dbm,br=Dbr)
Left0= CS.Left(fu=Lfu,fm=Lfm,fd=Lfd,mu=Lmu,mm=Lmm,md=Lmd,bu=Lbu,bm=Lbm,bd=Lbd)
Right0= CS.Right(fu=Rfu,fm=Rfm,fd=Rfd,mu=Rmu,mm=Rmm,md=Rmd,bu=Rbu,bm=Rbm,bd=Rbd)
Facelist0 = CS.Facelist(F=Front0,B=Back0,U=Up0,D=Down0,L=Left0,R=Right0)
testcube0 = CS.cubestate(Facelist0)
WC.whitecross(testcube0)
print("Cross: "+"".join(testcube0.moves))
testcube0.moves.clear()
F2L.F2L(testcube0)
print("F2L: "+"".join(testcube0.moves))
testcube0.moves.clear()
LL.lastlayer(testcube0)
print("Last layer: "+"".join(testcube0.moves))
testcube0.moves.clear()

    
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