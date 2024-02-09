import pygame
import sys

# Initialize Pygame
pygame.init()

height = 1000
width = height * 10 / 12
size = width, height
black = 0, 0, 0
background = 43,43,43
white = 255, 255, 255
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stratego")



font = pygame.font.Font(pygame.font.get_default_font(), 32)
text = font.render('Stratego', True, white)
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(background)

    screen.blit(text, textRect)


    # Update display
    pygame.display.flip()