import pygame

bgray1 = (62, 62, 62)
bgray2 = (100, 100, 100)
bgray3 = (80, 80, 80)

class BasicButton:
    def __init__(self, locationX, locationY, sizeX, sizeY, text):
        self.hovering = False
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.locationX = locationX
        self.locationY = locationY
        self.text = text
        self.Bezel = sizeX/20
        self.outerButton = pygame.Rect(self.locationX, self.locationY, self.sizeX, self.sizeY)
        self.innerButton = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, sizeX - 2 * self.Bezel, sizeY - 2 * self.Bezel)

    def draw(self, screen):
        pygame.draw.rect(screen, bgray1, self.outerButton)
        self.over_button()
        if self.hovering == True:
            pygame.draw.rect(screen, bgray2, self.innerButton)
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.locationX + self.sizeX / 2, self.locationY + self.sizeY / 2))
        screen.blit(text_surface, text_rect)
    
    def over_button(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.hovering = self.innerButton.collidepoint(mouseX, mouseY)
        return self.hovering
    
class PieceSpawner:
    def __init__(self, locationX, locationY, size, text, type):
        self.hovering = False
        self.type = type
        self.locationX = locationX
        self.locationY = locationY
        self.size = size
        self.Bezel = size/20
        self.text = text
        self.outerButton = pygame.Rect(self.locationX, self.locationY, self.size, self.size)
        self.innerButton = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, size - 2 * self.Bezel, size - 2 * self.Bezel)
    
    def draw(self, screen):
        pygame.draw.rect(screen, bgray3, self.outerButton)
        self.over_button()
        if self.hovering == True:
            pygame.draw.rect(screen, bgray2, self.innerButton)
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text_surface = font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.locationX + self.size / 2, self.locationY + self.size / 2))
        screen.blit(text_surface, text_rect)

    def over_button(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.hovering = self.innerButton.collidepoint(mouseX, mouseY)
        return self.hovering
        