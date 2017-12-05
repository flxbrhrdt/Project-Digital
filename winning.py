#Author: Siena and Felix
#Date: 11/7/2017
#Determines if game is won and by who when given a matrix
import numpy

def winning(matrix, connect=3):
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
    #tie
    if numpy.count_nonzero(arrayM) == rows*columns:
        return True, 0
    #if not won
    return False, 0

def scoring(matrix, connect, myTurn):
    '''Scores matrix position)'''
    #TODO: add myTurn
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    a = winning(matrix, connect)[0]
    b = winning(matrix, connect)[1]
    score1 = 0
    score2 = 0
    if a == True:
        if b == 1:
            score1 = 50
        elif b == 2:
            score2 = 50
    else:
        #horizontal
        for x in range(rows):
            for y in range(columns-1):
                if matrix[x,y] == matrix[x,y+1] and matrix[x,y] == 1 and not myTurn:     #add another == for Connect 4
                    score1 += 3
                elif matrix[x,y] == matrix[x,y+1] and matrix[x,y] == 2 and myTurn:     #add another == for Connect 4
                    score2 += 3
        #vertical
        for y in range(columns):
            for x in range(rows-1):
                if matrix[x,y] == matrix[x+1,y] and matrix[x,y] == 1 and not myTurn:     #add another == for Connect 4
                    score1 += 3
                elif matrix[x,y] == matrix[x+1,y] and matrix[x,y] == 2 and myTurn:     #add another == for Connect 4
                    score2 += 3

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
                if a[i] == a[i++1] and a[i] == 1 and not myTurn:
                    score1 += 3
                elif a[i] == a[i++1] and a[i] == 2 and myTurn:
                    score2 += 3
        #reverse diagonal
        arrayM = numpy.asarray(numpy.fliplr(matrix))
        for x in range(longer-1):
            a = numpy.diagonal(arrayM,x-(rows-connect+1))
            for i in range(len(a)-connect+1):
                if a[i] == a[i++1] == a[i+2] and a[i] == 1 and not myTurn:
                    score1 +=3
                elif a[i] == a[i++1] == a[i+2] and a[i] == 2 and myTurn:
                    score2 += 3
    if not myTurn:
        return score1
    elif myTurn:
        return score2


a = numpy.matrix('1 1 1 0; 0 0 0 0; 0 0 0 0')
# print(scoring(a,3))
