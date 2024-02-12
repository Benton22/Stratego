import pygame
import sys

def BoardScreen(screen):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Your game logic goes here
        

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update display
        pygame.display.flip()
