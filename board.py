import pygame

WINDOW_DIMENSIONS = (800, 800)  # Width and height of the pygame window

class Board:
    def __init__(self, p1, p2, piecesize=100):

        width, height = 5, 4

        self.PIECESIZE = piecesize
        self.BOARDWIDTH = width*piecesize
        self.BOARDHEIGHT = height*piecesize
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = (0, 0, 255)
        self.XMARG = (WINDOW_DIMENSIONS[0] - self.BOARDWIDTH) // 2
        self.YMARG = WINDOW_DIMENSIONS[1] // 4
        self.RECT = pygame.Rect(self.XMARG, self.YMARG,
                                self.BOARDWIDTH, self.BOARDHEIGHT)
        self.TURN = 0

        self.COUNT1 = 0  # player 1 moves
        self.COUNT2 = 0  # player 2 moves

        self.PLAYERS = (p1, p2)


def placePiece(board, column, piece):
    if board[column] == ' ':
        lowestOpenRow = column
        for i in range(4):
            if board[column + (5 * i)] == ' ':
                lowestOpenRow = i
        board[lowestOpenRow * 5 + column] = piece
        return board
    else:
        return board

def printBoard(board):
    for i in range(len(board)):
        if board[i] == player1:
            board[count,column] == 1
        elif board[i] == player2:
            board[count,column] == 2

def getOpenSpaces(board):
    openSpaces = 0
    for space in board:
        if space == ' ':
            openSpaces += 1

    return openSpaces
