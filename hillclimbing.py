import sys
import os
import math
import time
import random
class Hillclimbing():
    def __init__(self, n):
        self.n= n
        self.OPTIMAL_SCORE= 243

    def is_valid(self,grid, i, j, digit):
        valid_row = all([digit != grid[i][x][0] for x in range(self.n**2)]) # magic code that checks entire row for digit
        valid_col = all([digit != grid[x][j][0] for x in range(self.n**2)]) # magic code that checks entire col for digit
        if (valid_row and valid_col):
            init_x = i - i%self.n # find left side of nxn box
            init_y = j - j%self.n # find upper side of nxn box
            for x in range(init_x, init_x + self.n):
                for y in range(init_y, init_y + self.n): # check the nxn box for repeats
                    if grid[x][y][0] == digit: # if repeat was found
                        return False # return invalid
            return True # when row/col are valid and box did not find repeat
        else:
            return False # when row and/or col is NOT valid
    def  is_solved(self, grid):
        """
        Helper method that evaluates the score of
        the inner square of the grid. Used to calculate
        total score of Sudoku puzzle.
        """
        unique = []
        rowScore = 0
        colScore = 0
        totalScore = 0
        for i in range(0, self.n**2): #for every row in Grid
            valid_row = [grid[i][x] for x in range(self.n**2)]
            for value in valid_row:
                if value[0] not in unique:
                    if value[0] != 0:
                        rowScore += 1
                        unique.append(value[0])
                else: return False
            unique = [] # reset the unique values for next row
        for j in range(0, self.n**2):  # for every col in Grid
            valid_col = [grid[x][j] for x in range(self.n**2)]
            for value in valid_col:
                if value[0] not in unique:
                    if value[0] != 0:
                        colScore += 1
                        unique.append(value[0])
                else: return False
            unique = [] #reset the unique values for next col
        box = []
        v = 0
        w = 0
        unique = []
        squareScore = 0
        while (True):
            while (True):
                i = v
                j = w
                init_x = i - i%self.n # find left side of nxn box
                init_y = j - j%self.n # find upper side of nxn box
                for x in range(init_x, init_x + self.n):
                    for y in range(init_y, init_y + self.n):
                        box.append(grid[x][y])
                for value in box:
                    if value[0] not in unique:
                        if value[0] != 0:
                            squareScore += 1
                            unique.append(value[0])
                    else: return False
                unique = [] #reset unique values for next square
                box = []    #reset for next square
                if (w +self.n < self.n**2):
                    w += self.n
                else:
                    w = 0
                    break
            if (v +self.n < self.n**2):
                v += self.n
            else: break

        total_score=squareScore+colScore+rowScore
        if total_score==self.OPTIMAL_SCORE:
            return True
        else:
            return False
    def evaluate_squares(self, grid):
        """
        Helper method that evaluates the score of
        the inner square of the grid. Used to calculate
        total score of Sudoku puzzle.
        """
        box = []
        v = 0
        w = 0
        unique = []
        squareScore = 0
        while (True):
            while (True):
                i = v
                j = w
                init_x = i - i%self.n # find left side of nxn box
                init_y = j - j%self.n # find upper side of nxn box
                for x in range(init_x, init_x + self.n):
                    for y in range(init_y, init_y + self.n):
                        box.append(grid[x][y])
                for value in box:
                    if value[0] not in unique:
                        if value[0] != 0:
                            squareScore += 1
                            unique.append(value[0])
                    else: continue
                unique = [] #reset unique values for next square
                box = []    #reset for next square
                if (w +self.n < self.n**2):
                    w += self.n
                else:
                    w = 0
                    break
            if (v +self.n < self.n**2):
                v += self.n
            else: break
        return squareScore


    def evaluate_sudoku(self, grid):
        """
        This functions runs through the Sudoku grid
        and checks every row, col, and inner squares
        for unique values. Every time a unique value is
        found 1 point gets added to the totalScore.
        The maximum score for a 9x9 puzzle is 243.
        Meaning that there is a unique value in every row, col,
        and inner square.
        """
        unique = []
        rowScore = 0
        colScore = 0
        totalScore = 0
        for i in range(0, self.n**2): #for every row in Grid
            valid_row = [grid[i][x] for x in range(self.n**2)]
            for value in valid_row:
                if value[0] not in unique:
                    if value[0] != 0:
                        rowScore += 1
                        unique.append(value[0])
                else: continue
            unique = [] # reset the unique values for next row
        for j in range(0, self.n**2):  # for every col in Grid
            valid_col = [grid[x][j] for x in range(self.n**2)]
            for value in valid_col:
                if value[0] not in unique:
                    if value[0] != 0:
                        colScore += 1
                        unique.append(value[0])
                else: continue
            unique = [] #reset the unique values for next col
        squareScore = self.evaluate_squares(grid)
        totalScore = rowScore + colScore + squareScore
        return totalScore


    def fill_empty_cells(self, grid):
        for x in range(0, self.n**2):
            for y in range(0, self.n**2):
                tup = grid[x][y]
                if (tup[0] == 0):
                    grid[x][y] = (random.randint(1, self.n**2), True)


    def reset_puzzle(self, grid):
        for x in range(0, self.n**2):
            for y in range(0, self.n**2):
                tup = grid[x][y]
                if tup[1]:
                    while True:
                        for k in range(1, self.n**2+1):
                            r = random.randint(1, self.n**2)
                            if (self.is_valid(grid, x,y,r)):
                                grid[x][y] = (r, True)
                                break
                            else:
                                break
                        break


    def random_swap(self, grid):
        for x in range(0, self.n**2):
            for y in range(0, self.n**2):
                tup = grid[x][y]
                if tup[1]:
                    if (self.is_valid(grid, x,y,grid[x][y][0]) == False):
                        print("invalid")
                        print(grid[x][y])
                        return True

    def reset(self, grid):
        for x in range(0, self.n**2):
            for y in range(0, self.n**2):
                tup = grid[x][y]
                if tup[1]:
                    grid[x][y] = (0, True)

    def hillclimbing_search(self,grid):
        self.reset_puzzle(grid)
        flag = True
        while flag:
            flag = False
            randomNumb = random.randint(0, 100)
            if self.is_solved(grid):
                break
            for i in range(0, self.n**2):
                for j in range(0, self.n**2):
                    i = random.randint(0, self.n**2-1)
                    j = random.randint(0, self.n**2-1)
                    for k in range(1, self.n**2+1):
                        oldScore = self.evaluate_sudoku(grid)
                        temp = grid[i][j]
                        if temp[1]:
                            if (self.is_valid(grid, i,j,k)):
                                grid[i][j] = (k, True)
                        newScore = self.evaluate_sudoku(grid)
                        if (oldScore> newScore):
                            grid[i][j] = temp
                        elif(45 <= randomNumb <= 50):
                            if (self.is_solved(grid)==False):
                                self.reset(grid)
                            flag = True
                        elif(newScore == oldScore):
                            if (self.is_solved(grid)==False):
                                self.reset_puzzle(grid)
                                flag = True
                        else:
                            flag = True
            print(self.evaluate_sudoku(grid))
            pretty_print_puzzle(grid, self.n)
        print(self.evaluate_sudoku(grid))
        return grid

    def  conversion(self, input):
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
                        tup =(cell, False)
                    else:
                        tup =(cell, True)
                    temp.append(tup)
                if len(temp)==n**(2):
                    sudoku.append(temp)
                    temp=[]
        print("Intitial Puzzle")
        pretty_print_puzzle(sudoku, n)
        return sudoku
def pretty_print_puzzle(puzzle,n):

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
