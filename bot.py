#authors: Siena and Felix
# Needed functions isLegalMove
#new variables: board = matrix,
#

import pygame
import random
import sys
from pynput.keyboard import Key, Controller
from winning import *
keyboard = Controller()

pygame.init()
#c1location = (1,1)
#c2location = (2,1)
#c3location = (3,1)
#c4location = (4,2)
#c5location = (5,1)
#MOUSE = pygame.USEREVENT + 1
#column1 = pygame.event.Event(MOUSE, location=c1location)
#pygame.event.post(column1)
#pygame.event.get
#done = False
#while not done:
#    for event in pygame.event.get():
#        if event.type == MOUSE:
#            print("column1")
#            done = True
#    pygame.event.pump()

def minimax(node, depth, myTurn, matrix, connect=3):
    """Evaluation of scores and nodes to pick the best move.
    Takes depth, boolean of myTurn, matrix of the playing field, and # to connect.
    Returns an integer of score"""
    gametree = [0]*(node)
    print(gametree)

    '''Fix me! I place pieces and store them in new matrices
    rows = 4
    # enumerate all possible moves from this board
    legal_moves = []
    for i in range(rows):
        # if column i is a legal move
        if isLegalMove(board, i):
            # make the move in column i for curr_player
            temp = makeMove(i, board, myTurn)
            # create list of matrix
            legal_moves.append(temp)
    '''

    if depth == 0 or winning(matrix)[0]: # or len(legal_moves)==0:
        a = scoring(matrix, connect, myTurn)
        print(matrix)
        print('depth' + str(depth))
        return a
    elif myTurn:
        #bestValue = -10000
        for child in range(node):
            #place piece?
            print(child, myTurn)
            #call on node???
            gametree[child-1] = minimax(node, depth-1, False, matrix, connect=3)
            #bestValue = ...
    elif not myTurn:
        #bestValue = 10000
        for child in range(node): #legal_moves:
            #place piece?
            print(child, myTurn, node)
            gametree[child-1] = minimax(node, depth-1, True, matrix, connect=3)
            #bestValue = ...
    return gametree

a = numpy.matrix('0 1 0 1 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0')
# print(minimax(4, 3, True, a))


def search(depth, board, myTurn):
        """ Search the tree until depth 'depth'
            By default, the  is the board, and curr_player is whomever called this search
            Return score
        """
        rows = 4
        # enumerate all possible moves from this board
        legal_moves = []
        for i in range(rows):
            # if column i is a legal move
            if isLegalMove(board, i):
                # make the move in column i for curr_player
                temp = makeMove(i, board, myTurn)
                # create list of matrix
                legal_moves.append(temp)

        #TODO: CONSULTING
        # BASECASE (if depth == 0, game tied or someone wins)
        if depth == 0 or len(legal_moves) == 0 or winning(board):
            # return value(board, curr_player) from winning
            return scoring(s, connect, myTurn)

        # determine opponent's color - PROBABLY NOT NECESSARY
        # if curr_player == self.colors[0]:
        #     opp_player = self.colors[1]
        # else:
        #     opp_player = self.colors[0]

        #TODO: CONSULTING, how doe
        # RECURSION
        score = -99999999
        for child in legal_moves:
            if child == None:
                print("child == None (search)")
                # start recursion, check if minus is necessary
<<<<<<< HEAD
            score = max(score, -search(depth-1, child, False))
            # score negative or positive
=======
            score = max(score, -search(depth-1, child, opp_player))
            # score negative or positive???
>>>>>>> c474be841c42ebb7defc375c54cce74bb3f03aec
        return score

def choose_options(depth, board, myTurn):
    """
    INPUT: depth(integer), board(matrix), myTurn(boolean)

    OUTPUT: column (integer) were we should place our piece
    """
    rows = 4
    columns = 5
    possible_moves = {} # possible moves (key) and their scores (value)
    for column in range(columns):
        # check if column i is a possible
        if isLegalMove(board, column):
            # make the move in column  for curr_player
            temp = makeMove(column, board, myTurn)
            # assign overall score (value, recurs function) to every column (key)
            #TODO: CONSULTING
            possible_moves[column] = -search(depth-1, temp, False)
            # minus maybe has to stay depending on scoring implementation
    # return the key(column) for the best score
    return best_option(possible_moves)

def best_option(options={1: 3, 2: 6, 3: 100}):
    """
    INPUT: options with score (dict)

    choose the the highest value
    return the key (branch) of the maximum value (score)
    if no option given, choose the middle column(3)

    OUTPUT: column (integer) were we should place our piece
    """
    # find the best option (max score)
    best_option = max(possible_moves, key=options.get)
    return str(best_option)

def makeMove(column, board, myTurn, connect=3):
    """
    Input: column (int), whose turn (boolean), and the board (matrix)
    What: insert your coin in the column you chose
    How: find the first empty (0) spot in the column and replace with your number
    Output: the new board
    >>> makeMove(1, board, True)
    [[0, 2, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    # adapt the number of rows to the game
    if connect == 3:
        rows=4
    else:
        rows = 6
    # check if it is my turn
    if myTurn == True:
        coin = 1
    else:
        coin = 2

    # for matrix---------
        board_temp = board
        for i in range(rows):
            if board_temp[i, column] == 0:
                board_temp[i, column] = coin
                return board_temp

def isLegalMove(board, column):
    """
    Input: board (matrix), column (int)
    Check if there is a space left in the column
    output: boolean"""
    # loop through every row of a column
    rows = 4
    for i in range(rows):
        if board[i, column] == 0:
            # as soon as we find the first empty spot return True
            return True
    # if we iterated through all rows
    return False

def random_choice():
    """Choose random column"""
    columns= [0, 1, 2, 3, 4]
    chosen_column = random.choice(columns)
    return str(chosen_column)

def simulate_keypress(keypress):
    """simulates keypress"""
    keyboard.press(keypress)
    keyboard.release(keypress)


def bot_player(depth, board, myTurn):
    """
    concludes every necessary functions for AI
    """
    return chosen_column(random_choice())
    # return simulate_keypress(choose_options(depth, board, myTurn))
    # choose best option
    # simulate keypress


# simulate_keypress(choose_option())
choose_options(4, a, True)
