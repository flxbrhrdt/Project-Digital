#Author: Siena and Felix
#Date: 11/7/2017
#Determines if game is won and by who when given a matrix

def winning(matrix, connect):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    #horizontal
    for x in range(rows):
        row = []
        for y in (range(columns):
            row.append[x,y]
        for i in range(columns-connect+1):
            if row[i] == row[i+1] == row[i+2]     #add another == for Connect 4
                return row[i]
    #vertical
    for x in range(columns):
        column = []
        for y in (range(rows):
            column.append[x,y]
        for i in range(rows-connect+1):
            if column[i] == column[i+1] == column[i+2]     #add another == for Connect 4
                return row[i]
    #diagonal pos

    #diagonal neg

    #tie
