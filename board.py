import pygame
import numpy
import functions
import sys
import fake_bot


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

### Set colors and dimensions of board
background_color = (255,255,255)    #white
#width, height = 700 , 500           #screen dimensions for connect 4
width, height = 500, 400            #screen dimensions for connect 3
black = (0,0,0)

### Initializing game environment
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 3')
screen.fill(background_color)

### Initializing and printing board
gameboard = Board(5,4)
print(gameboard.matrix)

player = 0
Time = 0
endscreen = False
win = functions.winning(gameboard.matrix,3)

font = pygame.font.SysFont("Lucida Sans Typewriter", 50)
text1 = font.render("Welcome to Connect 3", True, black)
screen.blit(text1, (180, 100))
pygame.display.update()

running = True

while running:
    screen.fill((255, 255, 255)) #set up background
    gameboard.draw(screen)
    pygame.display.update()


    for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                # c = pygame.key.get_pressed()
                # functions.look_through_rows(gameboard.matrix, functions.pygame_key_reader(c) ,player)
                if event.key == pygame.K_1:
                    functions.look_through_rows(gameboard.matrix, 0, player)
                if event.key == pygame.K_2:
                    functions.look_through_rows(gameboard.matrix, 1, player)
                if event.key == pygame.K_3:
                    functions.look_through_rows(gameboard.matrix, 2, player)
                if event.key == pygame.K_4:
                    functions.look_through_rows(gameboard.matrix, 3, player)
                if event.key == pygame.K_5:
                    functions.look_through_rows(gameboard.matrix, 4, player)
                print(gameboard.matrix)

                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1

                gameboard.draw(screen)
                pygame.display.update()

            win = functions.winning(gameboard.matrix,3)
            if win[0] == True:
                running = False
                endscreen = True

            if player == 2:
                fake_bot.fake_player(4, gameboard.matrix)

            win = functions.winning(gameboard.matrix,3)
            if win[0] == True:
                running = False
                endscreen = True

    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            pygame.quit()
            quit()


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
