from time import clock

def recursive_n_queens_solver(number_of_queens, current_row, queens, solutions, times):
    # for current row examin the positions column by column
    for column in range(0,number_of_queens):
        attacked = False
        # check if current position attacked by upper queens
        previous_row = 0
        while previous_row < current_row and (not attacked):
            if (column == queens[previous_row] or
                    current_row + queens[previous_row] == previous_row + column or
                    current_row - queens[previous_row] == previous_row - column):
                # if any condition is true then this position attacked
                attacked = True
            previous_row += 1
        # if free position found,
        if not attacked:
            # save current queen position as possible solution
            queens[current_row] = column
            # if current row is last row then save as solution
            if current_row == number_of_queens - 1:
                solutions.append(queens[:])
                times.append(clock())
            # if current row is not last row then examin next row recursively
            else:
                recursive_n_queens_solver(number_of_queens,current_row + 1, queens, solutions, times)
    return [solutions, times]
