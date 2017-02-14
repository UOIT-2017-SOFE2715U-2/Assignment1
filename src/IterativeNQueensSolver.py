from time import clock

def iterative_n_queens_solver(numberOfQueens):
    N = numberOfQueens
    queens = [-1] * N
    solutions = []
    times = []
    current_row = 0
    column = 0

    while column<N and current_row >= 0:
        # test if this queen attacked by previous queens
        # start with assumption that it's not attacked
        attacked = False
        previous_row = 0
        while previous_row < current_row and (not attacked):
            # if this queen in same current_row as upper queen or diagnally attacked by upper queen
            if (column == queens[previous_row] or
                    current_row + queens[previous_row] == previous_row + column or
                    current_row - queens[previous_row] == previous_row - column):
                # any condition is true then queen attacked in this position
                attacked = True
            previous_row += 1
        # if position found for this queen, save the position and go to next current_row
        if not attacked:
            queens[current_row] = column
            if current_row == (N - 1) : # if it is the last current_row
                solutions.append(queens[:])
                times.append(clock())
                column += 1
                if column == N:
                    # back track
                    #----------------------------------------
                    while column >= N and current_row >= 0:
                        current_row -= 1
                        column = queens[current_row] + 1
                    #----------------------------------------
            else:
                column = 0
                current_row += 1
        # if there is no position for current queen
        elif attacked and column == N -1:
            column += 1
            # back track
            #--------------------------------------
            while column >= N and current_row >= 0:
                current_row -= 1
                column = queens[current_row] + 1
            #--------------------------------------
        else:
            column += 1
    return [solutions, times]
