import sys
import os
import math
import time

class Backtracking():

    def __init__(self, n):
        self.n=n

    def next_empty_cell(self,grid, i, j):
        count = 0
        # Searches through grid starting at i, j
        # These nested for loops aren't required
        # but cuts time by A LOT
        for x in range(i, (self.n**2)):
            for y in range(j, (self.n**2)):
                if grid[x][y] == 0:
                    return x, y

        # Searches through entire grid looking for a 0
        for x in range(0,self.n**2):
            for y in range(0,self.n**2):
                if grid[x][y] == 0:
                    return x, y

        # Could not find a 0. Solution found
        return -1, -1

    def is_valid(self,grid, i, j, digit):
        valid_row = all([digit != grid[i][x] for x in range(self.n**2)]) # magic code that checks entire row for digit
        valid_col = all([digit != grid[x][j] for x in range(self.n**2)]) # magic code that checks entire col for digit
        if (valid_row and valid_col):

            init_x = i - i%self.n # find left side of nxn box
            init_y = j - j%self.n # find upper side of nxn box

            for x in range(init_x, init_x + self.n):
                for y in range(init_y, init_y + self.n): # check the nxn box for repeats
                    if grid[x][y] == digit: # if repeat was found
                        return False # return invalid
            return True # when row/col are valid and box did not find repeat
        else:
            return False # when row and/or col is NOT valid

    def backtracking_search(self,grid, i = 0, j = 0):

        i, j = self.next_empty_cell(grid, i, j)
        if (i == -1):
            #print("Found Solution")
            #pretty_print_puzzle(grid)
            return True

        r = range(1, (self.n**2)+1)
        for digit in r:
            if self.is_valid(grid, i, j, digit):
                grid[i][j] = digit
                if (self.backtracking_search(grid, i, j) == True):
                    return True
                # Undo the current cell for backtracking
                grid[i][j] = 0
        return False
