from IterativeNQueensSolver import *
from RecursiveNQueensSolver import *
from DrawNQueensSolution import *
from time import clock

# define method for printing results

def print_result_times(solutions, start_time, times):
    print "Time to find first solution: " + str((times[0] - start_time)*1000000) + " micro sec."
    print "Time to find all solutions: " + str(
        (times[len(times) - 1] - start_time)*1000000) + " micro sec."
    print str(len(solutions)) + " solutions found for " + str(N) + " queens problem."


def print_solutions(solutions):
    print "Printing Solutions:\n"
    for i in range(0, len(solutions)):
        print solutions[i]

# prompt user for number of queens
N = input("Enter number of queens ")

# prepare to run the iterative method
print "\nIterative Algorithm:\n"
# save the time of the system before running the method
start_time = clock()
# run the iterative method which return the solutions and the time taken for every solution to be found
[solutions, times] = iterative_n_queens_solver(N)
# print the results
print_result_times(solutions,start_time, times)
# we know solutions are the same so, comment the following line for now
#print_solutions(solutions)

# prepare to run the recursive method
print "\nRecursive Algorithm:\n"
# save the time of the system before running the method
start_time = clock()
#run the recursive method which return the solutions and the time taken for every solution to be found
[solutions, times] = recursive_n_queens_solver(N, 0, [-1] * N, [], [])
# print the results
print_result_times(solutions,start_time, times)
print_solutions(solutions)

#uncomment the following block of lines if you have numpy and Pillow package installed
'''
print "\nSaving solutions. Please wait!"
s = 1
for i in solutions:
    draw_n_queens_solution(N,i,s)
    s += 1
'''