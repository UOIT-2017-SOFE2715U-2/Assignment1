from IterativeNQueensSolver import *
from DrawNQueensSolution import *

N = input("Enter number of queens ")

solutions = IterativeNQueensSolver(N)

print "Saving solutions. Please wait!"
s = 1
for i in solutions:
    print i
    DrawNQueensSolution(N,i,s)
    s = s + 1