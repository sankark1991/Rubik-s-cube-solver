"This is version 2.0 of the cubstate script."

import collections

"Each face is stored as a named tuple."
Front = collections.namedtuple('Front', 'ul um ur ml mm mr dl dm dr')
Back = collections.namedtuple('Back', 'ul um ur ml mm mr dl dm dr')
Up = collections.namedtuple('Up', 'fl fm fr ml mm mr bl bm br')
Down = collections.namedtuple('Down', 'fl fm fr ml mm mr bl bm br')
Left = collections.namedtuple('Left', 'fu fm fd mu mm md bu bm bd')
Right = collections.namedtuple('Right', 'fu fm fd mu mm md bu bm bd')

"The list of faces is a named tuple whose names are the six face names."
Facelist = collections.namedtuple('Facelist', 'F B U D L R')

"The class cubestate is initialized with a list of faces. The benefit of creating\
this class is now I can define all of the methods like face turns, cube turns, \
edgefinds, and cornerfinds here."
class cubestate:
    
    def __init__(self, Facelist):
        self.F = Facelist.F
        self.B = Facelist.B
        self.U = Facelist.U
        self.D = Facelist.D
        self.L = Facelist.L
        self.R = Facelist.R
        self.moves = []
    "Method Fturn: Clockwise turn the front face."
    def Fturn(self):
        self.F = Front(ul=self.F.dl, um=self.F.ml, ur=self.F.ul, ml=self.F.dm, \
                      mm=self.F.mm, mr=self.F.um, dl=self.F.dr, dm=self.F.mr, \
                      dr=self.F.ur)
        dummy = [self.R.fu, self.R.fm, self.R.fd]
        self.R = Right(fu=self.U.fl, fm=self.U.fm, fd=self.U.fr, mu=self.R.mu,\
                       mm=self.R.mm, md=self.R.md, bu=self.R.bu, bm=self.R.bm, \
                       bd=self.R.bd)
        self.U = Up(fl=self.L.fd, fm=self.L.fm, fr=self.L.fu, ml=self.U.ml, \
                    mm=self.U.mm, mr=self.U.mr, bl=self.U.bl, bm=self.U.bm, \
                    br=self.U.br)
        self.L = Left(fu=self.D.fl, fm=self.D.fm, fd=self.D.fr, mu=self.L.mu,\
                       mm=self.L.mm, md=self.L.md, bu=self.L.bu, bm=self.L.bm, \
                       bd=self.L.bd)
        self.D = Down(fl=dummy[2], fm=dummy[1], fr=dummy[0], ml=self.D.ml, \
                    mm=self.D.mm, mr=self.D.mr, bl=self.D.bl, bm=self.D.bm, \
                    br=self.D.br)
        self.moves.append('F')
    "Method Fprimeturn: Counterclockwise turn the front face."
    def Fprimeturn(self):
        self.F = Front(dl=self.F.ul, ml=self.F.um, ul=self.F.ur, dm=self.F.ml, \
                     mm=self.F.mm, um=self.F.mr, dr=self.F.dl, mr=self.F.dm, \
                     ur=self.F.dr)
        dummy = [self.R.fu, self.R.fm, self.R.fd]
        self.R = Right(bu=self.R.bu, bm=self.R.bm, bd=self.R.bd, mu=self.R.mu,\
                       mm=self.R.mm, md=self.R.md, fu=self.D.fr, fm=self.D.fm, \
                       fd=self.D.fl)
        self.D = Down(bl=self.D.bl, bm=self.D.bm, br=self.D.br, ml=self.D.ml, \
                    mm=self.D.mm, mr=self.D.mr, fl=self.L.fu, fm=self.L.fm, \
                    fr=self.L.fd)
        self.L = Left(bu=self.L.bu, bm=self.L.bm, bd=self.L.bd, mu=self.L.mu,\
                       mm=self.L.mm, md=self.L.md, fu=self.U.fr, fm=self.U.fm, \
                       fd=self.U.fl)
        self.U = Up(bl=self.U.bl, bm=self.U.bm, br=self.U.br, ml=self.U.ml, \
                    mm=self.U.mm, mr=self.U.mr, fl=dummy[0], fm=dummy[1], \
                    fr=dummy[2])
        self.moves.extend(['F', 'F', 'F'])
    "Method F2turn: Double turn the front face."
    def F2turn(self):
        self.F = Front(ul=self.F.dr, um=self.F.dm, ur=self.F.dl, ml=self.F.mr, \
                       mm=self.F.mm, mr=self.F.ml, dl=self.F.ur, dm=self.F.um, \
                       dr=self.F.ul)
        dummy = [self.R.fu, self.R.fm, self.R.fd]
        self.R = Right(fu=self.L.fd, fm=self.L.fm, fd=self.L.fu, mu=self.R.mu,\
                       mm=self.R.mm, md=self.R.md, bu=self.R.bu, bm=self.R.bm, \
                       bd=self.R.bd)
        self.L = Left(fu=dummy[2], fm=dummy[1], fd=dummy[0], mu=self.L.mu,\
                      mm=self.L.mm, md=self.L.md, bu=self.L.bu, bm=self.L.bm, \
                      bd=self.L.bd)
        dummy = [self.U.fl, self.U.fm, self.U.fr]
        self.U = Up(fl=self.D.fr, fm=self.D.fm, fr=self.D.fl, ml=self.U.ml, \
                    mm=self.U.mm, mr=self.U.mr, bl=self.U.bl, bm=self.U.bm, \
                    br=self.U.br)
        self.D = Down(fl=dummy[2], fm=dummy[1], fr=dummy[0], ml=self.D.ml, \
                      mm=self.D.mm, mr=self.D.mr, bl=self.D.bl, bm=self.D.bm, \
                      br=self.D.br)
        self.moves.extend(['F', 'F'])
    "Method Bturn: Clockwise turn the back face."
    def Bturn(self):
        self.B = Back(dl=self.B.ul, ml=self.B.um, ul=self.B.ur, dm=self.B.ml, \
                     mm=self.B.mm, um=self.B.mr, dr=self.B.dl, mr=self.B.dm, \
                     ur=self.B.dr)
        dummy = [self.R.bu, self.R.bm, self.R.bd]
        self.R = Right(fu=self.R.fu, fm=self.R.fm, fd=self.R.fd, mu=self.R.mu,\
                       mm=self.R.mm, md=self.R.md, bu=self.D.br, bm=self.D.bm, \
                       bd=self.D.bl)
        self.D = Down(fl=self.D.fl, fm=self.D.fm, fr=self.D.fr, ml=self.D.ml, \
                    mm=self.D.mm, mr=self.D.mr, bl=self.L.bu, bm=self.L.bm, \
                    br=self.L.bd)
        self.L = Left(fu=self.L.fu, fm=self.L.fm, fd=self.L.fd, mu=self.L.mu,\
                       mm=self.L.mm, md=self.L.md, bu=self.U.br, bm=self.U.bm, \
                       bd=self.U.bl)
        self.U = Up(fl=self.U.fl, fm=self.U.fm, fr=self.U.fr, ml=self.U.ml, \
                    mm=self.U.mm, mr=self.U.mr, bl=dummy[0], bm=dummy[1], \
                    br=dummy[2])
        self.moves.extend(['B'])
    "Method Bprimeturn: Counterclockwise turn the back face."
    def Bprimeturn(self):
        self.B = Back(ul=self.B.dl, um=self.B.ml, ur=self.B.ul, ml=self.B.dm, \
                      mm=self.B.mm, mr=self.B.um, dl=self.B.dr, dm=self.B.mr, \
                      dr=self.B.ur)
        dummy = [self.R.bu, self.R.bm, self.R.bd]
        self.R = Right(bu=self.U.bl, bm=self.U.bm, bd=self.U.br, mu=self.R.mu,\
                       mm=self.R.mm, md=self.R.md, fu=self.R.fu, fm=self.R.fm, \
                       fd=self.R.fd)
        self.U = Up(bl=self.L.bd, bm=self.L.bm, br=self.L.bu, ml=self.U.ml, \
                    mm=self.U.mm, mr=self.U.mr, fl=self.U.fl, fm=self.U.fm, \
                    fr=self.U.fr)
        self.L = Left(bu=self.D.bl, bm=self.D.bm, bd=self.D.br, mu=self.L.mu,\
                       mm=self.L.mm, md=self.L.md, fu=self.L.fu, fm=self.L.fm, \
                       fd=self.L.fd)
        self.D = Down(bl=dummy[2], bm=dummy[1], br=dummy[0], ml=self.D.ml, \
                    mm=self.D.mm, mr=self.D.mr, fl=self.D.fl, fm=self.D.fm, \
                    fr=self.D.fr)
        self.moves.extend(['B', 'B', 'B'])
    "Method B2turn: Double turn the back face."
    def B2turn(self):
        self.B = Back(dl=self.B.ur, ml=self.B.mr, ul=self.B.dr, dm=self.B.um, \
                     mm=self.B.mm, um=self.B.dm, dr=self.B.ul, mr=self.B.ml, \
                     ur=self.B.dl)
        dummy = [self.R.bu, self.R.bm, self.R.bd]
        self.R = Right(fu=self.R.fu, fm=self.R.fm, fd=self.R.fd, mu=self.R.mu,\
                       mm=self.R.mm, md=self.R.md, bu=self.L.bd, bm=self.L.bm, \
                       bd=self.L.bu)
        self.L = Left(fu=self.L.fu, fm=self.L.fm, fd=self.L.fd, mu=self.L.mu,\
                       mm=self.L.mm, md=self.L.md, bu=dummy[2], bm=dummy[1], \
                       bd=dummy[0])
        dummy = [self.D.bl, self.D.bm, self.D.br]
        self.D = Down(fl=self.D.fl, fm=self.D.fm, fr=self.D.fr, ml=self.D.ml, \
                    mm=self.D.mm, mr=self.D.mr, bl=self.U.br, bm=self.U.bm, \
                    br=self.U.bl)
        self.U = Up(fl=self.U.fl, fm=self.U.fm, fr=self.U.fr, ml=self.U.ml, \
                    mm=self.U.mm, mr=self.U.mr, bl=dummy[2], bm=dummy[1], \
                    br=dummy[0])
        self.moves.extend(['B', 'B'])    
    "Method Rturn: Clockwise turn the right face."
    def Rturn(self):
        self.R = Right(fu=self.R.fd, fm=self.R.md, fd=self.R.bd, mu=self.R.fm, \
                      mm=self.R.mm, md=self.R.bm, bu=self.R.fu, bm=self.R.mu, \
                      bd=self.R.bu)
        dummy = [self.F.dr, self.F.mr, self.F.ur]
        self.F = Front(ul=self.F.ul, ml=self.F.ml, dl=self.F.dl, um=self.F.um, \
                       mm=self.F.mm, dm=self.F.dm, ur=self.D.fr, mr=self.D.mr, \
                       dr=self.D.br)
        self.D = Down(fl=self.D.fl, ml=self.D.ml, bl=self.D.bl, fm=self.D.fm, \
                      mm=self.D.mm, bm=self.D.bm, fr=self.B.dr, mr=self.B.mr, \
                      br=self.B.ur)
        self.B = Back(ul=self.B.ul, ml=self.B.ml, dl=self.B.dl, um=self.B.um, \
                      mm=self.B.mm, dm=self.B.dm, ur=self.U.fr, mr=self.U.mr, \
                      dr=self.U.br)
        self.U = Up(fl=self.U.fl, ml=self.U.ml, bl=self.U.bl, fm=self.U.fm, \
                    mm=self.U.mm, bm=self.U.bm, fr=dummy[0], mr=dummy[1], br=dummy[2])
        self.moves.append('R')
    "Method Rprimeturn: Counterclockwise turn the right face."
    def Rprimeturn(self):
        self.R = Right(fd=self.R.fu, md=self.R.fm, bd=self.R.fd, fm=self.R.mu, \
                     mm=self.R.mm, bm=self.R.md, fu=self.R.bu, mu=self.R.bm, \
                     bu=self.R.bd)
        dummy = [self.F.ur, self.F.mr, self.F.dr]
        self.F = Front(ul=self.F.ul, ml=self.F.ml, dl=self.F.dl, um=self.F.um, \
                       mm=self.F.mm, dm=self.F.dm, ur=self.U.br, mr=self.U.mr, \
                       dr=self.U.fr)
        self.U = Up(fl=self.U.fl, ml=self.U.ml, bl=self.U.bl, fm=self.U.fm, \
                    mm=self.U.mm, bm=self.U.bm, fr=self.B.ur, mr=self.B.mr, br=self.B.dr)
        self.B = Back(ul=self.B.ul, ml=self.B.ml, dl=self.B.dl, um=self.B.um, \
                      mm=self.B.mm, dm=self.B.dm, ur=self.D.br, mr=self.D.mr, \
                      dr=self.D.fr)
        self.D = Down(fl=self.D.fl, ml=self.D.ml, bl=self.D.bl, fm=self.D.fm, \
                      mm=self.D.mm, bm=self.D.bm, fr=dummy[0], mr=dummy[1], br=dummy[2])
        self.moves.extend(['R','R','R'])
    "Method R2turn: Double turn the right face."
    def R2turn(self):
        self.R = Right(fd=self.R.bu, md=self.R.mu, bd=self.R.fu, fm=self.R.bm, \
                     mm=self.R.mm, bm=self.R.fm, fu=self.R.bd, mu=self.R.md, \
                     bu=self.R.fd)
        dummy = [self.F.ur, self.F.mr, self.F.dr]
        self.F = Front(ul=self.F.ul, ml=self.F.ml, dl=self.F.dl, um=self.F.um, \
                       mm=self.F.mm, dm=self.F.dm, ur=self.B.dr, mr=self.B.mr, \
                       dr=self.B.ur)
        self.B = Back(ul=self.B.ul, ml=self.B.ml, dl=self.B.dl, um=self.B.um, \
                      mm=self.B.mm, dm=self.B.dm, ur=dummy[2], mr=dummy[1], \
                      dr=dummy[0])
        dummy = [self.U.fr, self.U.mr, self.U.br]
        self.U = Up(fl=self.U.fl, ml=self.U.ml, bl=self.U.bl, fm=self.U.fm, \
                    mm=self.U.mm, bm=self.U.bm, fr=self.D.br, mr=self.D.mr, \
                    br=self.D.fr)   
        self.D = Down(fl=self.D.fl, ml=self.D.ml, bl=self.D.bl, fm=self.D.fm, \
                      mm=self.D.mm, bm=self.D.bm, fr=dummy[2], mr=dummy[1], \
                      br=dummy[0])
        self.moves.extend(['R','R'])
    "Method Lturn: Clockwise turn the left face."
    def Lturn(self):
        self.L = Left(fd=self.L.fu, md=self.L.fm, bd=self.L.fd, fm=self.L.mu, \
                     mm=self.L.mm, bm=self.L.md, fu=self.L.bu, mu=self.L.bm, \
                     bu=self.L.bd)
        dummy = [self.F.ul, self.F.ml, self.F.dl]
        self.F = Front(ur=self.F.ur, mr=self.F.mr, dr=self.F.dr, um=self.F.um, \
                       mm=self.F.mm, dm=self.F.dm, ul=self.U.bl, ml=self.U.ml, \
                       dl=self.U.fl)
        self.U = Up(fr=self.U.fr, mr=self.U.mr, br=self.U.br, fm=self.U.fm, \
                    mm=self.U.mm, bm=self.U.bm, fl=self.B.ul, ml=self.B.ml, bl=self.B.dl)
        self.B = Back(ur=self.B.ur, mr=self.B.mr, dr=self.B.dr, um=self.B.um, \
                      mm=self.B.mm, dm=self.B.dm, ul=self.D.bl, ml=self.D.ml, \
                      dl=self.D.fl)
        self.D = Down(fr=self.D.fr, mr=self.D.mr, br=self.D.br, fm=self.D.fm, \
                      mm=self.D.mm, bm=self.D.bm, fl=dummy[0], ml=dummy[1], bl=dummy[2])
        self.moves.append('L')
    "Method Lprimeturn: Counterclockwise turn the left face."
    def Lprimeturn(self):
        self.L = Left(fu=self.L.fd, fm=self.L.md, fd=self.L.bd, mu=self.L.fm, \
                      mm=self.L.mm, md=self.L.bm, bu=self.L.fu, bm=self.L.mu, \
                      bd=self.L.bu)
        dummy = [self.F.dl, self.F.ml, self.F.ul]
        self.F = Front(ur=self.F.ur, mr=self.F.mr, dr=self.F.dr, um=self.F.um, \
                       mm=self.F.mm, dm=self.F.dm, ul=self.D.fl, ml=self.D.ml, \
                       dl=self.D.bl)
        self.D = Down(fr=self.D.fr, mr=self.D.mr, br=self.D.br, fm=self.D.fm, \
                      mm=self.D.mm, bm=self.D.bm, fl=self.B.dl, ml=self.B.ml, \
                      bl=self.B.ul)
        self.B = Back(ur=self.B.ur, mr=self.B.mr, dr=self.B.dr, um=self.B.um, \
                      mm=self.B.mm, dm=self.B.dm, ul=self.U.fl, ml=self.U.ml, \
                      dl=self.U.bl)
        self.U = Up(fr=self.U.fr, mr=self.U.mr, br=self.U.br, fm=self.U.fm, \
                    mm=self.U.mm, bm=self.U.bm, fl=dummy[0], ml=dummy[1], bl=dummy[2])
        self.moves.extend(['L','L','L'])
    "Method L2turn: Double turn the left face."
    def L2turn(self):
        self.L = Left(fu=self.L.bd, fm=self.L.bm, fd=self.L.bu, mu=self.L.md, \
                      mm=self.L.mm, md=self.L.mu, bu=self.L.fd, bm=self.L.fm, \
                      bd=self.L.fu)
        dummy = [self.F.ul, self.F.ml, self.F.dl]
        self.F = Front(ur=self.F.ur, mr=self.F.mr, dr=self.F.dr, um=self.F.um, \
                       mm=self.F.mm, dm=self.F.dm, ul=self.B.dl, ml=self.B.ml, \
                       dl=self.B.ul)
        self.B = Back(ur=self.B.ur, mr=self.B.mr, dr=self.B.dr, um=self.B.um, \
                      mm=self.B.mm, dm=self.B.dm, ul=dummy[2], ml=dummy[1], \
                      dl=dummy[0])
        dummy = [self.D.fl, self.D.ml, self.D.bl]
        self.D = Down(fr=self.D.fr, mr=self.D.mr, br=self.D.br, fm=self.D.fm, \
                      mm=self.D.mm, bm=self.D.bm, fl=self.U.bl, ml=self.U.ml, \
                      bl=self.U.fl)
        self.U = Up(fr=self.U.fr, mr=self.U.mr, br=self.U.br, fm=self.U.fm, \
                    mm=self.U.mm, bm=self.U.bm, fl=dummy[2], ml=dummy[1], \
                    bl=dummy[0])
        self.moves.extend(['L','L'])
    "Method Uturn: Clockwise turn the up face."
    def Uturn(self):
        self.U = Up(fl=self.U.fr, ml=self.U.fm, bl=self.U.fl, fm=self.U.mr, \
                   mm=self.U.mm, bm=self.U.ml, fr=self.U.br, mr=self.U.bm, \
                   br=self.U.bl)
        dummy = [self.F.ul, self.F.um, self.F.ur]
        self.F = Front(dl=self.F.dl, dm=self.F.dm, dr=self.F.dr, ml=self.F.ml, \
                       mm=self.F.mm, mr=self.F.mr, ul=self.R.fu, um=self.R.mu, \
                       ur=self.R.bu)
        self.R = Right(fd=self.R.fd, md=self.R.md, bd=self.R.bd, fm=self.R.fm, \
                       mm=self.R.mm, bm=self.R.bm, fu=self.B.ur, mu=self.B.um, \
                       bu=self.B.ul)
        self.B = Back(dl=self.B.dl, dm=self.B.dm, dr=self.B.dr, ml=self.B.ml, \
                       mm=self.B.mm, mr=self.B.mr, ul=self.L.fu, um=self.L.mu, \
                       ur=self.L.bu)
        self.L = Left(fd=self.L.fd, md=self.L.md, bd=self.L.bd, fm=self.L.fm, \
                       mm=self.L.mm, bm=self.L.bm, fu=dummy[2], mu=dummy[1], \
                       bu=dummy[0])
        self.moves.append('U')
    "Method Uprimeturn: Counterclockwise turn the up face."
    def Uprimeturn(self):
        self.U = Up(fr=self.U.fl, fm=self.U.ml, fl=self.U.bl, mr=self.U.fm, \
                     mm=self.U.mm, ml=self.U.bm, br=self.U.fr, bm=self.U.mr, \
                     bl=self.U.br)
        dummy = [self.F.ul, self.F.um, self.F.ur]
        self.F = Front(dl=self.F.dl, dm=self.F.dm, dr=self.F.dr, ml=self.F.ml, \
                       mm=self.F.mm, mr=self.F.mr, ul=self.L.bu, um=self.L.mu, \
                       ur=self.L.fu)
        self.L = Left(fd=self.L.fd, md=self.L.md, bd=self.L.bd, fm=self.L.fm, \
                      mm=self.L.mm, bm=self.L.bm, fu=self.B.ul, mu=self.B.um, \
                      bu=self.B.ur)
        self.B = Back(dl=self.B.dl, dm=self.B.dm, dr=self.B.dr, ml=self.B.ml, \
                       mm=self.B.mm, mr=self.B.mr, ul=self.R.bu, um=self.R.mu, \
                       ur=self.R.fu)
        self.R = Right(fd=self.R.fd, md=self.R.md, bd=self.R.bd, fm=self.R.fm, \
                      mm=self.R.mm, bm=self.R.bm, fu=dummy[0], mu=dummy[1], \
                      bu=dummy[2])
        self.moves.extend(['U','U','U'])
    "Method U2turn: Double turn the up face."
    def U2turn(self):
        self.U = Up(fr=self.U.bl, fm=self.U.bm, fl=self.U.br, mr=self.U.ml, \
                     mm=self.U.mm, ml=self.U.mr, br=self.U.fl, bm=self.U.fm, \
                     bl=self.U.fr)
        dummy = [self.F.ul, self.F.um, self.F.ur]
        self.F = Front(dl=self.F.dl, dm=self.F.dm, dr=self.F.dr, ml=self.F.ml, \
                       mm=self.F.mm, mr=self.F.mr, ul=self.B.ur, um=self.B.um, \
                       ur=self.B.ul)
        self.B = Back(dl=self.B.dl, dm=self.B.dm, dr=self.B.dr, ml=self.B.ml, \
                       mm=self.B.mm, mr=self.B.mr, ul=dummy[2], um=dummy[1], \
                       ur=dummy[0])
        dummy = [self.L.fu, self.L.mu, self.L.bu]
        self.L = Left(fd=self.L.fd, md=self.L.md, bd=self.L.bd, fm=self.L.fm, \
                      mm=self.L.mm, bm=self.L.bm, fu=self.R.bu, mu=self.R.mu, \
                      bu=self.R.fu)      
        self.R = Right(fd=self.R.fd, md=self.R.md, bd=self.R.bd, fm=self.R.fm, \
                      mm=self.R.mm, bm=self.R.bm, fu=dummy[2], mu=dummy[1], \
                      bu=dummy[0])
        self.moves.extend(['U','U'])
    "Method Dturn: Clockwise turn the down face."
    def Dturn(self):
        self.D = Down(fr=self.D.fl, fm=self.D.ml, fl=self.D.bl, mr=self.D.fm, \
                     mm=self.D.mm, ml=self.D.bm, br=self.D.fr, bm=self.D.mr, \
                     bl=self.D.br)
        dummy = [self.F.dl, self.F.dm, self.F.dr]
        self.F = Front(ul=self.F.ul, um=self.F.um, ur=self.F.ur, ml=self.F.ml, \
                       mm=self.F.mm, mr=self.F.mr, dl=self.L.bd, dm=self.L.md, \
                       dr=self.L.fd)
        self.L = Left(fu=self.L.fu, mu=self.L.mu, bu=self.L.bu, fm=self.L.fm, \
                      mm=self.L.mm, bm=self.L.bm, fd=self.B.dl, md=self.B.dm, \
                      bd=self.B.dr)
        self.B = Back(ul=self.B.ul, um=self.B.um, ur=self.B.ur, ml=self.B.ml, \
                       mm=self.B.mm, mr=self.B.mr, dl=self.R.bd, dm=self.R.md, \
                       dr=self.R.fd)
        self.R = Right(fu=self.R.fu, mu=self.R.mu, bu=self.R.bu, fm=self.R.fm, \
                      mm=self.R.mm, bm=self.R.bm, fd=dummy[0], md=dummy[1], \
                      bd=dummy[2])
        self.moves.append('D')
    "Method Dprimeturn: Counterclockwise turn the down face."
    def Dprimeturn(self):
        self.D = Down(fl=self.D.fr, ml=self.D.fm, bl=self.D.fl, fm=self.D.mr, \
                   mm=self.D.mm, bm=self.D.ml, fr=self.D.br, mr=self.D.bm, \
                   br=self.D.bl)
        dummy = [self.F.dl, self.F.dm, self.F.dr]
        self.F = Front(ul=self.F.ul, um=self.F.um, ur=self.F.ur, ml=self.F.ml, \
                       mm=self.F.mm, mr=self.F.mr, dl=self.R.fd, dm=self.R.md, \
                       dr=self.R.bd)
        self.R = Right(fu=self.R.fu, mu=self.R.mu, bu=self.R.bu, fm=self.R.fm, \
                       mm=self.R.mm, bm=self.R.bm, fd=self.B.dr, md=self.B.dm, \
                       bd=self.B.dl)
        self.B = Back(ul=self.B.ul, um=self.B.um, ur=self.B.ur, ml=self.B.ml, \
                       mm=self.B.mm, mr=self.B.mr, dl=self.L.fd, dm=self.L.md, \
                       dr=self.L.bd)
        self.L = Left(fu=self.L.fu, mu=self.L.mu, bu=self.L.bu, fm=self.L.fm, \
                       mm=self.L.mm, bm=self.L.bm, fd=dummy[2], md=dummy[1], \
                       bd=dummy[0])
        self.moves.extend(['D','D','D'])
    "Method D2turn: Double turn the down face."
    def D2turn(self):
        self.D = Down(fl=self.D.br, ml=self.D.mr, bl=self.D.fr, fm=self.D.bm, \
                   mm=self.D.mm, bm=self.D.fm, fr=self.D.bl, mr=self.D.ml, \
                   br=self.D.fl)
        dummy = [self.F.dl, self.F.dm, self.F.dr]
        self.F = Front(ul=self.F.ul, um=self.F.um, ur=self.F.ur, ml=self.F.ml, \
                       mm=self.F.mm, mr=self.F.mr, dl=self.B.dr, dm=self.B.dm, \
                       dr=self.B.dl)
        self.B = Back(ul=self.B.ul, um=self.B.um, ur=self.B.ur, ml=self.B.ml, \
                       mm=self.B.mm, mr=self.B.mr, dl=dummy[2], dm=dummy[1], \
                       dr=dummy[0])
        dummy = [self.R.fd, self.R.md, self.R.bd]
        self.R = Right(fu=self.R.fu, mu=self.R.mu, bu=self.R.bu, fm=self.R.fm, \
                       mm=self.R.mm, bm=self.R.bm, fd=self.L.bd, md=self.L.md, \
                       bd=self.L.fd)        
        self.L = Left(fu=self.L.fu, mu=self.L.mu, bu=self.L.bu, fm=self.L.fm, \
                       mm=self.L.mm, bm=self.L.bm, fd=dummy[2], md=dummy[1], \
                       bd=dummy[0])
        self.moves.extend(['D','D'])
    "Method FtoUturn: Rotates the whole cube so that the current F face becomes\
    the U face."
    def FtoUturn(self):
        self.L = Left(fu=self.L.fd, fm=self.L.md, fd=self.L.bd, mu=self.L.fm, \
                      mm=self.L.mm, md=self.L.bm, bu=self.L.fu, bm=self.L.mu, \
                      bd=self.L.bu)
        dummy = Right(fu=self.R.fd, fm=self.R.md, fd=self.R.bd, mu=self.R.fm, \
                      mm=self.R.mm, md=self.R.bm, bu=self.R.fu, bm=self.R.mu, \
                      bd=self.R.bu)
        self.R = dummy
        dummy = Down(fl=self.B.dl, fm=self.B.dm, fr=self.B.dr, ml=self.B.ml, \
                    mm=self.B.mm, mr=self.B.mr, bl=self.B.ul, bm=self.B.um, \
                    br=self.B.ur)
        self.B = Back(ul=self.U.fl, um=self.U.fm, ur=self.U.fr, ml=self.U.ml, \
                      mm=self.U.mm, mr=self.U.mr, dl=self.U.bl, dm=self.U.bm, \
                      dr=self.U.br)
        self.U = Up(fl=self.F.dl, fm=self.F.dm, fr=self.F.dr, ml=self.F.ml, \
                    mm=self.F.mm, mr=self.F.mr, bl=self.F.ul, bm=self.F.um, \
                    br=self.F.ur)
        self.F = Front(ul=self.D.fl, um=self.D.fm, ur=self.D.fr, ml=self.D.ml, \
                      mm=self.D.mm, mr=self.D.mr, dl=self.D.bl, dm=self.D.bm, \
                      dr=self.D.br) 
        self.D = dummy
        self.moves.append('x')
    "Method FtoDturn: Rotates the whole cube so that the current F face becomes\
    the D face."
    def FtoDturn(self):
        self.L = Left(fd=self.L.fu, md=self.L.fm, bd=self.L.fd, fm=self.L.mu, \
                     mm=self.L.mm, bm=self.L.md, fu=self.L.bu, mu=self.L.bm, \
                     bu=self.L.bd)
        self.R = Right(fd=self.R.fu, md=self.R.fm, bd=self.R.fd, fm=self.R.mu, \
                     mm=self.R.mm, bm=self.R.md, fu=self.R.bu, mu=self.R.bm, \
                     bu=self.R.bd)
        dummy = Up(bl=self.B.dl, bm=self.B.dm, br=self.B.dr, ml=self.B.ml, \
                    mm=self.B.mm, mr=self.B.mr, fl=self.B.ul, fm=self.B.um, \
                    fr=self.B.ur)
        self.B = Back(ul=self.D.bl, um=self.D.bm, ur=self.D.br, ml=self.D.ml, \
                      mm=self.D.mm, mr=self.D.mr, dl=self.D.fl, dm=self.D.fm, \
                      dr=self.D.fr)
        self.D = Down(bl=self.F.dl, bm=self.F.dm, br=self.F.dr, ml=self.F.ml, \
                    mm=self.F.mm, mr=self.F.mr, fl=self.F.ul, fm=self.F.um, \
                    fr=self.F.ur)
        self.F = Front(ul=self.U.bl, um=self.U.bm, ur=self.U.br, ml=self.U.ml, \
                      mm=self.U.mm, mr=self.U.mr, dl=self.U.fl, dm=self.U.fm, \
                      dr=self.U.fr) 
        self.U = dummy
        self.moves.append('x`')
    "Method FtoLturn: Rotates the whole cube so that the current F face becomes\
    the L face."
    def FtoLturn(self):
        self.U = Up(fl=self.U.fr, ml=self.U.fm, bl=self.U.fl, fm=self.U.mr, \
                   mm=self.U.mm, bm=self.U.ml, fr=self.U.br, mr=self.U.bm, \
                   br=self.U.bl)
        self.D = Down(fl=self.D.fr, ml=self.D.fm, bl=self.D.fl, fm=self.D.mr, \
                   mm=self.D.mm, bm=self.D.ml, fr=self.D.br, mr=self.D.bm, \
                   br=self.D.bl)
        dummy = Front(ul=self.R.fu, um=self.R.mu, ur=self.R.bu, ml=self.R.fm, \
                      mm=self.R.mm, mr=self.R.bm, dl=self.R.fd, dm=self.R.md, \
                      dr=self.R.bd)
        self.R = Right(fu=self.B.ur, mu=self.B.um, bu=self.B.ul, fm=self.B.mr, \
                       mm=self.B.mm, bm=self.B.ml, fd=self.B.dr, md=self.B.dm, \
                       bd=self.B.dl)
        self.B = Back(ul=self.L.fu, um=self.L.mu, ur=self.L.bu, ml=self.L.fm, \
                      mm=self.L.mm, mr=self.L.bm, dl=self.L.fd, dm=self.L.md, \
                      dr=self.L.bd)
        self.L = Left(fu=self.F.ur, mu=self.F.um, bu=self.F.ul, fm=self.F.mr, \
                      mm=self.F.mm, bm=self.F.ml, fd=self.F.dr, md=self.F.dm, \
                      bd=self.F.dl)
        self.F = dummy
        self.moves.append('y')
    "Method FtoRturn: Rotates the whole cube so that the current F face becomes\
    the R face."
    def FtoRturn(self):
        self.U = Up(fr=self.U.fl, fm=self.U.ml, fl=self.U.bl, mr=self.U.fm, \
                     mm=self.U.mm, ml=self.U.bm, br=self.U.fr, bm=self.U.mr, \
                     bl=self.U.br)
        self.D = Down(fr=self.D.fl, fm=self.D.ml, fl=self.D.bl, mr=self.D.fm, \
                     mm=self.D.mm, ml=self.D.bm, br=self.D.fr, bm=self.D.mr, \
                     bl=self.D.br)
        dummy = Front(ul=self.L.bu, um=self.L.mu, ur=self.L.fu, ml=self.L.bm, \
                      mm=self.L.mm, mr=self.L.fm, dl=self.L.bd, dm=self.L.md, \
                      dr=self.L.fd)
        self.L = Left(fu=self.B.ul, mu=self.B.um, bu=self.B.ur, fm=self.B.ml, \
                       mm=self.B.mm, bm=self.B.mr, fd=self.B.dl, md=self.B.dm, \
                       bd=self.B.dr)
        self.B = Back(ul=self.R.bu, um=self.R.mu, ur=self.R.fu, ml=self.R.bm, \
                      mm=self.R.mm, mr=self.R.fm, dl=self.R.bd, dm=self.R.md, \
                      dr=self.R.fd)
        self.R = Right(fu=self.F.ul, mu=self.F.um, bu=self.F.ur, fm=self.F.ml, \
                      mm=self.F.mm, bm=self.F.mr, fd=self.F.dl, md=self.F.dm, \
                      bd=self.F.dr)
        self.F = dummy
        self.moves.append('y`')
        
        
        
    "Method edgefind: Find the edge with the input labels x and y."
    def edgefind(self, x, y):
        if self.F.mr == x and self.R.fm == y:
            return ['F', 'R']
        if self.F.ml == x and self.L.fm == y:
            return ['F', 'L']
        if self.F.um == x and self.U.fm == y:
            return ['F', 'U']
        if self.F.dm == x and self.D.fm == y:
            return ['F', 'D']
        if self.B.mr == x and self.R.bm == y:
            return ['B', 'R']
        if self.B.ml == x and self.L.bm == y:
            return ['B', 'L']
        if self.B.um == x and self.U.bm == y:
            return ['B', 'U']
        if self.B.dm == x and self.D.bm == y:
            return ['B', 'D']
        
        if self.U.fm == x and self.F.um == y:
            return ['U', 'F']
        if self.U.bm == x and self.B.um == y:
            return ['U', 'B']
        if self.U.mr == x and self.R.mu == y:
            return ['U', 'R']
        if self.U.ml == x and self.L.mu == y:
            return ['U', 'L']
        if self.D.fm == x and self.F.dm == y:
            return ['D', 'F']
        if self.D.bm == x and self.B.dm == y:
            return ['D', 'B']
        if self.D.mr == x and self.R.md == y:
            return ['D', 'R']
        if self.D.ml == x and self.L.md == y:
            return ['D', 'L']
        
        if self.L.fm == x and self.F.ml == y:
            return ['L', 'F']
        if self.L.bm == x and self.B.ml == y:
            return ['L', 'B']
        if self.L.mu == x and self.U.ml == y:
            return ['L', 'U']
        if self.L.md == x and self.D.ml == y:
            return ['L', 'D']
        if self.R.fm == x and self.F.mr == y:
            return ['R', 'F']
        if self.R.bm == x and self.B.mr == y:
            return ['R', 'B']
        if self.R.mu == x and self.U.mr == y:
            return ['R', 'U']
        if self.R.md == x and self.D.mr == y:
            return ['R', 'D']
        
    "Method cornerfind: Find the corner with the input labels x, y, and z."
    def cornerfind(self, x, y, z):
        if self.F.ur == x and self.R.fu == y and self.U.fr == z:
            return ['F','R','U']
        if self.F.dr == x and self.R.fd == y and self.D.fr == z:
            return ['F','R','D']
        if self.F.ul == x and self.L.fu == y and self.U.fl == z:
            return ['F','L','U']
        if self.F.dl == x and self.L.fd == y and self.D.fl == z:
            return ['F','L','D']
        if self.F.ur == x and self.U.fr == y and self.R.fu == z:
            return ['F','U','R']
        if self.F.dr == x and self.D.fr == y and self.R.fd == z:
            return ['F','D','R']
        if self.F.ul == x and self.U.fl == y and self.L.fu == z:
            return ['F','U','L']
        if self.F.dl == x and self.D.fl == y and self.L.fd == z:
            return ['F','D','L']
        if self.B.ur == x and self.R.bu == y and self.U.br == z:
            return ['B','R','U']
        if self.B.dr == x and self.R.bd == y and self.D.br == z:
            return ['B','R','D']
        if self.B.ul == x and self.L.bu == y and self.U.bl == z:
            return ['B','L','U']
        if self.B.dl == x and self.L.bd == y and self.D.bl == z:
            return ['B','L','D']
        if self.B.ur == x and self.U.br == y and self.R.bu == z:
            return ['B','U','R']
        if self.B.dr == x and self.D.br == y and self.R.bd == z:
            return ['B','D','R']
        if self.B.ul == x and self.U.bl == y and self.L.bu == z:
            return ['B','U','L']
        if self.B.dl == x and self.D.bl == y and self.L.bd == z:
            return ['B','D','L']
        
        if self.U.fr == x and self.F.ur == y and self.R.fu == z:
            return ['U','F','R']
        if self.U.fl == x and self.F.ul == y and self.L.fu == z:
            return ['U','F','L']
        if self.U.br == x and self.B.ur == y and self.R.bu == z:
            return ['U','B','R']
        if self.U.bl == x and self.B.ul == y and self.L.bu == z:
            return ['U','B','L']
        if self.U.fr == x and self.R.fu == y and self.F.ur == z:
            return ['U','R','F']
        if self.U.fl == x and self.L.fu == y and self.F.ul == z:
            return ['U','L','F']
        if self.U.br == x and self.R.bu == y and self.B.ur == z:
            return ['U','R','B']
        if self.U.bl == x and self.L.bu == y and self.B.ul == z:
            return ['U','L','B']
        if self.D.fr == x and self.F.dr == y and self.R.fd == z:
            return ['D','F','R']
        if self.D.fl == x and self.F.dl == y and self.L.fd == z:
            return ['D','F','L']
        if self.D.br == x and self.B.dr == y and self.R.bd == z:
            return ['D','B','R']
        if self.D.bl == x and self.B.dl == y and self.L.bd == z:
            return ['D','B','L']
        if self.D.fr == x and self.R.fd == y and self.F.dr == z:
            return ['D','R','F']
        if self.D.fl == x and self.L.fd == y and self.F.dl == z:
            return ['D','L','F']
        if self.D.br == x and self.R.bd == y and self.B.dr == z:
            return ['D','R','B']
        if self.D.bl == x and self.L.bd == y and self.B.dl == z:
            return ['D','L','B']
        
        if self.R.fu == x and self.U.fr == y and self.F.ur == z:
            return ['R','U','F']
        if self.R.fd == x and self.D.fr == y and self.F.dr == z:
            return ['R','D','F']
        if self.R.bu == x and self.U.br == y and self.B.ur == z:
            return ['R','U','B']
        if self.R.bd == x and self.D.br == y and self.B.dr == z:
            return ['R','D','B']
        if self.R.fu == x and self.F.ur == y and self.U.fr == z:
            return ['R','F','U']
        if self.R.fd == x and self.F.dr == y and self.D.fr == z:
            return ['R','F','D']
        if self.R.bu == x and self.B.ur == y and self.U.br == z:
            return ['R','B','U']
        if self.R.bd == x and self.B.dr == y and self.D.br == z:
            return ['R','B','D']     
        if self.L.fu == x and self.U.fl == y and self.F.ul == z:
            return ['L','U','F']
        if self.L.fd == x and self.D.fl == y and self.F.dl == z:
            return ['L','D','F']
        if self.L.bu == x and self.U.bl == y and self.B.ul == z:
            return ['L','U','B']
        if self.L.bd == x and self.D.bl == y and self.B.dl == z:
            return ['L','D','B']
        if self.L.fu == x and self.F.ul == y and self.U.fl == z:
            return ['L','F','U']
        if self.L.fd == x and self.F.dl == y and self.D.fl == z:
            return ['L','F','D']
        if self.L.bu == x and self.B.ul == y and self.U.bl == z:
            return ['L','B','U']
        if self.L.bd == x and self.B.dl == y and self.D.bl == z:
            return ['L','B','D']
    "Method movescleanup: Eliminates redundancies in the moveslist."
    def movesconsolidate(self):
        i = 0
        while i < len(self.moves):
            if self.moves[i] == 'F' or self.moves[i] == 'F`' or self.moves[i] == 'F2':
                x = 'F'
                nx = 'B'
            elif self.moves[i] == 'B' or self.moves[i] == 'B`' or self.moves[i] == 'B2':
                x = 'B'
                nx = 'F'
            elif self.moves[i] == 'U' or self.moves[i] == 'U`' or self.moves[i] == 'U2':
                x = 'U'
                nx = 'D'
            elif self.moves[i] == 'D' or self.moves[i] == 'D`' or self.moves[i] == 'D2':
                x = 'D'
                nx = 'U'
            elif self.moves[i] == 'R' or self.moves[i] == 'R`' or self.moves[i] == 'R2':
                x = 'R'
                nx = 'L'
            elif self.moves[i] == 'L' or self.moves[i] == 'L`' or self.moves[i] == 'L2':
                x = 'L'
                nx = 'R'
            else:
                i += 1
                continue
            counter = 0
            total = 0
            while i + counter < len(self.moves):
                if self.moves[i + counter] == x:
                    total += 1
                    del self.moves[i + counter]
                elif self.moves[i + counter] == x+'`':
                    total += 3
                    del self.moves[i + counter]
                elif self.moves[i + counter] == x+'2':
                    total += 2
                    del self.moves[i + counter]
                elif self.moves[i + counter] == nx or self.moves[i + counter] == nx+'`' or self.moves[i + counter] == nx+'2':
                    counter += 1
                else:
                    break
            if total % 4 == 1:
                self.moves.insert(i,x)
            elif total % 4 == 2:
                self.moves.insert(i,x+'2')
            elif total % 4 == 3:
                self.moves.insert(i,x+'`')
            else:
                i = max(-1,i-2)
            i += 1
            
    "PLL (permutation-last-layer) algorithms. For (relative) permutation."
    def PLL_edgeright(self):
        self.F2turn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Lturn()
        self.F2turn()
        self.Rturn()
        self.Lprimeturn()
        self.Uprimeturn()
        self.F2turn()
    def PLL_edgeleft(self):
        self.F2turn()
        self.Uturn()
        self.Rprimeturn()
        self.Lturn()
        self.F2turn()
        self.Rturn()
        self.Lprimeturn()
        self.Uturn()
        self.F2turn()
    def PLL_edgez(self):
        self.FtoDturn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Uturn()
        self.Dturn()
        self.Rprimeturn()
        self.Dturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Uturn()
        self.Rturn()
        self.D2turn()
        self.FtoUturn()
    def PLL_edgeplus(self):
        self.R2turn()
        self.L2turn()
        self.Dturn()
        self.R2turn()
        self.L2turn()
        self.U2turn()
        self.R2turn()
        self.L2turn()
        self.Dturn()
        self.R2turn()
        self.L2turn()
    def PLL_9(self):
        self.FtoUturn()
        self.Rprimeturn()
        self.Uturn()
        self.Rprimeturn()
        self.D2turn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.D2turn()
        self.R2turn()
        self.FtoDturn()
    def PLL_9rev(self):
        self.FtoUturn()
        self.R2turn()
        self.D2turn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.D2turn()
        self.Rturn()
        self.Uprimeturn()
        self.Rturn()
        self.FtoDturn()
    def PLL_double9(self):
        self.FtoDturn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Dturn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Dprimeturn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Dturn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Dprimeturn()
        self.FtoUturn()
    def PLL_Lright(self):
        self.Lturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Uturn()
        self.Lprimeturn()
        self.U2turn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.U2turn()
        self.Rturn()
    def PLL_Lleft(self):
        self.Rprimeturn()
        self.Uturn()
        self.Lturn()
        self.Uprimeturn()
        self.Rturn()
        self.U2turn()
        self.Lprimeturn()
        self.Uturn()
        self.Lturn()
        self.U2turn()
        self.Lprimeturn()
    def PLL_T(self):
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Fturn()
        self.R2turn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Fprimeturn()
    def PLL_7right(self):
        self.Rprimeturn()
        self.U2turn()
        self.Rturn()
        self.U2turn()
        self.Rprimeturn()
        self.Fturn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Fprimeturn()
        self.R2turn()
    def PLL_7left(self):
        self.Lturn()
        self.U2turn()
        self.Lprimeturn()
        self.U2turn()
        self.Lturn()
        self.Fprimeturn()
        self.Lprimeturn()
        self.Uprimeturn()
        self.Lturn()
        self.Uturn()
        self.Lturn()
        self.Fturn()
        self.L2turn()
    def PLL_V(self):
        self.Rprimeturn()
        self.Uturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Bprimeturn()
        self.Rprimeturn()
        self.B2turn()
        self.Uprimeturn()
        self.Bprimeturn()
        self.Uturn()
        self.Bprimeturn()
        self.Rturn()
        self.Bturn()
        self.Rturn()
    def PLL_Gright(self):
        self.R2turn()
        self.Dturn()
        self.FtoLturn()
        self.Rprimeturn()
        self.Uturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Rturn()
        self.Dprimeturn()
        self.F2turn()
        self.Lprimeturn()
        self.Uturn()
        self.Lturn()
    def PLL_Gleft(self):
        self.L2turn()
        self.Dprimeturn()
        self.FtoRturn()
        self.Lturn()
        self.Uprimeturn()
        self.Lturn()
        self.Uturn()
        self.Lprimeturn()
        self.Dturn()
        self.F2turn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
    def PLL_Grightrev(self):
        self.Lprimeturn()
        self.Uprimeturn()
        self.Lturn()
        self.F2turn()
        self.Dturn()
        self.Rprimeturn()
        self.Uturn()
        self.Rturn()
        self.Uprimeturn()
        self.Rturn()
        self.FtoRturn()
        self.Dprimeturn()
        self.R2turn()
    def PLL_Gleftrev(self):
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.F2turn()
        self.Dprimeturn()
        self.Lturn()
        self.Uprimeturn()
        self.Lprimeturn()
        self.Uturn()
        self.Lprimeturn()
        self.FtoLturn()
        self.Dturn()
        self.L2turn()
    def PLL_equal(self):
        self.Rprimeturn()
        self.Uturn()
        self.Rturn()
        self.Uprimeturn()
        self.R2turn()
        self.Fprimeturn()
        self.Uprimeturn()
        self.Fturn()
        self.Uturn()
        self.Rturn()
        self.Fturn()
        self.Rprimeturn()
        self.Fprimeturn()
        self.R2turn()
    def PLL_Y(self):
        self.Fturn()
        self.Rturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Fprimeturn()
        self.Rturn()
        self.Uturn()
        self.Rprimeturn()
        self.Uprimeturn()
        self.Rprimeturn()
        self.Fturn()
        self.Rturn()
        self.Fprimeturn()
    def PLL_Nright(self):
        self.Rprimeturn()
        self.Uturn()
        self.Lprimeturn()
        self.U2turn()
        self.Rturn()
        self.Uprimeturn()
        self.Lturn()
        self.Rprimeturn()
        self.Uturn()
        self.Lprimeturn()
        self.U2turn()
        self.Rturn()
        self.Uprimeturn()
        self.Lturn()
    def PLL_Nleft(self):
        self.Lturn()
        self.Uprimeturn()
        self.Rturn()
        self.U2turn()
        self.Lprimeturn()
        self.Uturn()
        self.Rprimeturn()
        self.Lturn()
        self.Uprimeturn()
        self.Rturn()
        self.U2turn()
        self.Lprimeturn()
        self.Uturn()
        self.Rprimeturn()