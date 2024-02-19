import pygame
import sys
from .Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground
from .Logic.ActualGame import gameLogic

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
lighterBackground = (56, 56, 56)
white = 255, 255, 255
gridSize = 11
gridLinesH = []
gridLinesV = []
gridLineFiller = []
gameState = "Setup"

#Draw the Grid -----------------------------------------------------------Draw the Grid
class GridLines():
    def __init__(self, locationX, locationY, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.locationX = locationX
        self.locationY = locationY
        self.Bezel = 1
        self.outerLine = pygame.Rect(self.locationX, self.locationY, self.sizeX, self.sizeY)
        self.innerLine = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, sizeX - 2 * self.Bezel, sizeY - 2 * self.Bezel)

#standard grid
for i in range(0, gridSize):
    gridLinesH.append (GridLines(0, (i * height/12) + height/12-3, width+6, 6))
    gridLinesV.append (GridLines((i * height/12), height/12, 6, width))
#filling in the gaps
gridLineFiller.append(GridLines(0, height/2 - 3, 2 * width/10 + 3, 6))
gridLineFiller.append(GridLines(4 * width/10 + 3, height/2 - 3, 2 * width/10, 6))
gridLineFiller.append(GridLines(8 * width/10 + 3, height/2 - 3, 2 * width/10, 6))
gridLineFiller.append(GridLines((3 * height/12), height/12, 6, 4* height/12))
gridLineFiller.append(GridLines((7 * height/12), height/12, 6, 4* height/12))
gridLineFiller.append(GridLines((3 * height/12), 6 * height/12 + height/12, 6, 4* height/12))
gridLineFiller.append(GridLines((7 * height/12), 6 * height/12 + height/12, 6, 4* height/12))

#Draw the Grid -----------------------------------------------------------Draw the Grid


cannotPlace = pygame.Rect(0, 7 * height/12, width, 4 * height/12)


def BoardScreen(screen, CurrentScreenIndex):
    running = True
    global gameState
    while running:
        mousePressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePressed = True


        # Drawing
        screen.fill(background)

        if gameState == "Setup":
            pygame.draw.rect(screen, lighterBackground, cannotPlace)

        for gridLine in range(len(gridLinesH)):
            if gridLine != 5:
                pygame.draw.rect(screen, black, gridLinesH[gridLine].outerLine)
            if gridLine != 3 and gridLine != 7:
                pygame.draw.rect(screen, black, gridLinesV[gridLine].outerLine)

        for gridLine in range(len(gridLineFiller)):
            pygame.draw.rect(screen, black, gridLineFiller[gridLine].outerLine)

        for gridLine in range(len(gridLinesH)):
            if gridLine != 5:
                pygame.draw.rect(screen, white, gridLinesH[gridLine].innerLine)
            if gridLine != 3 and gridLine != 7:
                pygame.draw.rect(screen, white, gridLinesV[gridLine].innerLine)

        for gridLine in range(len(gridLineFiller)):
            pygame.draw.rect(screen, white, gridLineFiller[gridLine].innerLine)

        gameState = gameLogic(screen, mousePressed, gameState)



        # Update display
        pygame.display.flip()
