# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:20:40 2019

@author: sanka
"""

import cubefunctions

def whitecross(cubestate):
    "Let r, u, l, d be the colors on the four faces."
    f = cubestate.F.mm
    r = cubestate.R.mm
    u = cubestate.U.mm
    l = cubestate.L.mm
    d = cubestate.D.mm
    for i in [r, u, l, d]:
        edge = cubestate.edgefind(f, i)
        "2 turns: edge is on the white face in the wrong orientation."
        if edge[1] == 'F':
            if edge[0] == 'R':
                if cubestate.F.um != f:
                    cubestate.Rturn()
                    cubestate.Uturn()
                elif cubestate.F.dm != f:
                    cubestate.Rprimeturn()
                    cubestate.Dprimeturn()
                else:
                    cubestate.Rturn()
                    cubestate.Fprimeturn()
                    cubestate.Uturn()
            if edge[0] == 'U':
                if cubestate.F.ml != f:
                    cubestate.Uturn()
                    cubestate.Lturn()
                elif cubestate.F.mr != f:
                    cubestate.Uprimeturn()
                    cubestate.Rprimeturn()
                else:
                    cubestate.Uturn()
                    cubestate.Fprimeturn()
                    cubestate.Lturn()
            if edge[0] == 'L':
                if cubestate.F.dm != f:
                    cubestate.Lturn()
                    cubestate.Dturn()
                elif cubestate.F.um != f:
                    cubestate.Lprimeturn()
                    cubestate.Uprimeturn()
                else:
                    cubestate.Lturn()
                    cubestate.Fprimeturn()
                    cubestate.Dturn()
            if edge[0] == 'D':
                if cubestate.F.mr != f:
                    cubestate.Dturn()
                    cubestate.Rturn()
                elif cubestate.F.ml != f:
                    cubestate.Dprimeturn()
                    cubestate.Lprimeturn()
                else:
                    cubestate.Dturn()
                    cubestate.Fprimeturn()
                    cubestate.Rturn()
        "2 turns: edge is on the opposite face with the white panel on an adjacent face."
        if edge[1] == 'B':
            if edge[0] == 'R':
                while cubestate.F.um == f:
                    cubestate.Fturn()
                if cubestate.F.ml == f:
                    cubestate.Rprimeturn()
                    cubestate.Uturn()
                    cubestate.Rturn()
                else:
                    cubestate.Rprimeturn()
                    cubestate.Uturn()
                    cubestate.Rturn()
            if edge[0] == 'U':
                while cubestate.F.ml == f:
                    cubestate.Fturn()
                if cubestate.F.um == f:
                    cubestate.Uprimeturn()
                    cubestate.Lturn()
                    cubestate.Uturn()
                else:
                    cubestate.Uprimeturn()
                    cubestate.Lturn()
            if edge[0] == 'L':
                while cubestate.F.dm == f:
                    cubestate.Fturn()
                if cubestate.F.ml == f:
                    cubestate.Lprimeturn()
                    cubestate.Dturn()
                    cubestate.Lturn()
                else:
                    cubestate.Lprimeturn()
                    cubestate.Dturn()
            if edge[0] == 'D':
                while cubestate.F.mr == f:
                    cubestate.Fturn()
                if cubestate.F.dm == f:
                    cubestate.Dprimeturn()
                    cubestate.Rturn()
                    cubestate.Dturn()
                else:
                    cubestate.Dprimeturn()
                    cubestate.Rturn()
        "1 turn or 0 turns: non-white panel is on an adjacent face."
        if edge[0] != 'F':
            if edge[1] == 'R':
                while cubestate.F.mr == f:
                    cubestate.Fturn()
                if edge[0] == 'U':
                    cubestate.Rprimeturn()
                elif edge[0] == 'D':
                    cubestate.Rturn()
                elif edge[0] == 'B':
                    cubestate.Rturn()
                    cubestate.Rturn()
            if edge[1] == 'L':
                while cubestate.F.ml == f:
                    cubestate.Fturn()
                if edge[0] == 'U':
                    cubestate.Lturn()
                elif edge[0] == 'D':
                    cubestate.Lprimeturn()
                elif edge[0] == 'B':
                    cubestate.L2turn()
            if edge[1] == 'U':
                while cubestate.F.um == f:
                    cubestate.Fturn()
                if edge[0] == 'R':
                    cubestate.Uturn()
                elif edge[0] == 'L':
                    cubestate.Uprimeturn()
                elif edge[0] == 'B':
                    cubestate.U2turn()
            if edge[1] == 'D':
                while cubestate.F.dm == f:
                    cubestate.Fturn()
                if edge[0] == 'R':
                    cubestate.Dprimeturn()
                elif edge[0] == 'L':
                    cubestate.Dturn()
                elif edge[0] == 'B':
                    cubestate.D2turn()  
    

    "The next step is to permute the four cross edges correctly."

    "First, get the FR edge to the right position."
    if cubestate.U.fm == r:
        cubestate.Fturn()
    if cubestate.D.fm == r:
        cubestate.Fprimeturn()
    if cubestate.L.fm == r:
        cubestate.F2turn()   
    "There are six possibilities for the positions of the three other edges."
    if cubestate.U.fm == d and cubestate.D.fm == u:
        if cubestate.moves[-1] == 'F2':
            cubestate.F2turn()
            cubestate.Rturn()
            cubestate.F2turn()
            cubestate.Rprimeturn()
            cubestate.F2turn()
            cubestate.Rturn()
        else:
            cubestate.Uturn()
            cubestate.F2turn()
            cubestate.Uprimeturn()
            cubestate.F2turn()
            cubestate.Uturn()
    if cubestate.U.fm == d and cubestate.L.fm == u:
        cubestate.Fturn()
        cubestate.Rturn()
        cubestate.Fprimeturn()
        cubestate.Rprimeturn()
        cubestate.Fturn()
        cubestate.Rturn()
    if cubestate.U.fm == l and cubestate.L.fm == d:
        cubestate.Fprimeturn()
        cubestate.Rprimeturn()
        cubestate.Fturn()
        cubestate.Rturn()
        cubestate.Fprimeturn()
        cubestate.Rprimeturn()
    if cubestate.U.fm == l and cubestate.L.fm == u:
        cubestate.Uturn()
        cubestate.Fturn()
        cubestate.Uprimeturn()
        cubestate.Fprimeturn()
        cubestate.Uturn()
    if cubestate.L.fm == d and cubestate.D.fm == l:
        cubestate.Lturn()
        cubestate.Fturn()
        cubestate.Lprimeturn()
        cubestate.Fprimeturn()
        cubestate.Lturn()
    cubestate.movesconsolidate()
    cubestate.FtoDturn()
    #moveswhitecross = cubestate.moves.copy()
    #cubestate.moves.clear()
    #return moveswhitecross