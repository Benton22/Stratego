import pygame
import sys
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground
from Screens.Logic.Buttons import PieceSpawner

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255

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
    spawnerRed.append(PieceSpawner((i*2) * width/22, 2* height/48, 30, str(i), i))

print(grid)

def drawGame(screen):
    for numSpawner in range(len(spawnerRed)):
        spawnerRed[numSpawner].draw(screen)
