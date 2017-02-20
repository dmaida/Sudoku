import sys
import os
import math
import numpy








def  input_conversion(input='1...............'):
    n=len(input)**(1/4)
    if n-int(n)!=0:
        print("Not a valid sudoku string. Please try again.")
        return
    else:
        n= int(n)
    sudoku=[]


    '''Two for loops
     The loop will go 0-n^2 if a dot meaning a blank space is in input a zero will be put in
    '''
    temp=[]
    
    for i in range( len(input)):


        if len(temp)<n**(2):
            if input[i]=='.':
                temp.append(0)
            else:
                temp.append(int(input[i]))
        if len(temp)==n**(2):
            sudoku.append(temp)
            temp=[]

    pretty_print_puzzle(sudoku,n)


def pretty_print_puzzle(puzzle,n):

    row_number=0

    for row in puzzle:
        row_string='|'
        row_number+=1
        for spot in range(len(row)):
            if spot%n==0 and spot !=0:
                row_string=row_string+' | '+str(row[spot])
            else:
                row_string=row_string+' '+str(row[spot])
        print(row_string+' | ')
        if row_number%n==0 and row_number!= len(puzzle):
            print(  '')

        row_string=''





if __name__ == "__main__":
    input_conversion()
