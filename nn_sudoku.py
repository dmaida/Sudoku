import sys
import os
import math
import numpy
import time

n = -1 # gonna be passing n around like a joint. Should probably be a global


def next_empty_cell(grid, i, j):

    count = 0

    # Searches through grid starting at i, j
    # These nested for loops aren't required
    # but cuts time by A LOT
    for x in range(i, (n**2)):
        for y in range(j, (n**2)):
            if grid[x][y] == 0:
                return x, y

    # Searches through entire grid looking for a 0
    for x in range(0,n**2):
        for y in range(0,n**2):
            if grid[x][y] == 0:
                return x, y

    # Could not find a 0. Solution found
    return -1, -1

def is_valid(grid, i, j, digit):
    valid_row = all([digit != grid[i][x] for x in range(n**2)]) # magic code that checks entire row for digit
    valid_col = all([digit != grid[x][j] for x in range(n**2)]) # magic code that checks entire col for digit
    if (valid_row and valid_col):

        init_x = i - i%n # find left side of nxn box
        init_y = j - j%n # find upper side of nxn box

        for x in range(init_x, init_x + n):
            for y in range(init_y, init_y + n): # check the nxn box for repeats
                if grid[x][y] == digit: # if repeat was found
                    return False # return invalid
        return True # when row/col are valid and box did not find repeat
    else:
        return False # when row and/or col is NOT valid

def backtracking_search(grid, i = 0, j = 0):

    i, j = next_empty_cell(grid, i, j)
    if (i == -1):
        print("Found Solution")
        pretty_print_puzzle(grid)
        return True

    r = range(1, (n**2)+1)
    for digit in r:
        if is_valid(grid, i, j, digit):
            grid[i][j] = digit
            if (backtracking_search(grid, i, j) == True):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def  input_conversion(input):
    global n
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

    return sudoku


def pretty_print_puzzle(puzzle):
    global n

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




if __name__ == "__main__":
    grid = input_conversion(u'106008000050000600000005072400600009060000030900001004620900000008000020000500301')
    print ("Initial Grid")
    pretty_print_puzzle(grid)
    start = int(round(time.time()*1000))
    backtracking_search(grid)
    finish = int(round(time.time()*1000))
    print("It took {} ms to solve".format(finish - start))
