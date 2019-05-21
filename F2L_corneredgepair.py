# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:20:59 2019

@author: sanka
"""

import cubefunctions

"It'll be assumed here that the cross is on the D face."

"The algorithm below will solve the corner edge pair involving the FRD corner \
and the FR edge."

"First we move the corner to either the FRD or FRU position and the edge to one\
of the five positions FR, FU, RU, BU, LU."

def F2L_ce_pair(cube):
    x = cube.F.mm
    y = cube.R.mm
    z = cube.D.mm
    
    #"Case 1: the corner is in one of the four D slots. In this case, our strategy \
    #is to get the edge near it and pair them up."
    #cp = cube.cornerfind(x,y,z)
    #case = 0
    #if cp == ['F','D','L'] or cp == ['D','L','F'] or cp == ['L','F','D']:
    #    cube.FtoRturn()
    #    case = 1
    #elif cp == ['B','L','D'] or cp == ['L','D','B'] or cp == ['D','B','L']:
    #    cube.FtoRturn()
    #    cube.FtoRturn()
    #    case = 2
    #elif cp == ['D','B','R'] or cp == ['B','R','D'] or cp == ['R','D','B']:
    #    cube.FtoLturn()
    #    case = 3
    #elif cp == ['F','R','D'] or cp == ['R','D','F'] or cp == ['R','D','F']:
    #    case = 4
    #if case == 1 or case == 2 or case == 3:
    #    cp = cube.cornerfind(x,y,z)
    #    ep = cube.edgefind(x,y)
    #    if ep == ['F','L'] or ep == ['L','F']:
    #        cube.Fturn()
    #        cube.Uprimeturn()
    #        cube.Fprimeturn()
    #    elif ep == ['R','B'] or ep == ['B','R']:
    #        cube.Rprimeturn()
    #        cube.Uturn()
    #        cube.Rturn()
    #    elif ep == ['L','B'] or ep == ['B','L']:
    #        cube.Lturn()
    #        cube.Uprimeturn()
    #        cube.Lprimeturn()       
    

    "First, move the corner to either the FRU position, or if it's already in the \
    FRD position then leave it there."
    cp = cube.cornerfind(x,y,z)
    if cp == ['F','D','L'] or cp == ['D','L','F'] or cp == ['L','F','D']:
        cube.Lprimeturn()
        cube.Uprimeturn()
        cube.Lturn()
    elif cp == ['B','L','D'] or cp == ['L','D','B'] or cp == ['D','B','L']:
        cube.Lturn()
        cube.U2turn()
        cube.Lprimeturn()
    elif cp == ['D','R','B'] or cp == ['B','D','R'] or cp == ['R','B','D']:
        cube.Bturn()
        cube.Uturn()
        cube.Bprimeturn()
    elif cp == ['U','F','L'] or cp == ['F','L','U'] or cp == ['L','U','F']:
        cube.Uprimeturn()
    elif cp == ['U','B','R'] or cp == ['R','U','B'] or cp == ['B','R','U']:
        cube.Uturn()
    elif cp == ['U','L','B'] or cp == ['B','U','L'] or cp == ['L','B','U']:
        cube.U2turn()
    else:
        pass
    
    "Variable pos = 1 if the corner is in the right position, or pos = 0 if it's above."
    cp = cube.cornerfind(x,y,z)
    if cp == ['F','R','D'] or cp == ['R','D','F'] or cp == ['D','F','R']:
        pos = 1
    else:
        pos = 0
    
    "Now move the edge to the U face, or if it's already in the FR position then \
    leave it there."
    ep = cube.edgefind(x,y)
    if ep == ['F','L'] or ep == ['L','F']:
        cube.Fturn()
        cube.Uprimeturn()
        cube.Fprimeturn()
    elif ep == ['R','B'] or ep == ['B','R']:
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
    elif ep == ['L','B'] or ep == ['B','L']:
        if pos == 1:
            cube.Lturn()
            cube.Uprimeturn()
            cube.Lprimeturn()
        else:
            cube.Lturn()
            cube.Uprimeturn()
            cube.Lprimeturn()
            cube.Uturn()
    else:
        pass
    
    "There are now 60 cases to handle."
    cp = cube.cornerfind(x,y,z)
    ep = cube.edgefind(x,y)
    
    "Corner oriented FUR. There are 10 cases here."
    if cp == ['F','U','R']:
        if ep == ['U','B']:
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['F','U']:
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
        elif ep == ['R','U']:
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.U2turn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['B','U']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
        elif ep == ['L','U']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
        elif ep == ['U','R']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['U','L']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['U','F']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['F','R']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
        elif ep == ['R','F']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
    "Corner oriented URF. There are 10 cases here."
    if cp == ['U','R','F']:
        if ep == ['L','U']:
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['U','R']:
            cube.Uturn()
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
        elif ep == ['U','F']:
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
            cube.U2turn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['U','L']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
        elif ep == ['U','B']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
        elif ep == ['F','U']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['B','U']:
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['R','U']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['F','R']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
        elif ep == ['R','F']:
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
    "Corner oriented RFU. There are 10 cases here."
    if cp == ['R','F','U']:
        if ep == ['L','U']:
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
        elif ep == ['B','U']:
            cube.Fprimeturn()
            cube.Lprimeturn()
            cube.U2turn()
            cube.Lturn()
            cube.Fturn()
        elif ep == ['U','L']:
            cube.Rturn()
            cube.Bturn()
            cube.U2turn()
            cube.Bprimeturn()
            cube.Rprimeturn()
        elif ep == ['U','B']:
            cube.Uturn()
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
        elif ep == ['F','U']:
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['U','F']:
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.U2turn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['R','U']:
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
            cube.U2turn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        elif ep == ['U','R']:
            cube.Rturn()
            cube.U2turn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep == ['F','R']:
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
        elif ep == ['R','F']:
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
    "Corner oriented RDF. There are 10 cases."
    if cp == ['R','D','F']:
        if ep[0] == 'U':
            if ep[1] == 'F':
                cube.Uprimeturn()
            elif ep[1] == 'L':
                cube.U2turn()
            elif ep[1] == 'B':
                cube.Uturn()
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
        elif ep[1] == 'U':
            if ep[0] == 'R':
                cube.Uturn
            elif ep[0] == 'B':
                cube.U2turn
            elif ep[0] == 'L':
                cube.Uprimeturn
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fturn()
        else:
            if ep == ['F','R']:
                cube.Rturn()
                cube.Uprimeturn()
                cube.Rprimeturn()
                cube.Uprimeturn()
                cube.Rturn()
                cube.Uturn()
                cube.Rprimeturn()
                cube.Uprimeturn()
                cube.Rturn()
                cube.U2turn()
                cube.Rprimeturn()
            elif ep == ['R','F']:
                cube.Rturn()
                cube.Uprimeturn()
                cube.Rprimeturn()
                cube.Uturn()
                cube.Fprimeturn()
                cube.Uprimeturn()
                cube.Fturn()
                cube.Uprimeturn()
                cube.Fprimeturn()
                cube.Uprimeturn()
                cube.Fturn()
            
    "Corner oriented DFR. There are 10 cases."
    if cp == ['D','F','R']:
        if ep[0] == 'U':
            if ep[1] == 'B':
                cube.Uturn()
            elif ep[1] == 'L':
                cube.U2turn()
            elif ep[1] == 'F':
                cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rprimeturn()
        elif ep[1] == 'U':
            if ep[0] == 'R':
                cube.Uturn()
            elif ep[0] == 'B':
                cube.U2turn()
            elif ep[0] == 'L':
                cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uturn()
            cube.Fturn()
        else:
            if ep == ['F','R']:
                cube.Rturn()
                cube.Uprimeturn()
                cube.Rprimeturn()
                cube.Uturn()
                cube.Rturn()
                cube.U2turn()
                cube.Rprimeturn()
                cube.Uturn()
                cube.Rturn()
                cube.Uprimeturn()
                cube.Rprimeturn()
            elif ep == ['R','F']:
                cube.Rturn()
                cube.Uturn()
                cube.Rprimeturn()
                cube.Uprimeturn()
                cube.Rturn()
                cube.Uprimeturn()
                cube.Rprimeturn()
                cube.U2turn()
                cube.Fprimeturn()
                cube.Uprimeturn()
                cube.Fturn()
    "Corner in place. There are 10 cases."
    if cp == ['F','R','D']:
        if ep[0] == 'U':
            if ep[1] == 'B':
                cube.Uturn()
            elif ep[1] == 'L':
                cube.U2turn()
            elif ep[1] == 'F':
                cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Rturn()
            cube.Uturn()
            cube.Rturn()
        elif ep[1] == 'U':
            if ep[0] == 'R':
                cube.Uturn()
            elif ep[0] == 'B':
                cube.U2turn()
            elif ep[0] == 'L':
                cube.Uprimeturn()
            cube.Fturn()
            cube.Uturn()
            cube.Fturn()
            cube.Uturn()
            cube.Fturn()
            cube.Uprimeturn()
            cube.Fprimeturn()
            cube.Uprimeturn()
            cube.Fprimeturn()
        elif ep == ['R','F']:
            cube.Rturn()
            cube.Uprimeturn()
            cube.Rprimeturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()
            cube.Uturn()
            cube.Fprimeturn()
            cube.U2turn()
            cube.Fturn()

def F2L(cube):
    F2L_ce_pair(cube)
    cube.FtoLturn()
    F2L_ce_pair(cube)
    cube.FtoLturn()
    F2L_ce_pair(cube)
    cube.FtoLturn()
    F2L_ce_pair(cube)
    cube.movesconsolidate()
    #movesF2L = cube.moves.copy()
    #cube.moves.clear()
    #return movesF2L
    