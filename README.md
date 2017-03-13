# Sudoku Solver With Search

###### Authors: Ben Sherington, Olivia Lorimor, Nazar Stelmakh, Daniel Maida
###### Email: bsherington@wsu.edu, oliva.lorimor@wsu.edu, nazar.stelmakh@wsu.edu, daniel.maida@wsu.edu

### Description:

The purpose of this project is to create a Sudoku Puzzle Solving Agent. 
Two distinct solution strategies will be implemented and evaluated.
In this paper we will be exploring a constraint satisfaction algorithm called
Backtracking to solve a Sudoku puzzle. In addition to Backtracking, we will be
exploring a less traditional algorithm, Stochastic Hill Climbing, for a constraint 
satisfaction problem such as Sudoku. 

We implemented three distint methods for extra credit. 

### Run/Compile:

In a Unix Enviroment such as Linux or Mac OS X.

$python3 main.y method puzzle

method options:
	backtracking
	backtracking_prime 
	hillclimbing
	
puzzle options:
    Sudoko puzzle string such as this. 
    
    000030009048900000200470100125000080000080710000500000000090054061000003000050070

### Archive:
backtracking_prime.py 
backtracking.py 
hillclimbing.py 
main.py 
runTest.sh
README.md 
Puzzles
timeData 


