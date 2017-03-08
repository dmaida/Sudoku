import sys
import os
import math
import time

class backtracking_prime():

    def __init__(self, puzzle, n):
        self.n = n
        self.grid = {}
        self.puzzle = puzzle

    def solve_puzzle(self):
        for i in range(self.n*self.n):
            self.grid[i] = {}
            for j in range(self.n*self.n):
                if self.puzzle[i][j]:
                    move = []
                    move.append(self.puzzle[i][j])
                    self.grid[i][j] = move
                else:
                    moves = list(range(1, self.n * self.n + 1))
                    self.grid[i][j] = moves
        self.reduce_domain()
        self.backtrack()

    def is_valid(self,grid, i, j, digit):
        for x in range(self.n**2):
            if ((len(grid[i][x]) == 1) and (digit == grid[i][x][0])):
                return False
        for x in range(self.n**2):
            if (((len(grid[x][j]) == 1) and (digit == grid[x][j][0]))):
                return False

        init_x = i - i%self.n # find left side of nxn box
        init_y = j - j%self.n # find upper side of nxn box

        for x in range(init_x, init_x + self.n):
            for y in range(init_y, init_y + self.n): # check the nxn box for repeats
                if ((len(grid[x][y]) == 1) and (grid[x][y][0] == digit)): # if repeat was found
                    return False # return invalid
        return True # when row/col are valid and box did not find repeat

    def reduce_domain(self):
        repeat = True
        while repeat:
            repeat = False
            for i in range(0, self.n*self.n):
                for j in range(0, self.n*self.n):

                    pencil_list = self.grid[i][j]

                    if (len(pencil_list) != 1):
                        #print("entered ",i,j)
                        for num in pencil_list:
                            #print(num)
                            if (not self.is_valid(self.grid, i, j, num)):
                                #print("Removing ", num, "from ", self.grid[i][j])
                                pencil_list.remove(num)
                                repeat = True

    def next_cell(self, i, j):
        for x in range(i, (self.n**2)):
            #print("X: ",x)

            for y in range(j, (self.n**2)):
                #print("Y: ",y)
                pencil_list = self.grid[x][y]
                #print ("Returning: ",pencil_list, "Len ", len(pencil_list))
                #print_puzzle(self.grid, self.n)
                if (len(pencil_list) > 1):
                    #print ("Returning: ",pencil_list)
                    return x, y
            j = 0

        for x in range(0, self.n**2):
            for y in range(0, self.n**2):
                if (len(pencil_list) > 1):
                    return x, y

        return -1, -1

    def backtrack(self, i = 0, j = 0):
        grid = self.grid
        i, j = self.next_cell(i, j)
        #print("Changing ", i, j)
        if (i == -1):
            return True

        r = grid[i][j]
        for digit in r:
            if self.is_valid(grid, i, j, digit):
                temp = []
                temp.append(digit)
                grid[i][j] = temp
                #print_puzzle(self.grid, self.n)
                if (self.backtrack(i,j) == True):
                    return True
                grid[i][j] = r
        return False

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
                cell = int(input[i])
                if cell != 0:
                    tup =(cell, True)
                else:
                    tup =(cell, False)

                temp.append(tup)
            if len(temp)==n**(2):
                sudoku.append(temp)
                temp=[]
    print("Intitial Puzzle")
    pretty_print_puzzle(sudoku, n)
    return (n, sudoku)

def print_puzzle(puzzle,n):

    row_number=0
    print()
    for row in range(n*n):
        digit = []
        for col in range(n*n):
            digit.append(puzzle[row][col])
        print(digit)

def main():
    #tup = input_conversion(u'003020600900305001001806400008102900700000008006708200002609500800203009005010300')
    tup = input_conversion(u'000005043050002007034000080000007600900010005001200000090000310400800050580900000')
    puzzle = tup[1]
    n = tup[0]
    start = int(round(time.time()*1000))
    solved_puzzle = backtracking_prime(puzzle, n)
    finish = int(round(time.time()*1000))
    print_puzzle(solved_puzzle.grid, n)
    print("It took {} ms to solve".format(finish - start))


if __name__ == "__main__":
    main()
