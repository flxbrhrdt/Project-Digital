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
            if matrix[x+1,y] == matrix[x+1,y] == matrix[x+2,y] and matrix[x,y] != 0:     #add another == for Connect 4
                return True, matrix[x,y]

    #diagonal pos
    
    #diagonal neg
    #tie

    return False, 0

a = numpy.matrix('1 0 0 0; 0 0 0 1; 1 0 1 0')
print(winning(a,3))
