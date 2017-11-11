#Author: Siena and Felix
#Date: 11/7/2017
#Determines if game is won and by who when given a matrix
import numpy

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
    #diagonal pos

    #diagonal neg
    #tie

    return False, 0

def scoring(matrix, connect):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    a = winning(matrix, connect)[0]
    score = 0
    if a == False:
        #horizontal
        for x in range(rows):
            for y in range(columns-1):
                if matrix[x,y] == matrix[x,y+1] and matrix[x,y] != 0:     #add another == for Connect 4
                    score += 3
                    print('2x')
            if score == 0:
                for y in range(columns):
                    if matrix[x,y] != 0:
                        score += 1
                        print('1x')
        #vertical
        for y in range(columns):
            for x in range(rows-1):
                if matrix[x,y] == matrix[x+1,y] and matrix[x,y] != 0:     #add another == for Connect 4
                    score += 3
                    print("2y")
            if score == 0:
                for x in range(rows):
                        if matrix[x,y] != 0:
                            score += 1
                            print("1y")
    elif a == True:
        score = 10
    return score

a = numpy.matrix('0 0 1 0; 0 0 1 0; 0 0 1 0')
print(scoring(a,3))
