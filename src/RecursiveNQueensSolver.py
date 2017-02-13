
def recursive_n_queens_solver(number_of_queens, current_row, queens, solutions):
    for column in range(0,number_of_queens):
        attacked = False
        for row in range(0,current_row):
            if (column == queens[row] or
                current_row + queens[row] == row + column or
                current_row - queens[row] == row - column):
                attacked = True
        if not attacked:
            queens[current_row] = column
            if current_row == number_of_queens - 1:
                solutions.append(queens[:])
            else:
                recursive_n_queens_solver(number_of_queens,current_row + 1, queens, solutions)
    return solutions
