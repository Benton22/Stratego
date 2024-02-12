import pygame
import sys




def MenuScreen(screen):
    running = True
    height = 1000
    width = height * 10 / 12
    size = width, height
    black = 0, 0, 0
    background = 43,43,43
    white = 255, 255, 255

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
        

        # Clear the screen
        screen.fill(background)
        screen.blit(text, textRect)

        # Update display
        pygame.display.flip()
