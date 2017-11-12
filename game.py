#this is the file for our game

import pygame
import sys
import numpy
pygame.init()


background_color = (255,255,255)
width, height = 640, 480

"""Bunch of variables"""
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 4')


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

player = 0

def look_through_rows(board, column, player):
    count = 3
    count2 = 1
    while count >= 0 and count2 == 1:
        if board[count,column] == 0:
            board[count,column] = player
            count2 = count2 - 1
        else:
            count = count - 1
    return board



#Keyboard input for player. Can be completed after structure of matrix is set.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if player == 0:
                    player = 1
                elif player == 1:
                    player = 2
                elif player == 2:
                    player = 1
                if event.key == pygame.K_1:
                    look_through_rows(board, 0, player)
                    print(board)
                if event.key == pygame.K_2:
                    look_through_rows(board, 1, player)
                    print(board)
                if event.key == pygame.K_3:
                    look_through_rows(board, 2, player)
                    print(board)
                if event.key == pygame.K_4:
                    look_through_rows(board, 3, player)
                    print(board)
                if event.key == pygame.K_5:
                    look_through_rows(board, 4, player)
                    print(board)

pygame.quit()
            # if event.key == K_2:
            #     #place in second column of matrix, set 0 in lowest row within column to 1
            # if event.key == K_3:
            #     #place in third column of matrix, set 0 in lowest row within column to 1
            # if event.key == K_4:
            #     #place in fourth column of matrix, set 0 in lowest row within column to 1
            # if event.key == K_5:
            #     #place in fifth column of matrix, set 0 in lowest row within column to 1
