from IterativeNQueensSolver import *
from RecursiveNQueensSolver import *
from DrawNQueensSolution import *
from datetime import datetime


N = input("Enter number of queens ")

print "\nIterative Algorithm:\n"
start_time = datetime.now()
solutions = IterativeNQueensSolver(N)
end_time = datetime.now()
print str(end_time.microsecond - start_time.microsecond) + " micro sec."
print str(len(solutions)) + " solutions found for " + str(N) + " queens problem."

print "Printing Solutions:\n"
for i in range(0,len(solutions)):
    print solutions[i]

print "\nRecursive Algorithm:\n"
start_time = datetime.now()
solutions = recursive_n_queens_solver(N, 0, [-1] * N,[])
end_time = datetime.now()
print str(end_time.microsecond - start_time.microsecond) + " micro sec."
print str(len(solutions)) + " solutions found for " + str(N) + " queens problem."

print "Printing Solutions:\n"
for i in range(0,len(solutions)):
    print solutions[i]


#uncomment the following block of lines if you have Pillow package installed

print "\nSaving solutions. Please wait!"
s = 1
for i in solutions:
    DrawNQueensSolution(N,i,s)
    s = s + 1
