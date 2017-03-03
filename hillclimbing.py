import sys
import os
import math
import time

class Hillclimbing():

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


    def evaluate_sudoku(self, grid):

        """
        This functions runs through the Sudoku grid
        and checks every row, col, and inner squares
        for unique values. Every time a unique value is
        found 1 point gets added to the totalScore.

        The maximum score for a 9x9 puzzle is 243.
        Meaning that there is a unique value in every row, col,
        and inner square.

        IN PROGRESS: Still need to score inner squares.
        """
        unique = []
        rowScore = 0
        colScore = 0
        totalScore = 0
        for i in range(0, self.n**2): #for every row in Grid
            valid_row = [grid[i][x] for x in range(self.n**2)]
            for value in valid_row:
                if value not in unique:
                    rowScore += 1
                    unique.append(value)
                else: continue
            unique = [] # reset the unique values for next row

        for j in range(0, self.n**2):  # for every col in Grid
            valid_col = [grid[x][j] for x in range(self.n**2)]
            for value in valid_col:
                if value not in unique:
                    colScore += 1
                    unique.append(value)
                else: continue
            unique = [] #reset the unique values for next col
        totalScore = rowScore + colScore

        print(totalScore)
        return totalScore


    def hillclimbing_search(self,grid, i = 0, j = 0):
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
                temp.append(int(input[i]))
            if len(temp)==n**(2):
                sudoku.append(temp)
                temp=[]
    return (n, sudoku)

def main(argv):
    tup = input_conversion(u'004060000070000050000391007009000300102040709003000500800629000020000010000030800')
    grid = tup[1]
    n = tup[0]

    solver = Hillclimbing(n)
    solver.evaluate_sudoku(grid)


if __name__ == "__main__":
    main(sys.argv)

"""
Stochastic Hill Climbing

X = Fill the empty cells randomly
flag = true
while flag is true
    flag = false
    for i=0 to 8
        for j= 0 to 8
        i= random btw 0 to 8
        j= random btw 0 to 8
        for k = 1 to 9
            oldScore = evaluate(X)
            temp = X[i][j]
            X[i][j] = k
            newScore = evaluate(X)
            if oldScore > newScore
                X[i][j] = temp
            else
                flag = true
        end second for
    end first for
end while


"""
