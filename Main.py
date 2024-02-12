import pygame
import sys
pygame.init()

from Screens.Board import BoardScreen
from Screens.Menu import MenuScreen
from Logic.Buttons import BasicButton

ScreenIndex = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    height = 1000
    width = height * 10 / 12
    size = width, height
    black = 0, 0, 0
    background = 43,43,43
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)

    if ScreenIndex == 1: MenuScreen(screen)
    elif ScreenIndex == 2: BoardScreen(screen)

    # Update display
    pygame.display.flip()