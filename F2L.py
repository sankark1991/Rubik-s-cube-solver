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

"Testmix 1: LFD'F'R2UBRFR'L'F'R2D'RU2BD2FL'D'R'FB2RD'FDL'U'L"
Frontface = Front()

moves = []

x = cubestate.F.mm
y = cubestate.R.mm
z = cubestate.D.mm

"First, move the corner to either the FRU position, or if it's already in the \
FRD position then leave it there.
cp = cubestate.cornerfind(x,y,z)
if cp == ['F','D','L'] or cp == ['D','L','F'] or cp == ['L','F','D']:
    cubestate.Lprimeturn()
    cubestate.Uprimeturn()
    cubestate.Lturn()
elif cp == ['B','L','D'] or cp == ['L','D','B'] or cp == ['D','B','L']:
    cubestate.Lturn()
    cubestate.Uturn()
    cubestate.Uturn()
    cubestate.Lprimeturn()
elif cp == ['D','B','R'] or cp == ['B','R','D'] or cp == ['R','D','B']:
    cubestate.Bturn()
    cubestate.Uturn()
    cubestate.Bprimeturn()
elif cp == ['U','F','L'] or cp == ['F','L','U'] or cp == ['L','U','F']:
    cubestate.Uprimeturn()
elif cp == ['U','R','B'] or cp == ['R','B','U'] or cp == ['B','U','R']:
    cubestate.Uturn()
    cubestate.Uturn()
elif cp == ['U','B','L'] or cp = ['B','L','U'] or cp == ['L','U','B']:
    cubestate.Uturn()
    
if cp == ['F','R','D'] or cp == ['R','D','F'] or cp == ['D','F','R']:
    pos = 1
else:
    pos = 0
    
"Now move the edge to the U face, or if it's already in the FR position then \
leave it there."
ep = cubestate.edgefind(x,y)
if ep == ['F','L'] or ep == ['L','F']:
    cubestate.Fturn()
    cubestate.Uprimeturn()
    cubestate.Fprimeturn()
elif ep == ['R','B'] or ep == ['B','R']:
    cubestate.Rprimeturn()
    cubestate.Uturn()
    cubestate.Rturn()
elif ep == ['L','B'] or ep == ['B','L']:
    if pos == 1:
        cubestate.Lturn()
        cubestate.Uprimeturn()
        cubestate.Lprimeturn()
    else:
        cubestate.Lturn()
        cubestate.Uprimeturn()
        cubestate.Lprimeturn()
        cubestate.Uturn()
    
"There are now 41 possible cases to handle."
cp = cubestate.cornerfind(x,y,z)
ep = cubestate.edgefind(x,y)
    