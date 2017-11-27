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


def minimax(node, depth, myTurn, matrix, connect):
    """Evaluation of scores and nodes to pick the best move.
    Takes depth, boolean of myTurn, matrix of the playing field, and # to connect.
    Returns an """
    print('hello')
    if depth == 0: # or node is terminal
        print("a")
        a = scoring(matrix, connect, myTurn)
        return a
    elif myTurn:
        #bestValue = -10
        for child in range(node):
            #place piece in column child
            print('myTurn')
            v = minimax(child, depth-1, False, matrix, connect)
            #bestValue =
            return (v, child)
    elif not myTurn:
        #bestValue = 10
        for child in range(node):
            #place piece in column child
            print('not myTurn')
            v = minimax(child, depth-1, True, matrix, connect)
            #bestValue =
            return (v, child)
    else:
        return 'Sad'

# a = numpy.matrix('0 1 0 1; 0 1 0 0; 0 0 0 0')
# print(minimax(4, 4, True, a, 3))

def scoring(draw):
    """generate random output"""
    return int(draw)

def create_gametree(depth, nodes=5):
    """create a gametree for the game of connect 3

    Args:
       depth: how many draws in advance
       nodes: possible draws

    Returns:
        Gametree in form nested lists
    """
    final_score = []
    if depth > 1:
        Gametree = []
        for i in range(nodes):
            # which draw = i
            # which depth = original depth - depth
            Gametree.append(scoring(i))
            Gametree.append(create_gametree(depth-1))
        return Gametree
    elif depth == 1: #Basecase
        for k in range(nodes):
            final_score.append(scoring(k))
        return final_score

print(create_gametree(2, 5))


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
