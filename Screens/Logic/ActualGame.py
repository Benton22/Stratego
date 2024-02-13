import pygame
import sys
from .Variables.Globals import globalheight, globalwidth, globalsize, globalbackground
from .Buttons import PieceSpawner

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255

#making the grid
grid = [[0 for i in range(10)] for j in range(10)]

for i in range(2,4):
    for j in range(4,6):
        grid[i][j] = "x"
for i in range(6,8):
    for j in range(4,6):
        grid[i][j] = "x"



class Piece():
    def __init__(self, pos, type, team):
        self.pos = pos
        self.type = type
        self.team = team

spawnerRed = []
for i in range(1,10):
    spawnerRed.append(PieceSpawner((i*2) * width/22 - width/22, height - 2 * height/48, 30, str(i), i))

print(grid)

def gameLogic(screen):
    for numSpawner in range(len(spawnerRed)):
        spawnerRed[numSpawner].draw(screen)
    #finding part of grid mouse is in
    
    xIndex = 0
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX < width/10:
        xIndex = 1
    elif mouseX < 2 * width/10 + 3:
        xIndex = 2
    elif mouseX < 3 * width/10 + 3:
        xIndex = 3
    elif mouseX < 4 * width/10 + 3:
        xIndex = 4
    elif mouseX < 5 * width/10 + 3:
        xIndex = 5
    elif mouseX < 6 * width/10 + 3:
        xIndex = 6
    elif mouseX < 7 * width/10 + 3:
        xIndex = 7
    elif mouseX < 8 * width/10 + 3:
        xIndex = 8
    elif mouseX < 9 * width/10 + 3:
        xIndex = 9
    else:
        xIndex = 10
    print(xIndex)
