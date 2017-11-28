import pygame
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
    Returns an """
    if depth == 0 or winning(matrix)[0]:
        a = scoring(matrix, connect, myTurn)
        # print(matrix)
        # print('depth' + str(depth))
        return a
    elif myTurn:
        #bestValue = -10
        # for child in range(node):
            #place piece in column child
        print('depth' + str(depth), ', myTurn')
        v = [minimax(0, depth-1, True, matrix, connect), minimax(1, depth-1, False, matrix, connect), minimax(2, depth-1, True, matrix, connect), minimax(3, depth-1, True, matrix, connect)]
            #bestValue
        return v
    elif not myTurn:
        #bestValue = 10
        # for child in range(node):
            #place piece in column child
        print('depth' + str(depth), ', not myTurn')
        v = [minimax(0, depth-1, True, matrix, connect), minimax(1, depth-1, True, matrix, connect), minimax(2, depth-1, True, matrix, connect), minimax(3, depth-1, True, matrix, connect)]
            #bestValue =
        return v
    else:
        return 'Sad'

a = numpy.matrix('0 1 0 1; 0 0 0 0; 0 0 0 0')
print(minimax(4, 4, True, a))

def choose_option(options={3:100}):
    """choose the the highest value
    return the key (branch) of the maximum value (score)
    if no option given, choose the middle column(3)
    """
    best_option = max(options, key=options.get)
    return str(best_option)

def simulate_keypress(keypress):
    """simulates keypress"""
    keyboard.press(keypress)
    keyboard.release(keypress)

# simulate_keypress(choose_option())
