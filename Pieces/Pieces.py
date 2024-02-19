import pygame
import sys
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground, globalwidth

width = globalwidth

flag_image = pygame.image.load("Stratego\\Pieces\\Flag.png")
bomb_image = pygame.image.load("Stratego\\Pieces\\Bomb.png")
fullOutline_image = pygame.image.load("Stratego\\Pieces\\FullOutline.png")
topOutline_image = pygame.image.load("Stratego\\Pieces\\TopOutline.png")
leftOutline_image = pygame.image.load("Stratego\\Pieces\\LeftOutline.png")
rightOutline_image = pygame.image.load("Stratego\\Pieces\\RightOutline.png")
bottomOutline_image = pygame.image.load("Stratego\\Pieces\\BottomOutline.png")

fullOutline_image = pygame.transform.scale(fullOutline_image, (width/11 + 2, width/11 + 2))
topOutline_image = pygame.transform.scale(topOutline_image, (width/11 + 2, width/11 + 2))
leftOutline_image = pygame.transform.scale(leftOutline_image, (width/11 + 2, width/11 + 2))
rightOutline_image = pygame.transform.scale(rightOutline_image, (width/11 + 2, width/11 + 2))
bottomOutline_image = pygame.transform.scale(bottomOutline_image, (width/11 + 2, width/11 + 2))

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

        

        #Creation of bomb and text surfaces----------------------------Creation of bomb and text surfaces
        if self.type < 10:
            self.text = str(self.type)
            self.png = False
        elif self.type == 12:
            self.image = flag_image
        elif self.type == 11:
            self.text = "S"
            self.png = False
        else:
            self.image = bomb_image
        if self.png == False:
            font = pygame.font.Font(pygame.font.get_default_font(), 22)
            self.text_surface = font.render(self.text, True, (255,255,255))
        else:
            self.image = pygame.transform.scale(self.image, (int(self.size-2 * self.Bezel), int(self.size - 2 * self.Bezel)))
        

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
        if self.png == False:
            self.text_rect = self.text_surface.get_rect(center=(self.locationX + self.size / 2, self.locationY + self.size / 2))
            screen.blit(self.text_surface, self.text_rect)
        else:
            screen.blit(self.image, (self.locationX + self.Bezel, self.locationY + self.Bezel))
        

    
    def over_Piece(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.hovering = self.innerSquare.collidepoint(mouseX, mouseY)
        return self.hovering
    
def moveLogic(type, xIndex, yIndex, potentialMoves, grid):
    potentialMoves[xIndex][yIndex][0] = 1
    potentialMoves[xIndex][yIndex][1] = "Center"
    print(potentialMoves[xIndex][yIndex])
    print(potentialMoves[xIndex][yIndex-1])
    if xIndex > 0 and grid[xIndex -1][yIndex] < 1:
        potentialMoves[xIndex - 1][yIndex][0] = 1
        if grid[xIndex][yIndex] != 9:
            potentialMoves[xIndex - 1][yIndex][1] = "Left"
        else:
            while checker < 10:
                checker = xIndex
                print (checker)
                if xIndex > 0 and grid[checker][yIndex] < 1:
                    checker -= 1
                else: 
                    break
    if xIndex < 9 and grid[xIndex +1][yIndex] < 1:
        potentialMoves[xIndex + 1][yIndex][0] = 1
        if grid[xIndex][yIndex] != 9:
            potentialMoves[xIndex + 1][yIndex][1] = "Right"
    if  yIndex > 1 and grid[xIndex][yIndex-1] < 1:
        potentialMoves[xIndex][yIndex - 1][0] = 1
        if grid[xIndex][yIndex] != 9:
            potentialMoves[xIndex][yIndex - 1][1] = "Up"
    if yIndex < 9 and grid[xIndex][yIndex+1] < 1:
        potentialMoves[xIndex][yIndex + 1][0] = 1
        if grid[xIndex][yIndex] != 9:
            potentialMoves[xIndex][yIndex + 1][1] = "Down"
    return potentialMoves

def drawPotential(screen, potentialMoves):
    for i in range(0, 10):
        for j in range(0, 10):
            locationX = i * width / 10
            locationY = j * width / 10 + width / 10
            if potentialMoves[i][j][1] == "Center":
                screen.blit(fullOutline_image, (locationX + 6, locationY + 3))
            elif potentialMoves[i][j][1] == "Up":
                screen.blit(topOutline_image, (locationX + 6, locationY + 3))
            elif potentialMoves[i][j][1] == "Left":
                screen.blit(leftOutline_image, (locationX + 6, locationY + 3))
            elif potentialMoves[i][j][1] == "Right":
                screen.blit(rightOutline_image, (locationX + 6, locationY + 3))
            elif potentialMoves[i][j][1] == "Down":
                screen.blit(bottomOutline_image, (locationX + 6, locationY + 3))