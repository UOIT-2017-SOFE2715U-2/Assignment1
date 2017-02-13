

def IterativeNQueensSolver(numberOfQueens):
    N = numberOfQueens
    Queens = [0] * N
    AttackedSumDiagnal = [None] * N
    AttackedDifferenceDiagnal = [None] * N

    solutions = []
    row = 0
    column = 0

    while column<N and row >= 0:
        ## test if this queen attacked by previous queens
        ## start with assumption that it's not attacked
        Attacked = False
        for i in range(0,row):
            # if this queen in same row as upper queen or diagnally attacked by upper queen
            if (column == Queens[i] or
                    AttackedSumDiagnal[i] == row + column or
                    AttackedDifferenceDiagnal[i] == row - column):
                ## any conditino is ture then queen attacked in this position
                Attacked = True
        ## if position found for this queen, save the position and go to next row
        if Attacked == False:
            Queens[row] = column
            AttackedSumDiagnal[row] = column + row
            AttackedDifferenceDiagnal[row] = row - column
            if row == (N - 1) : # if it is the last row
                solutions.append(Queens[:])
                column = column + 1
                if column == N:
                    while column >= N and row >= 0:
                        row = row - 1
                        column = Queens[row] + 1
            else:
                column = 0
                row = row + 1
        ## if there is no position for current Queen
        elif Attacked == True and column == N -1:
            column = column + 1
            while column >= N and row >= 0:
                row = row - 1
                column = Queens[row] + 1
        else:
            column = column + 1
    return solutions
