import sys
import os
import math
import time
from backtracking import *
from hillclimbing import *


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


def pretty_print_puzzle(puzzle,n):

    row_number=0
    print()
    for row in puzzle:
        row_string='|'
        row_number+=1
        for spot in range(len(row)):
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
    tup = input_conversion(argv[1])
    grid = tup[1]
    n = tup[0]
    pretty_print_puzzle(grid, n)
    print ("Initial Grid")
    solver = Backtracking(n)
    start = int(round(time.time()*1000))
    solver.backtracking_search(grid)
    finish = int(round(time.time()*1000))
    with open("timeResults.txt", 'a') as file:
        out = str(finish - start)+"\n"
        file.write(out)
    file.close()
    print("It took {} ms to solve".format(finish - start))


if __name__ == "__main__":
    main(sys.argv)