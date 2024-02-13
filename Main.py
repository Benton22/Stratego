import pygame
import sys
pygame.init()

from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground
from Screens.Board import BoardScreen
from Screens.Menu import MenuScreen
from Screens.Logic.Buttons import BasicButton

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255

ScreenIndex = [1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen = pygame.display.set_mode(size)

    if ScreenIndex[0] == 1: MenuScreen(screen, ScreenIndex)
    elif ScreenIndex[0] == 2: BoardScreen(screen, ScreenIndex)

    
    # Update display
    pygame.display.flip()