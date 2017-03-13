#! /usr/bin/env python
import sys
import os
import math
import time
from backtracking import *
from hillclimbing import *
from backtracking_prime import *


def  input_conversion(input):
    n = len(input)**(1/4)
    if n-int(n)!=0:
        print("Not a valid sudoku string. Please try again.")
        exit()
    else:
        n = int(n)
    sudoku=[]


    '''Two for loops
     The loop will go 0-n^2 if a dot meaning a blank space is in input a zero will be put in
    '''
    temp=[]

    if input.isnumeric():
        for i in range( len(input)):


            if len(temp)<n**(2):
                temp.append(int(input[i]))
            if len(temp)==n**(2):
                sudoku.append(temp)
                temp=[]

    return (n, sudoku)


def pretty_print_puzzle(puzzle, n):

    row_number=0
    print()
    for row in puzzle:
        row_string='|'
        row_number+=1
        for spot in range(len(row)):
            #An if statment due to the fact that input conversion in hillclimbing makes the spot a tuple instead of just an int.
            if type(row[spot])  ==tuple:
                if spot%n==0 and spot !=0:
                    row_string=row_string+'  |  '+str(row[spot][0])
                else:
                    row_string=row_string+'  '+str(row[spot][0])
            else:
                if spot%n==0 and spot !=0:
                    row_string=row_string+'  |  '+str(row[spot])
                else:
                    row_string=row_string+'  '+str(row[spot])
        print(row_string+'  |')
        if row_number%n==0 and row_number!= len(puzzle):
            print()

        row_string=''
    print()

def main(argv):
    my_input = ''
    if len(argv) >2 :
        my_input = str(argv[2])
    tup = input_conversion(my_input)
    grid = tup[1]
    n = tup[0]

    #print ("Initial Grid")
    #pretty_print_puzzle(grid, n)

    start = int(round(time.time()*1000))
    if ('backtracking' in argv):
        solver = Backtracking(n)
        start = int(round(time.time()*1000))
        solver.backtracking_search(grid)
        finish = int(round(time.time()*1000))

    elif('hillclimbing' in argv):
        solver = Hillclimbing(n)
        start = int(round(time.time()*1000))
        puzzle = solver.conversion(my_input)
        solver.hillclimbing_search(puzzle)
        finish = int(round(time.time()*1000))

    elif('backtracking_prime' in argv):
        solver = backtracking_prime(grid, n)
        start = int(round(time.time()*1000))
        solver.solve_puzzle()
        finish = int(round(time.time()*1000))
    else:
        print("Invalid input to program.")
        print("Please rerun the program with the following format of input:")
        print("python3 main.py <method> <puzzle>\n"
             +"The following are valid <method> inputs: \n"
             +"     backtracking\n     backtracking_prime\n     hillclimbing")
        sys.exit()

    with open("timeResults.txt", 'a') as file:
        out = str(finish - start)+"\n"
        file.write(out)
    file.close()
    print("It took {} ms to solve".format(finish - start))

if __name__ == "__main__":
    main(sys.argv)
