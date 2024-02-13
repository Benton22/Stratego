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
    spawnerRed.append(PieceSpawner((i*2) * width/24 - width/22, height - 2 * height/48, 30, str(i), i, False))
spawnerRed.append(PieceSpawner((10*2) * width/24 - width/22, height - 2 * height/48, 30, "S", "S", False))
spawnerRed.append(PieceSpawner((11*2) * width/24 - width/22, height - 2 * height/48, 30, "Stratego\Images\Bomb.png", "B", True))
spawnerRed.append(PieceSpawner((12*2) * width/24 - width/22, height - 2 * height/48, 30, "Stratego\Images\Flag.png", "F", True))

print(grid)

def gameLogic(screen):
    for numSpawner in range(len(spawnerRed)):
        spawnerRed[numSpawner].draw(screen)

    xIndex, yIndex = gridIndexer()






def gridIndexer():
    xIndex = 0
    yIndex = 0
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

    if mouseY < 2 * width/10:
        yIndex = 1
    elif mouseY < 3 * width/10 + 3:
        yIndex = 2
    elif mouseY < 4 * width/10 + 3:
        yIndex = 3
    elif mouseY < 5 * width/10 + 3:
        yIndex = 4
    elif mouseY < 6 * width/10 + 3:
        yIndex = 5
    elif mouseY < 7 * width/10 + 3:
        yIndex = 6
    elif mouseY < 8 * width/10 + 3:
        yIndex = 7
    elif mouseY < 9 * width/10 + 3:
        yIndex = 8
    elif mouseY < 10 * width/10 + 3:
        yIndex = 9
    else:
        yIndex = 10
    return(xIndex, yIndex)
