import pygame
import sys
from Screens.Logic.Buttons import BasicButton
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground



height = 1000
width = height * 10 / 12
size = width, height
black = 0, 0, 0
background = 43,43,43
white = 255, 255, 255


StartButton = BasicButton(width/2 - 70, height/2, 140, 80, "Start")




def MenuScreen(screen, CurrentScreenIndex):
    running = True

    pygame.display.set_caption("Stratego")
    font = pygame.font.Font(pygame.font.get_default_font(), 64)
    text = font.render('Stratego', True, white)
    textRect = text.get_rect()
    textRect.center = (width / 2, height / 4)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Your game logic goes here
        if event.type == pygame.MOUSEBUTTONDOWN:
            if StartButton.over_button():
                CurrentScreenIndex[0] = 2
                return CurrentScreenIndex

        # Clear the screen
        screen.fill(background)
        screen.blit(text, textRect)
        StartButton.draw(screen)

        # Update display
        pygame.display.flip()
    print(CurrentScreenIndex)
    return CurrentScreenIndex
