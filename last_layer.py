# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:28:56 2019

@author: sanka
"""

import cubefunctions

"It's assumed that the bottom two layers are solved. The OLL is done in two steps:\
first edge orientation, then corner orientation. The PLL is done in one step."

"Later I might implement the OLL as one algorithm. The challenge in writing this\
code is to find a clever way to group all of the cases, mimicking the 'pattern \
recognition' that a human does. But I don't think I'll learn much from this exercise."

def OLL(cube):
    y = cube.U.mm
    "Each of the four edges will be labeled either True (correctly oriented) or\
    False (incorrectly oriented). An even number of these are True, so there are\
    8 possibilities for edge orientation."
    eo = (cube.U.fm == y, cube.U.ml == y, cube.U.bm == y, cube.U.mr == y)
    if eo == (False, False, False, False):
        cube.Lprimeturn()
        cube.R2turn()
        cube.Bturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.U2turn()
        cube.Lprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Rprimeturn()
    elif eo == (False, True, False, True):
        cube.Fturn()
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uprimeturn()
        cube.Fprimeturn()
    elif eo == (True, False, True, False):
        cube.Uturn()
        cube.Fturn()
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uprimeturn()
        cube.Fprimeturn()
    elif eo == (False, True, True, False):
        cube.Fturn()
        cube.Uturn()
        cube.Rturn()
        cube.Uprimeturn()
        cube.Rprimeturn()
        cube.Fprimeturn()
    elif eo == (True, True, False, False):
        cube.Uturn()
        cube.Fturn()
        cube.Uturn()
        cube.Rturn()
        cube.Uprimeturn()
        cube.Rprimeturn()
        cube.Fprimeturn()
    elif eo == (True, False, False, True):
        cube.U2turn()
        cube.Fturn()
        cube.Uturn()
        cube.Rturn()
        cube.Uprimeturn()
        cube.Rprimeturn()
        cube.Fprimeturn()
    elif eo == (False, False, True, True):
        cube.Uprimeturn()
        cube.Fturn()
        cube.Uturn()
        cube.Rturn()
        cube.Uprimeturn()
        cube.Rprimeturn()
        cube.Fprimeturn()
    elif eo == (True, True, True, True):
        pass
    else:
        print("Error - invalid edge configuration!")
    "Each of the four corners will be labeled 0 (correct oriented), 1 (requires \
    a clockwise turn to be correctly oriented), or 2 (requires a counterclockwise\
    turn to be correctly oriented). The sum of these four numbers has to be a \
    multiple of three, so there are 27 possibilities for the corners."
    if cube.U.fl == y:
        co0 = 0
    elif cube.L.fu == y:
        co0 = 1
    elif cube.F.ul == y:
        co0 = 2
    else:
        print("Error, non-yellow corner on top!")
    if cube.U.bl == y:
        co1 = 0
    elif cube.B.ul == y:
        co1 = 1
    elif cube.L.bu == y:
        co1 = 2
    else:
        print("Error, non-yellow corner on top!")
    if cube.U.br == y:
        co2 = 0
    elif cube.R.bu == y:
        co2 = 1
    elif cube.B.ur == y:
        co2 = 2
    else:
        print("Error, non-yellow corner on top!") 
    if cube.U.fr == y:
        co3 = 0
    elif cube.F.ur == y:
        co3 = 1
    elif cube.R.fu == y:
        co3 = 2
    else:
        print("Error, non-yellow corner on top!")
    co = (co0, co1, co2, co3)
    "Case: Three corners need to be turned clockwise."
    if co == (0, 1, 1, 1):
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (1, 1, 1, 0):
        cube.Uturn()
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (1, 1, 0, 1):
        cube.U2turn()
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (1, 0, 1, 1):
        cube.Uprimeturn()
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
        cube.U2turn()
        cube.Rprimeturn()
    #Case: Three corners need to be turned counterclockwise.
    elif co == (2, 2, 2, 0):
        cube.Lprimeturn()
        cube.Uprimeturn()
        cube.Lturn()
        cube.Uprimeturn()
        cube.Lprimeturn()
        cube.U2turn()
        cube.Lturn()
    elif co == (0, 2, 2, 2):
        cube.Uprimeturn()
        cube.Lprimeturn()
        cube.Uprimeturn()
        cube.Lturn()
        cube.Uprimeturn()
        cube.Lprimeturn()
        cube.U2turn()
        cube.Lturn()
    elif co == (2, 0, 2, 2):
        cube.U2turn()
        cube.Lprimeturn()
        cube.Uprimeturn()
        cube.Lturn()
        cube.Uprimeturn()
        cube.Lprimeturn()
        cube.U2turn()
        cube.Lturn()
    elif co == (2, 2, 0, 2):
        cube.Uturn()
        cube.Lprimeturn()
        cube.Uprimeturn()
        cube.Lturn()
        cube.Uprimeturn()
        cube.Lprimeturn()
        cube.U2turn()
        cube.Lturn()
    #Case: Two adjacent corners, yellows pointed in opposite directions.
    elif co == (0, 0, 2, 1):
        cube.Rturn()
        cube.Bturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
    elif co == (1, 0, 0, 2):
        cube.Uprimeturn()
        cube.Rturn()
        cube.Bturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
    elif co == (2, 1, 0, 0):
        cube.U2turn()
        cube.Rturn()
        cube.Bturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
    elif co == (0, 2, 1, 0):
        cube.Uturn()
        cube.Rturn()
        cube.Bturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
    #Case: Two adjacent corners, yellows pointed in the same direction.#
    elif co == (2, 0, 0, 1):
        cube.R2turn()
        cube.Dturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rturn()
        cube.Dprimeturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (1, 2, 0, 0):
        cube.Uprimeturn()
        cube.R2turn()
        cube.Dturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rturn()
        cube.Dprimeturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (0, 1, 2, 0):
        cube.U2turn()
        cube.R2turn()
        cube.Dturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rturn()
        cube.Dprimeturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (0, 0, 1, 2):
        cube.Uprimeturn()
        cube.R2turn()
        cube.Dturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rturn()
        cube.Dprimeturn()
        cube.Rprimeturn()
        cube.U2turn()
        cube.Rprimeturn()
    #Case: Two opposite corners.#
    elif co == (0, 2, 0, 1):
        cube.Rturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
    elif co == (2, 0, 1, 0):
        cube.Lprimeturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
        cube.Rturn()
        cube.Bturn()
    elif co == (0, 1, 0, 2):
        cube.Uturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
        cube.Rturn()
        cube.Bturn()
    elif co == (1, 0, 2, 0):
        cube.Uprimeturn()
        cube.Rturn()
        cube.Bturn()
        cube.Lturn()
        cube.Bprimeturn()
        cube.Rprimeturn()
        cube.Bturn()
        cube.Lprimeturn()
        cube.Bprimeturn()
    #Case: Four corners, case 1.
    elif co == (1, 2, 2, 1):
        cube.Rturn()
        cube.U2turn()
        cube.R2turn()
        cube.Uprimeturn()
        cube.R2turn()
        cube.Uprimeturn()
        cube.R2turn()
        cube.U2turn()
        cube.Rturn()
    elif co == (2, 2, 1, 1):
        cube.Uturn()
        cube.Rturn()
        cube.U2turn()
        cube.R2turn()
        cube.Uprimeturn()
        cube.R2turn()
        cube.Uprimeturn()
        cube.R2turn()
        cube.U2turn()
        cube.Rturn()
    elif co == (2, 1, 1, 2):
        cube.Lturn()
        cube.U2turn()
        cube.L2turn()
        cube.Uprimeturn()
        cube.L2turn()
        cube.Uprimeturn()
        cube.L2turn()
        cube.U2turn()
        cube.Lturn()
    elif co == (1, 1, 2, 2):
        cube.Uturn()
        cube.Lturn()
        cube.U2turn()
        cube.L2turn()
        cube.Uturn()
        cube.L2turn()
        cube.Uturn()
        cube.L2turn()
        cube.U2turn()
        cube.Lturn()
    #Case: Four corners, case 2.#
    elif co == (1, 2, 1, 2):
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
        cube.Uprimeturn()
        cube.Rprimeturn()
        cube.Uturn()
        cube.Rturn()
        cube.U2turn()
        cube.Rprimeturn()
    elif co == (2, 1, 2, 1):
        cube.Rturn()
        cube.U2turn()
        cube.Rprimeturn()
        cube.Uprimeturn()
        cube.Rturn()
        cube.Uturn()
        cube.Rprimeturn()
        cube.Uprimeturn()
        cube.Rturn()
        cube.Uprimeturn()
        cube.Rprimeturn()
    else: pass
    

def PLL(cube):
    f = cube.F.mm
    l = cube.L.mm
    b = cube.B.mm
    r = cube.R.mm
    #"There are 24*24/2 = 288 possible permutations of the last layer. Each can \
    #be solved using some number of Uturns, then one of the 21 PLL algorithms, then\
    #again some number of Uturns. Hard-coding in all 288 cases will be painful, so\
    #at the cost of one or two moves, I'll first turn the U face until the front-left\
    #corner is correct, and then from there address the 72 possible cases."
    if cube.F.ul == f:
        pass
    elif cube.R.fu == f:
        cube.Uturn()
    elif cube.B.ur == f:
        cube.U2turn()
    elif cube.L.bu == f:
        cube.Uprimeturn()
    else:
        print("Can't find front-left corner!")
        return None
      
    #"I'll now store the four edges in a list."
    ep = [cube.F.um, cube.L.mu, cube.B.um, cube.R.mu]
    #"I'll store the four corners in a list according to their countnerclockwise\
    #(more right) panel. Note that cp[0] == f by construction."
    cp = [cube.F.ul, cube.L.bu, cube.B.ur, cube.R.fu]

    #"Now each of the 72 possibilities can be solved using the PLL methods. I've\
    #hard-coded them all in."
    
    #No PLL algorithm required
    if cp == [f,l,b,r] and ep == [f,l,b,r]:
        pass
    #Edge right
    elif cp == [f,l,b,r] and ep == [r,f,b,l]:
        cube.PLL_edgeright()
    elif cp == [f,l,b,r] and ep == [r,l,f,b]:
        cube.Uturn()
        cube.PLL_edgeright()
    elif cp == [f,l,b,r] and ep == [f,r,l,b]:
        cube.U2turn()
        cube.PLL_edgeright()
    elif cp == [f,l,b,r] and ep == [b,f,l,r]:
        cube.Uprimeturn()
        cube.PLL_edgeright()
    #Edge left
    elif cp == [f,l,b,r] and ep == [l,r,b,f]:
        cube.PLL_edgeleft()
    elif cp == [f,l,b,r] and ep == [b,l,r,f]:
        cube.Uturn()
        cube.PLL_edgeleft()
    elif cp == [f,l,b,r] and ep == [f,b,r,l]:
        cube.U2turn()
        cube.PLL_edgeleft()
    elif cp == [f,l,b,r] and ep == [l,b,f,r]:
        cube.Uprimeturn()
        cube.PLL_edgeleft()
    #Edge Z
    elif cp == [f,l,b,r] and ep == [r,b,l,f]:
        cube.PLL_edgez()
    elif cp == [f,l,b,r] and ep == [l,f,r,b]:
        cube.Uturn()
        cube.PLL_edgez()
    #Edge plus
    elif cp == [f,l,b,r] and ep == [b,r,f,l]:
        cube.PLL_edgeplus()
    #9 move
    elif cp == [f,b,r,l] and ep == [f,l,b,r]:
        cube.PLL_9()
    elif cp == [f,b,l,r] and ep == [r,f,l,b]:
        cube.U2turn()
        cube.PLL_9()
    elif cp == [f,l,r,b] and ep == [r,f,l,b]:
        cube.Uturn()
        cube.PLL_9()
    elif cp == [f,r,l,b] and ep == [b,r,f,l]:
        cube.Uprimeturn()
        cube.PLL_9()
    #9rev move
    elif cp == [f,r,l,b] and ep == [f,l,b,r]:
        cube.PLL_9rev()
    elif cp == [f,b,r,l] and ep == [b,r,f,l]:
        cube.Uturn()
        cube.PLL_9rev()
    elif cp == [f,b,l,r] and ep == [r,b,f,l]:
        cube.Uprimeturn()
        cube.PLL_9rev()
    elif cp == [f,l,r,b] and ep == [l,b,r,f]:
        cube.U2turn()
        cube.PLL_9rev()
    #Double9
    elif cp == [f,r,b,l] and ep == [r,f,l,b]:
        cube.PLL_double9()
    elif cp == [f,r,b,l] and ep == [l,b,r,f]:
        cube.Uturn()
        cube.PLL_double9()
    #Lright
    elif cp == [f,l,r,b] and ep == [f,l,r,b]:
        cube.PLL_Lright()
    elif cp == [f,b,l,r] and ep == [f,b,l,r]:
        cube.Uturn()
        cube.PLL_Lright()
    elif cp == [f,b,r,l] and ep == [f,b,r,l]:
        cube.U2turn()
        cube.PLL_Lright()
    elif cp == [f,r,l,b] and ep == [f,r,l,b]:
        cube.Uprimeturn()
        cube.PLL_Lright()
    #Lleft
    elif cp == [f,b,r,l] and ep == [b,l,r,f]:
        cube.Uturn()
        cube.PLL_Lleft()
    elif cp == [f,r,l,b] and ep == [r,l,f,b]:
        cube.PLL_Lleft()
    elif cp == [f,l,r,b] and ep == [r,l,b,f]:
        cube.U2turn()
        cube.PLL_Lleft()
    elif cp == [f,b,l,r] and ep == [f,l,b,r]:
        cube.Uprimeturn()
        cube.PLL_Lleft()
    #T
    elif cp == [f,l,r,b] and ep == [f,r,b,l]:
        cube.PLL_T()
    elif cp == [f,b,l,r] and ep == [b,l,f,r]:
        cube.Uturn()
        cube.PLL_T()
    elif cp == [f,b,r,l] and ep == [r,b,l,f]:
        cube.Uprimeturn()
        cube.PLL_T()
    elif cp == [f,r,l,b] and ep == [r,b,l,f]:
        cube.U2turn()
        cube.PLL_T()
    #7right
    elif cp == [f,b,l,r] and ep == [r,l,b,f]:
        cube.PLL_7right()
    elif cp == [f,l,r,b] and ep == [l,f,b,r]:
        cube.Uprimeturn()
        cube.PLL_7right()
    elif cp == [f,r,l,b] and ep == [r,f,b,l]:
        cube.Uturn()
        cube.PLL_7right()
    elif cp == [f,b,r,l] and ep == [l,r,b,f]:
        cube.U2turn()
        cube.PLL_7right()
    #7left
    elif cp == [f,b,l,r] and ep == [l,f,b,r]:
        cube.PLL_7left()
    elif cp == [f,l,r,b] and ep == [f,b,l,r]:
        cube.Uprimeturn()
        cube.PLL_7left()
    elif cp == [f,r,l,b] and ep == [b,f,l,r]:
        cube.Uturn()
        cube.PLL_7left()
    elif cp == [f,b,r,l] and ep == [l,b,f,r]:
        cube.U2turn()
        cube.PLL_7left()
    #V
    elif cp == [f,r,b,l] and ep == [f,l,r,b]:
        cube.PLL_V()
    elif cp == [f,r,b,l] and ep == [l,r,f,b]:
        cube.Uprimeturn()
        cube.PLL_V()
    elif cp == [f,r,b,l] and ep == [l,f,b,r]:
        cube.U2turn()
        cube.PLL_V()
    elif cp == [f,r,b,l] and ep == [b,f,r,l]:
        cube.Uturn()
        cube.PLL_V()
    #Gright
    elif cp == [f,l,r,b] and ep == [r,b,f,l]:
        cube.PLL_Gright()
    elif cp == [f,b,l,r] and ep == [l,r,f,b]:
        cube.Uturn()
        cube.PLL_Gright()
    elif cp == [f,r,l,b] and ep == [l,b,f,r]:
        cube.U2turn()
        cube.PLL_Gright()
    elif cp == [f,b,r,l] and ep == [r,l,f,b]:
        cube.Uprimeturn()
        cube.PLL_Gright()
    #Gleft
    elif cp == [f,r,l,b] and ep == [f,b,r,l]:
        cube.PLL_Gleft()
    elif cp == [f,b,r,l] and ep == [r,f,b,l]:
        cube.Uturn()
        cube.PLL_Gleft()
    elif cp == [f,l,r,b] and ep == [b,f,r,l]:
        cube.U2turn()
        cube.PLL_Gleft()
    elif cp == [f,b,l,r] and ep == [r,b,f,l]:
        cube.Uprimeturn()
        cube.PLL_Gleft()
    #Grightrev
    elif cp == [f,r,l,b] and ep == [b,l,r,f]:
        cube.PLL_Grightrev()
    elif cp == [f,b,r,l] and ep == [b,f,l,r]:
        cube.Uturn()
        cube.PLL_Grightrev()
    elif cp == [f,l,r,b] and ep == [b,r,l,f]:
        cube.U2turn()
        cube.PLL_Grightrev()
    elif cp == [f,b,l,r] and ep == [b,f,r,l]:
        cube.Uprimeturn()
        cube.PLL_Grightrev()
    #Gleftrev
    elif cp == [f,l,r,b] and ep == [l,r,f,b]:
        cube.PLL_Gleftrev()
    elif cp == [f,b,l,r] and ep == [b,r,l,f]:
        cube.Uturn()
        cube.PLL_Gleftrev()
    elif cp == [f,r,l,b] and ep == [l,r,b,f]:
        cube.U2turn()
        cube.PLL_Gleftrev()
    elif cp == [f,b,r,l] and ep == [f,r,l,b]:
        cube.Uprimeturn()
        cube.PLL_Gleftrev()
    #equal
    elif cp == [f,b,l,r] and ep == [f,r,b,l]:
        cube.PLL_equal()
    elif cp == [f,r,l,b] and ep == [l,f,r,b]:
        cube.Uturn()
        cube.PLL_equal()
    elif cp == [f,b,r,l] and ep == [l,f,r,b]:
        cube.U2turn()
        cube.PLL_equal()
    elif cp == [f,l,r,b] and ep == [b,l,f,r]:
        cube.Uprimeturn()
        cube.PLL_equal()
    #Y
    elif cp == [f,r,b,l] and ep == [f,b,l,r]:
        cube.PLL_Y()
    elif cp == [f,r,b,l] and ep == [r,b,f,l]:
        cube.Uturn()
        cube.PLL_Y()
    elif cp == [f,r,b,l] and ep == [r,l,b,f]:
        cube.U2turn()
        cube.PLL_Y()
    elif cp == [f,r,b,l] and ep == [b,r,l,f]:
        cube.Uprimeturn()
        cube.PLL_Y()
    #Nright
    elif cp == [f,r,b,l] and ep == [f,r,b,l]:
        cube.PLL_Nright()
    #Nleft
    elif cp == [f,r,b,l] and ep == [b,l,f,r]:
        cube.PLL_Nleft()
    else:
        print("Can't find PLL algorithm!")

def lastlayer(cube):
    OLL(cube)
    PLL(cube)
    if cube.F.um == cube.F.mm:
        pass
    elif cube.F.um == cube.L.mm:
        cube.Uturn()
    elif cube.F.um == cube.B.mm:
        cube.U2turn()
    elif cube.F.um == cube.R.mm:
        cube.Uprimeturn()
    cube.movesconsolidate()
    #movesLL = cube.moves.copy()
    #cube.moves.clear()
    #return movesLL