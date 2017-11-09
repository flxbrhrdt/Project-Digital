import pygame
import sys

pygame.init()

#simulate keypress
from pynput.keyboard import Key, Controller
keyboard = Controller()

c1location = (1,1)
c2location = (2,1)
c3location = (3,1)
c4location = (4,2)
c5location = (5,1)
MOUSE = pygame.USEREVENT + 1
column1 = pygame.event.Event(MOUSE, location=c1location)
pygame.event.post(column1)


pygame.event.get
done = False
while not done:
    for event in pygame.event.get():
        if event.type == MOUSE:
            print("column1")
            done = True
    pygame.event.pump()

def choose_option():
    return 4

def fake_keydown():
    """ creates a key.down output for the game script """
    if choose_option() == 1:
        simulate_keypress('1')
    elif choose_option() == 2:
        simulate_keypress('2')
    elif choose_option() == 3:
        simulate_keypress('3')
    elif choose_option() == 4:
        simulate_keypress('4')
    if choose_option() == 5:
        simulate_keypress('5')
    else:
        simulate_keypress('3')
    pass

def simulate_keypress(keypress):
    """simulates keypress """
    keyboard.press(keypress)
    keyboard.release(keypress)

fake_keydown()
