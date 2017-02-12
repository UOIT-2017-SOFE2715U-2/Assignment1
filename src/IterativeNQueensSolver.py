# picuters By en:User:Cburnett - Own workThis vector image was created with Inkscape., CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1496714
from DrawNQueensSolution import *
import time

def IterativeNQueensSolver(numberOfQueens):
    start_time = time.time()
    N = numberOfQueens
    Queens = [0] * N
    AttackedSumDiagnal = [None] * N
    AttackedDifferenceDiagnal = [None] * N

    numberOfSolutions = 0
    solutions = []
    row = 0
    column = 0

    while column<N and row >= 0:
        ## test if this queen attacked by previous queens
        Attacked = False
        for i in range(0,row):
            if (column == Queens[i] or
                    AttackedSumDiagnal[i] == row + column or
                    AttackedDifferenceDiagnal[i] == row - column):
                ## it is attacked. so,
                Attacked = True
        ## if position found for this queen, go to next row
        if Attacked == False:
            Queens[row] = column
            AttackedSumDiagnal[row] = column + row
            AttackedDifferenceDiagnal[row] = row - column
            if row == (N - 1) : # if it is the last row
                numberOfSolutions = numberOfSolutions + 1
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
    end_time = time.time()
    print str(end_time - start_time) + " sec."
    print str(numberOfSolutions) + " solutinos found for " + str(N) + " queens problem."
    return solutions
