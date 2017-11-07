import pygame
import sys
pygame.init()


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
