import pygame
import sys
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255
gridSize = 10
gridLinesH = []

def BoardScreen(screen, CurrentScreenIndex):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Your game logic goes here
        class GridLines():
            def __init__(self, locationX, locationY, sizeX, sizeY):
                self.hovering = False
                self.sizeX = sizeX
                self.sizeY = sizeY
                self.locationX = locationX
                self.locationY = locationY
                self.Bezel = sizeX/20
                self.outerButton = pygame.Rect(self.locationX, self.locationY, self.sizeX, self.sizeY)
                self.innerButton = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, sizeX - 2 * self.Bezel, sizeY - 2 * self.Bezel)
        
        for i in range(0, gridSize):
            gridLinesH [i] = GridLines(0, gridlines)

        # Drawing
        screen.fill(background)

        # Update display
        pygame.display.flip()
