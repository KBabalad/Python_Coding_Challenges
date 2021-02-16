"""
Solve sudoko is a puzzle solving excercise in which we take a 2 dimensional list that has an input of 9X9 inputs in which
the inputs we need to solve will be written as zero for empty spaces we need to enter and the others will numbers from 1-9.
Here we find the 0 in the list check whether it is in that particular row, column and the 3x3 box.
If the we find a zer then think of how we replace itwith the suitable right sudoko value for a perfect sudoko
"""

from itertools import product

def sudoko_puzzle(puzzle):
    for (row,col) in product(range(0,9),repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1,10):
                allowed =True
                for i in range(0,9):
                    if(puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False; break
                for (i,j) in product(range(0,3),repeat=2):
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False; break
                if allowed:
                    puzzle[row][col] = num
                    if trial := sudoko_puzzle(puzzle):
                        return trial
                    else:
                        puzzle[row][col]=0
            return False
    print_puzzle(puzzle)
    return puzzle

def print_puzzle(puzzle):
    # print '*' in place of 0 if non zero print value num
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0,9):
        if ((row%3 ==0) and (row!=0)):
            print('-'*33) # draw horizontal line
        for col in  range(0,9):
            if((col%3==0) and (col !=0)):
                print('|' , end = '') # draw vertical line
            print('',puzzle[row][col],'', end='')
        print()
    print()

if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print_puzzle(puzzle)
    sudoko_puzzle(puzzle)



