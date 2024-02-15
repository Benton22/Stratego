import pygame
import sys
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground

flagPath = "Stratego\\Pieces\\Flag.png"
bombPath = "Stratego\\Pieces\\Bomb.png"

bgray1 = (62, 62, 62)
bgray2 = (100, 100, 100)
bgray3 = (80, 80, 80)

class Piece ():
    def __init__(self, locationX, locationY, size, type, moving):
        self.locationX = locationX
        self.locationY = locationY
        self.size = size
        self.type = type
        self.png = True
        self.Bezel = 6
        self.outerSquare = pygame.Rect(self.locationX, self.locationY, self.size, self.size)
        self.innerSquare = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, self.size - 2 * self.Bezel, self.size - 2 * self.Bezel)
        self.moving = moving
        
        if self.type != "F" and self.type != "B":
            self.text = str(self.type)
            self.png = False
        elif self.type == "F":
            self.text = flagPath
        else:
            self.text = bombPath


    def draw(self, screen):

        if self.moving:
            mouseXdrag, mouseYdrag = pygame.mouse.get_pos()
            self.locationX = mouseXdrag - self.size/2
            self.locationY = mouseYdrag - self.size/2
            self.outerSquare = pygame.Rect(self.locationX, self.locationY, self.size, self.size)
            self.innerSquare = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, self.size - 2 * self.Bezel, self.size - 2 * self.Bezel)
        pygame.draw.rect(screen, bgray3, self.outerSquare)
        self.over_Piece()

        if self.hovering == True:
            pygame.draw.rect(screen, bgray2, self.innerSquare)
        font = pygame.font.Font(pygame.font.get_default_font(), 22)
        
        if self.png == False:
            text_surface = font.render(self.text, True, (255,255,255))
            text_rect = text_surface.get_rect(center=(self.locationX + self.size / 2, self.locationY + self.size / 2))
            screen.blit(text_surface, text_rect)
        else:
            self.image = pygame.image.load(self.text)
            self.image = pygame.transform.scale(self.image, (int(self.size-2 * self.Bezel), int(self.size - 2 * self.Bezel)))
            screen.blit(self.image, (self.locationX + self.Bezel, self.locationY + self.Bezel))
        
        

    
    def over_Piece(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.hovering = self.innerSquare.collidepoint(mouseX, mouseY)
        return self.hovering