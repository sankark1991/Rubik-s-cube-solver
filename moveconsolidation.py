"This is version 2.0 of the cubstate script."

def movesexpand(moves):
    "Expand the list out into single clockwise turns."
    i = 0
    while i < len(moves):
        if moves[i] == 'F' or moves[i] == 'B' or moves[i] == 'U' or moves[i] == 'D' or moves[i] == 'R' or moves[i] == 'L':
            i += 1
        elif moves[i] == 'F2':
            moves[i] = 'F'
            moves.insert(i,'F')
            i += 2
        elif moves[i] == 'B2':
            moves[i] = 'B'
            moves.insert(i,'B')
            i += 2
        elif moves[i] == 'U2':
            moves[i] = 'U'
            moves.insert(i,'U')
            i += 2
        elif moves[i] == 'D2':
            moves[i] = 'D'
            moves.insert(i,'D')
            i += 2
        elif moves[i] == 'R2':
            moves[i] = 'R'
            moves.insert(i,'R')
            i += 2
        elif moves[i] == 'L2':
            moves[i] = 'L'
            moves.insert(i,'L')
            i += 2
        elif moves[i] == 'F`':
            moves[i] = 'F'
            moves.insert(i,'F')
            moves.insert(i,'F')
            i += 3
        elif moves[i] == 'B`':
            moves[i] = 'B'
            moves.insert(i,'B')
            moves.insert(i,'B')
            i += 3
        elif moves[i] == 'U`':
            moves[i] = 'U'
            moves.insert(i,'U')
            moves.insert(i,'U')
            i += 3
        elif moves[i] == 'D`':
            moves[i] = 'D'
            moves.insert(i,'D')
            moves.insert(i,'D')
            i += 3
        elif moves[i] == 'R`':
            moves[i] = 'R'
            moves.insert(i,'R')
            moves.insert(i,'R')
            i += 3
        elif moves[i] == 'L`':
            moves[i] = 'L'
            moves.insert(i,'L')
            moves.insert(i,'L')
            i += 3
            
def movesreorder(moves):
    "F's before B's, U's before D's, R's before L's."
    i = 0

def movesconsolidate(moves):   
    "Combine terms together."
    i = 0
    while i < len(moves):
        if i < len(moves) and moves[i] in ['F','F2','F`']:
            counter = 1
            if moves[i] == 'F':
                total = 1
            elif moves[i] == 'F2':
                total = 2
            elif moves[i] == 'F`':
                total = 3
            while (i + counter < len(moves)) and moves[i + counter] in ['F','F2','F`']:
                if moves[i + counter] == 'F':
                    total += 1
                elif moves[i + counter] == 'F2':
                    total += 2
                elif moves[i + counter] == 'F`':
                    total += 3
                counter += 1
            del moves[i:i + counter]
            if total % 4 == 1:
                moves.insert(i,'F')
                i += 1
            elif total % 4 == 2:
                moves.insert(i,'F2')
                i += 1
            elif total % 4 == 3:
                moves.insert(i,'F`')
                i += 1
            else:
                i -= 1
        if i < len(moves) and moves[i] in ['B','B2','B`']:
            counter = 1
            if moves[i] == 'B':
                total = 1
            elif moves[i] == 'B2':
                total = 2
            elif moves[i] == 'B`':
                total = 3
            while (i + counter < len(moves)) and moves[i + counter] in ['B','B2','B`']:
                if moves[i + counter] == 'B':
                    total += 1
                elif moves[i + counter] == 'B2':
                    total += 2
                elif moves[i + counter] == 'B`':
                    total += 3
                counter += 1
            del moves[i:i + counter]
            if total % 4 == 1:
                moves.insert(i,'B')
                i += 1
            elif total % 4 == 2:
                moves.insert(i,'B2')
                i += 1
            elif total % 4 == 3:
                moves.insert(i,'B`')
                i += 1
            else:
                i -= 1
        if i < len(moves) and moves[i] in ['U','U2','U`']:
            counter = 1
            if moves[i] == 'U':
                total = 1
            elif moves[i] == 'U2':
                total = 2
            elif moves[i] == 'U`':
                total = 3
            while (i + counter < len(moves)) and moves[i + counter] in ['U','U2','U`']:
                if moves[i + counter] == 'U':
                    total += 1
                elif moves[i + counter] == 'U2':
                    total += 2
                elif moves[i + counter] == 'U`':
                    total += 3
                counter += 1
            del moves[i:i + counter]
            if total % 4 == 1:
                moves.insert(i,'U')
                i += 1
            elif total % 4 == 2:
                moves.insert(i,'U2')
                i += 1
            elif total % 4 == 3:
                moves.insert(i,'U`')
                i += 1
            else:
                i -= 1
        if i < len(moves) and moves[i] in ['D','D2','D`']:
            counter = 1
            if moves[i] == 'D':
                total = 1
            elif moves[i] == 'D2':
                total = 2
            elif moves[i] == 'D`':
                total = 3
            while (i + counter < len(moves)) and moves[i + counter] in ['D','D2','D`']:
                if moves[i + counter] == 'D':
                    total += 1
                elif moves[i + counter] == 'D2':
                    total += 2
                elif moves[i + counter] == 'D`':
                    total += 3
                counter += 1
            del moves[i:i + counter]
            if total % 4 == 1:
                moves.insert(i,'D')
                i += 1
            elif total % 4 == 2:
                moves.insert(i,'D2')
                i += 1
            elif total % 4 == 3:
                moves.insert(i,'D`')
                i += 1
            else:
                i -= 1
        if i < len(moves) and moves[i] in ['R','R2','R`']:
            counter = 1
            if moves[i] == 'R':
                total = 1
            elif moves[i] == 'R2':
                total = 2
            elif moves[i] == 'R`':
                total = 3
            while (i + counter < len(moves)) and moves[i + counter] in ['R','R2','R`']:
                if moves[i + counter] == 'R':
                    total += 1
                elif moves[i + counter] == 'R2':
                    total += 2
                elif moves[i + counter] == 'R`':
                    total += 3
                counter += 1
            del moves[i:i + counter]
            if total % 4 == 1:
                moves.insert(i,'R')
                i += 1
            elif total % 4 == 2:
                moves.insert(i,'R2')
                i += 1
            elif total % 4 == 3:
                moves.insert(i,'R`')
                i += 1
            else:
                i -= 1
        if i < len(moves) and moves[i] in ['L','L2','L`']:
            counter = 1
            if moves[i] == 'L':
                total = 1
            elif moves[i] == 'L2':
                total = 2
            elif moves[i] == 'L`':
                total = 3
            while (i + counter < len(moves)) and moves[i + counter] in ['L','L2','L`']:
                if moves[i + counter] == 'L':
                    total += 1
                elif moves[i + counter] == 'L2':
                    total += 2
                elif moves[i + counter] == 'L`':
                    total += 3
                counter += 1
            del moves[i:i + counter]
            if total % 4 == 1:
                moves.insert(i,'L')
                i += 1
            elif total % 4 == 2:
                moves.insert(i,'L2')
                i += 1
            elif total % 4 == 3:
                moves.insert(i,'L`')
                i += 1
            else:
                i -= 1
            
            
test1 = ['F','F','D','D`','D2','U','D','D`','U`','L','L`','F`','F2','R`','R']