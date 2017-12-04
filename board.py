import pygame
import numpy
import functions
import sys


pygame.init()

background_color = (255,255,255)
WINDOW_DIMENSIONS = (640, 480)
width, height = 640, 480

"""Bunch of variables"""
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption('Connect 4')

class Board:
    def __init__(self, rows, columns, piecesize=100):

        self.rows = rows
        self.columns = columns
        self.matrix = numpy.matrix(functions.createboard(self.rows,self.columns))

    def draw(self, screen):
        # Drawing the grid
        for x in range(0, self.rows * 100, 100):
            for y in range(0, self.columns * 100, 100):
                rectangle =(x,y, 100, 100)
                pygame.draw.rect(screen, (0,0,255), rectangle, 5)

        #drawing the chips
        for x in range(self.rows):
            for y in range(self.columns):
                pos = (x *100 + 50 , y *100 + 50)

                if self.matrix[y, x] == 1:
                    color = (255, 255, 0)   # player 1 is yellow
                elif self.matrix[y, x] == 2:
                    color = (255, 0, 0)     # player 2 is red
                else:
                    continue
                pygame.draw.circle(screen, color , pos, 40)


gameboard = Board(5,4)
#TODO add variability with board size
print(gameboard.matrix)

background_color = (255,255,255)
width, height = 640, 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 3')
screen.fill(background_color)

player = 0
Time = 0
endscreen = False
win = functions.winning(gameboard.matrix,3)

running = True

while running:
    screen.fill((255, 255, 255)) #set up background
    gameboard.draw(screen)
    pygame.display.update()
    if pygame.time.get_ticks() > (Time + 10):
        Time = pygame.time.get_ticks()
        win = functions.winning(gameboard.matrix,3)
        if win[0] == True:
            running = False
            endscreen = True
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if player == 0:
                    player = 1
                elif player == 1:
                    player = 2
                elif player == 2:
                    player = 1
                if event.key == pygame.K_1:
                    functions.look_through_rows(gameboard.matrix, 0, player)
                    print(gameboard.matrix)
                if event.key == pygame.K_2:
                    print(gameboard.matrix)
                    functions.look_through_rows(gameboard.matrix, 1, player)
                if event.key == pygame.K_3:
                    functions.look_through_rows(gameboard.matrix, 2, player)
                    print(gameboard.matrix)
                if event.key == pygame.K_4:
                    functions.look_through_rows(gameboard.matrix, 3, player)
                    print(gameboard.matrix)
                if event.key == pygame.K_5:
                    functions.look_through_rows(gameboard.matrix, 4, player)
                    print(gameboard.matrix)
                #TODO change the event keys to take in nay rows not just
                # up to 5.
                gameboard.draw(screen)
                pygame.display.update()

while endscreen:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

        basicfont = pygame.font.SysFont(None, 20)
        text = basicfont.render('Congrats! Player %.2d'%(win[1]) + ' Has Won', True, (0, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)

    pygame.display.update()

pygame.quit()
