import numpy
import pygame

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

def winning(matrix, connect):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    #horizontal
    for x in range(rows):
        for y in range(columns-connect+1):
            if matrix[x,y] == matrix[x,y+1] == matrix[x,y+2] and matrix[x,y] != 0:     #add another == for Connect 4
                return True, matrix[x,y]
    #vertical
    for y in range(columns):
        for x in range(rows-connect+1):
            if matrix[x,y] == matrix[x+1,y] == matrix[x+2,y] and matrix[x,y] != 0:     #add another == for Connect 4
                return True, matrix[x,y]
    #determines which side is longer for diagonal search
    if rows>columns:
        longer = rows
    else:
        longer = columns
    #diagonal
    arrayM = numpy.asarray(matrix)
    for x in range(longer-1):
        a = numpy.diagonal(arrayM,x-(rows-connect+1))
        for i in range(len(a)-connect+1):
            if a[i] == a[i++1] == a[i+2] and a[i] !=0:
                return True, a[i]
    #reverse diagonal
    arrayM = numpy.asarray(numpy.fliplr(matrix))
    for x in range(longer-1):
        a = numpy.diagonal(arrayM,x-(rows-connect+1))
        for i in range(len(a)-connect+1):
            if a[i] == a[i++1] == a[i+2] and a[i] !=0:
                return True, a[i]
    if numpy.count_nonzero(arrayM) == rows*columns:
        return True, 0
        #if not won
    return False, 0

def look_through_rows(board, column, player):
    if board.shape[1] > column:
        count = board.shape[0] - 1
        count2 = 1
        while count >= 0 and count2 == 1:
            if board[count,column] == 0:
                board[count,column] = player
                count2 = count2 - 1
            else:
                count = count - 1
        return board
    else:
        print('Improper Column Given')

# def pygame_key_reader(key):
#     if key[49] == 1:
#         return 0
#     if key[50] == 1:
#         return 1
#     if key[51] == 1:
#         return 2
#     if key[52] == 1:
#         return 3
#     if key[53] == 1:
#         return 4
#     if key[54] == 1:
#         return 5
#     if key[55] == 1:
#         return 6
#     if key[56] == 1:
#         return 7
#     else:
#         return 'Broken'
