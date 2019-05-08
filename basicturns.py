"In this script, I'm going to define the functions which correspond to cube \
rotations and reorientations."

"The six faces of the cube are referred to as F=front, R=right, U=up, B=back, \
L=left, D=down. In algebraic notation, any of these six letters refers to a \
rotation of the corresponding face. For example, R = rotate R clockwise, R' = \
rotate R counterclockwise, and R2 = rotate R 180 degrees."

"There are also full cube re-orientations, given by x, y, and z which correspond \
to rotating the R, U, and F face clockwise without holding the rest of the cube \
constant. Similarly define x', y', z', x2, y2, z2. These won't be necessary but \
they might be useful later for efficiency."

"It will be assumed that the cube state is given as a 6-element list, \
and each of these elements is a 9-element list whose entries are drawn from \
the set {z, x, y, z', x', y'}. These six variables are supposed to represent \
the six colors on whatever cube you're using, and it's assumed that the mapping \
follows a right-handed convention. I'm going to imagine x means right, y means \
up, and z means coming out of the page."

"On my own Rubik's cube, I have x=white, y=red, z=blue, x'=yellow, y'=orange, \
z'=green (up to symmetries by the 24-element group of re-orientations, of course)."

"The order in which the 54 colors are given is very important. Here's going to \
be my convention. The six lists give the colors on the F, R, U, B, L, D faces, \
in that order. The reason for this is that if you sequentially re-orient the cube\
left, down, left, down, left, down then you will see the faces in precisely this\
order and end up back at the F face in the same orientation you started with."

"Within each face, the 9 panels will be given as on a phone dialpad, starting \
in the top left corner and proceeding along each row in turn."


"The following three functions tell us how to rotate a given face in 2d. The\
input is a 9-element list."
def Clockwisefaceturn(A):
    return [A[6],A[3],A[0],A[7],A[4],A[1],A[8],A[5],A[2]]
def Counterclockwisefaceturn(A):
    return [A[2],A[5],A[8],A[1],A[4],A[7],A[0],A[3],A[6]]
def Doublefaceturn(A):
    return [A[8],A[7],A[6],A[5],A[4],A[3],A[2],A[1],A[0]]

"The following is a full list of the 18 basic turn operations. Instead of just\
using the six generators, I've defined all 18 turns in order to make things faster."

"Some code we will have to keep using:"
#    B = []
#    B.append([A[0][0],A[0][1],A[0][2],A[0][3],A[0][4],A[0][5],A[0][6],A[0][7],A[0][8]])
#    B.append([A[1][0],A[1][1],A[1][2],A[1][3],A[1][4],A[1][5],A[1][6],A[1][7],A[1][8]])
#    B.append([A[2][0],A[2][1],A[2][2],A[2][3],A[2][4],A[2][5],A[2][6],A[2][7],A[2][8]])
#    B.append([A[3][0],A[3][1],A[3][2],A[3][3],A[3][4],A[3][5],A[3][6],A[3][7],A[3][8]])
#    B.append([A[4][0],A[4][1],A[4][2],A[4][3],A[4][4],A[4][5],A[4][6],A[4][7],A[4][8]])
#    B.append([A[5][0],A[5][1],A[5][2],A[5][3],A[5][4],A[5][5],A[5][6],A[5][7],A[5][8]])
def Fturn(A):
    B = []
    B.append(Clockwisefaceturn(A[0]))
    B.append([A[2][0],A[1][1],A[1][2],A[2][3],A[1][4],A[1][5],A[2][6],A[1][7],A[1][8]])
    B.append([A[4][2],A[2][1],A[2][2],A[4][1],A[2][4],A[2][5],A[4][0],A[2][7],A[2][8]])
    B.append(A[3])
    B.append([A[5][0],A[5][1],A[5][2],A[4][3],A[4][4],A[4][5],A[4][6],A[4][7],A[4][8]])
    B.append([A[1][6],A[1][3],A[1][0],A[5][3],A[5][4],A[5][5],A[5][6],A[5][7],A[5][8]])  
    return(B)

def Fprimeturn(A):
    B = []
    B.append(Counterclockwisefaceturn(A[0]))
    B.append([A[5][2],A[1][1],A[1][2],A[5][1],A[1][4],A[1][5],A[5][0],A[1][7],A[1][8]])
    B.append([A[1][0],A[2][1],A[2][2],A[1][3],A[2][4],A[2][5],A[1][6],A[2][7],A[2][8]])
    B.append(A[3])
    B.append([A[2][6],A[2][3],A[2][0],A[4][3],A[4][4],A[4][5],A[4][6],A[4][7],A[4][8]])
    B.append([A[4][0],A[4][1],A[4][2],A[5][3],A[5][4],A[5][5],A[5][6],A[5][7],A[5][8]])  
    return(B)

def F2turn(A):
    B = []
    B.append(Doublefaceturn(A[0]))
    B.append([A[4][2],A[1][1],A[1][2],A[4][1],A[1][4],A[1][5],A[4][0],A[1][7],A[1][8]])
    B.append([A[5][2],A[2][1],A[2][2],A[5][1],A[2][4],A[2][5],A[5][0],A[2][7],A[2][8]])
    B.append(A[3])
    B.append([A[1][6],A[1][3],A[1][0],A[4][3],A[4][4],A[4][5],A[4][6],A[4][7],A[4][8]])
    B.append([A[2][6],A[2][3],A[2][0],A[5][3],A[5][4],A[5][5],A[5][6],A[5][7],A[5][8]])  
    return(B)

def Rturn(A):
    B = []
    B.append([A[0][0],A[0][1],A[5][2],A[0][3],A[0][4],A[5][5],A[0][6],A[0][7],A[5][8]])
    B.append(Clockwisefaceturn(A[1]))
    B.append([A[2][0],A[2][1],A[2][2],A[2][3],A[2][4],A[2][5],A[0][8],A[0][5],A[0][2]])
    B.append([A[3][0],A[3][1],A[3][2],A[3][3],A[3][4],A[3][5],A[2][6],A[2][7],A[2][8]])
    B.append(A[4])
    B.append([A[5][0],A[5][1],A[3][8],A[5][3],A[5][4],A[3][7],A[5][6],A[5][7],A[3][6]])
    return(B)

def Rprimeturn(A):
    B = []
    B.append([A[0][0],A[0][1],A[2][8],A[0][3],A[0][4],A[2][7],A[0][6],A[0][7],A[2][6]])
    B.append(Counterclockwisefaceturn(A[1]))
    B.append([A[2][0],A[2][1],A[2][2],A[2][3],A[2][4],A[2][5],A[3][6],A[3][7],A[3][8]])
    B.append([A[3][0],A[3][1],A[3][2],A[3][3],A[3][4],A[3][5],A[5][8],A[5][5],A[5][2]])
    B.append(A[4])
    B.append([A[5][0],A[5][1],A[0][2],A[5][3],A[5][4],A[0][5],A[5][6],A[5][7],A[0][8]])
    return(B)

def R2turn(A):
    B = []
    B.append([A[0][0],A[0][1],A[3][8],A[0][3],A[0][4],A[3][7],A[0][6],A[0][7],A[3][6]])
    B.append(Doublefaceturn(A[1]))
    B.append([A[2][0],A[2][1],A[2][2],A[2][3],A[2][4],A[2][5],A[5][8],A[5][5],A[5][2]])
    B.append([A[3][0],A[3][1],A[3][2],A[3][3],A[3][4],A[3][5],A[0][8],A[0][5],A[0][2]])
    B.append(A[4])
    B.append([A[5][0],A[5][1],A[2][8],A[5][3],A[5][4],A[2][7],A[5][6],A[5][7],A[2][6]])
    return(B)

def Uturn(A):
    B = []
    B.append([A[1][0],A[1][1],A[1][2],A[0][3],A[0][4],A[0][5],A[0][6],A[0][7],A[0][8]])
    B.append([A[3][6],A[3][3],A[3][0],A[1][3],A[1][4],A[1][5],A[1][6],A[1][7],A[1][8]])
    B.append(Clockwisefaceturn(A[2]))
    B.append([A[4][0],A[3][1],A[3][2],A[4][3],A[3][4],A[3][5],A[4][6],A[3][7],A[3][8]])
    B.append([A[0][2],A[4][1],A[4][2],A[0][1],A[4][4],A[4][5],A[0][0],A[4][7],A[4][8]])
    B.append(A[5])
    return(B)

def Uprimeturn(A):
    B = []
    B.append([A[4][6],A[4][3],A[4][0],A[0][3],A[0][4],A[0][5],A[0][6],A[0][7],A[0][8]])
    B.append([A[0][0],A[0][1],A[0][2],A[1][3],A[1][4],A[1][5],A[1][6],A[1][7],A[1][8]])
    B.append(Counterclockwisefaceturn(A[2]))
    B.append([A[1][2],A[3][1],A[3][2],A[1][1],A[3][4],A[3][5],A[1][0],A[3][7],A[3][8]])
    B.append([A[3][0],A[4][1],A[4][2],A[3][3],A[4][4],A[4][5],A[3][6],A[4][7],A[4][8]])
    B.append(A[5])
    return(B)

def U2turn(A):
    B = []
    B.append([A[3][6],A[3][3],A[3][0],A[0][3],A[0][4],A[0][5],A[0][6],A[0][7],A[0][8]])
    B.append([A[4][6],A[4][3],A[4][0],A[1][3],A[1][4],A[1][5],A[1][6],A[1][7],A[1][8]])
    B.append(Doublefaceturn(A[2]))
    B.append([A[0][2],A[3][1],A[3][2],A[0][1],A[3][4],A[3][5],A[0][0],A[3][7],A[3][8]])
    B.append([A[1][2],A[4][1],A[4][2],A[1][1],A[4][4],A[4][5],A[1][0],A[4][7],A[4][8]])
    B.append(A[5])
    return(B)

def Bturn(A):
    B = []
    B.append(A[0])
    B.append([A[1][0],A[1][1],A[5][8],A[1][3],A[1][4],A[5][7],A[1][6],A[1][7],A[5][6]])
    B.append([A[2][0],A[2][1],A[1][2],A[2][3],A[2][4],A[1][5],A[2][6],A[2][7],A[1][8]])
    B.append(Clockwisefaceturn(A[3]))
    B.append([A[4][0],A[4][1],A[4][2],A[4][3],A[4][4],A[4][5],A[2][8],A[2][5],A[2][2]])
    B.append([A[5][0],A[5][1],A[5][2],A[5][3],A[5][4],A[5][5],A[4][6],A[4][7],A[4][8]])
    return(B)

def Bprimeturn(A):
    B = []
    B.append(A[0])
    B.append([A[1][0],A[1][1],A[2][2],A[1][3],A[1][4],A[2][5],A[1][6],A[1][7],A[2][8]])
    B.append([A[2][0],A[2][1],A[4][8],A[2][3],A[2][4],A[4][7],A[2][6],A[2][7],A[4][6]])
    B.append(Counterclockwisefaceturn(A[3]))
    B.append([A[4][0],A[4][1],A[4][2],A[4][3],A[4][4],A[4][5],A[5][6],A[5][7],A[5][8]])
    B.append([A[5][0],A[5][1],A[5][2],A[5][3],A[5][4],A[5][5],A[1][8],A[1][5],A[1][2]])
    return(B)

def B2turn(A):
    B = []
    B.append(A[0])
    B.append([A[1][0],A[1][1],A[4][8],A[1][3],A[1][4],A[4][7],A[1][6],A[1][7],A[4][6]])
    B.append([A[2][0],A[2][1],A[5][8],A[2][3],A[2][4],A[5][7],A[2][6],A[2][7],A[5][6]])
    B.append(Doublefaceturn(A[3]))
    B.append([A[4][0],A[4][1],A[4][2],A[4][3],A[4][4],A[4][5],A[1][8],A[1][5],A[1][2]])
    B.append([A[5][0],A[5][1],A[5][2],A[5][3],A[5][4],A[5][5],A[2][8],A[2][5],A[2][2]])
    return(B)

def Lturn(A):
    B = []
    B.append([A[2][2],A[0][1],A[0][2],A[2][1],A[0][4],A[0][5],A[2][0],A[0][7],A[0][8]])
    B.append(A[1])
    B.append([A[3][0],A[3][1],A[3][2],A[2][3],A[2][4],A[2][5],A[2][6],A[2][7],A[2][8]])
    B.append([A[5][6],A[5][3],A[5][0],A[3][3],A[3][4],A[3][5],A[3][6],A[3][7],A[3][8]])
    B.append(Clockwisefaceturn(A[4]))
    B.append([A[0][0],A[5][1],A[5][2],A[0][3],A[5][4],A[5][5],A[0][6],A[5][7],A[5][8]])
    return(B)

def Lprimeturn(A):
    B = []
    B.append([A[5][0],A[0][1],A[0][2],A[5][3],A[0][4],A[0][5],A[5][6],A[0][7],A[0][8]])
    B.append(A[1])
    B.append([A[0][6],A[0][3],A[0][0],A[2][3],A[2][4],A[2][5],A[2][6],A[2][7],A[2][8]])
    B.append([A[2][0],A[2][1],A[2][2],A[3][3],A[3][4],A[3][5],A[3][6],A[3][7],A[3][8]])
    B.append(Counterclockwisefaceturn(A[4]))
    B.append([A[3][2],A[5][1],A[5][2],A[3][1],A[5][4],A[5][5],A[3][0],A[5][7],A[5][8]])
    return(B)

def L2turn(A):
    B = []
    B.append([A[3][2],A[0][1],A[0][2],A[3][1],A[0][4],A[0][5],A[3][0],A[0][7],A[0][8]])
    B.append(A[1])
    B.append([A[5][6],A[5][3],A[5][0],A[2][3],A[2][4],A[2][5],A[2][6],A[2][7],A[2][8]])
    B.append([A[0][6],A[0][3],A[0][0],A[3][3],A[3][4],A[3][5],A[3][6],A[3][7],A[3][8]])
    B.append(Doublefaceturn(A[4]))
    B.append([A[2][2],A[5][1],A[5][2],A[2][1],A[5][4],A[5][5],A[2][0],A[5][7],A[5][8]])
    return(B)

def Dturn(A):
    B = []
    B.append([A[0][0],A[0][1],A[0][2],A[0][3],A[0][4],A[0][5],A[4][8],A[4][5],A[4][2]])
    B.append([A[1][0],A[1][1],A[1][2],A[1][3],A[1][4],A[1][5],A[0][6],A[0][7],A[0][8]])
    B.append(A[2])
    B.append([A[3][0],A[3][1],A[1][8],A[3][3],A[3][4],A[1][7],A[3][6],A[3][7],A[1][6]])
    B.append([A[4][0],A[4][1],A[3][2],A[4][3],A[4][4],A[3][5],A[4][6],A[4][7],A[3][8]])
    B.append(Clockwisefaceturn(A[5]))
    return(B)

def Dprimeturn(A):
    B = []
    B.append([A[0][0],A[0][1],A[0][2],A[0][3],A[0][4],A[0][5],A[1][6],A[1][7],A[1][8]])
    B.append([A[1][0],A[1][1],A[1][2],A[1][3],A[1][4],A[1][5],A[3][8],A[3][5],A[3][2]])
    B.append(A[2])
    B.append([A[3][0],A[3][1],A[4][2],A[3][3],A[3][4],A[4][5],A[3][6],A[3][7],A[4][8]])
    B.append([A[4][0],A[4][1],A[0][8],A[4][3],A[4][4],A[0][7],A[4][6],A[4][7],A[0][6]])
    B.append(Counterclockwisefaceturn(A[5]))
    return(B)

def D2turn(A):
    B = []
    B.append([A[0][0],A[0][1],A[0][2],A[0][3],A[0][4],A[0][5],A[3][8],A[3][5],A[3][2]])
    B.append([A[1][0],A[1][1],A[1][2],A[1][3],A[1][4],A[1][5],A[4][8],A[4][5],A[4][2]])
    B.append(A[2])
    B.append([A[3][0],A[3][1],A[0][8],A[3][3],A[3][4],A[0][7],A[3][6],A[3][7],A[0][6]])
    B.append([A[4][0],A[4][1],A[1][8],A[4][3],A[4][4],A[1][7],A[4][6],A[4][7],A[1][6]])
    B.append(Doublefaceturn(A[5]))
    return(B)

"Finally, here are the operations for re-orienting the cube."
