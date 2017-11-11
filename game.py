#this is the file for our game

import pygame
import sys
import numpy
pygame.init()

#Enter classes
# class player(object):
#
#     def __init__():
#
#     def __repr__():
#
#     def draw():

def createboard(rows,columns):
    row_size = ''
    for rows in range(rows):
        if rows == 0:
            row_size = row_size + '0'
        else:
            row_size = row_size + ',0'
    fullmatrix = ''
    for cols in range(columns):
        if cols == 0:
            fullmatrix = fullmatrix + row_size
        else:
            fullmatrix = fullmatrix + '; ' + row_size
    return fullmatrix


board = numpy.matrix('0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0')
print(board)




#Keyboard input for player. Can be completed after structure of matrix is set.
for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_1:
                for element in reversed(board[:,0]):
                    if board[element,0] == 0:
                        board[element,0] = 1
            #
            # if event.key == K_2:
            #     #place in second column of matrix, set 0 in lowest row within column to 1
            # if event.key == K_3:
            #     #place in third column of matrix, set 0 in lowest row within column to 1
            # if event.key == K_4:
            #     #place in fourth column of matrix, set 0 in lowest row within column to 1
            # if event.key == K_5:
            #     #place in fifth column of matrix, set 0 in lowest row within column to 1
