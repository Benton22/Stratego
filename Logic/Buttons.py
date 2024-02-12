import pygame

bgray1 = (62, 62, 62)
bgray2 = (100, 100, 100)


class BasicButton:
    def __init__(self, locationX, locationY, sizeX, sizeY, text):
        self.hovering = False
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.locationX = locationX
        self.locationY = locationY
        self.text = text
        self.button = pygame.display.get_surface()
        self.Bezel = sizeX/20
        self.outerButton = pygame.Rect(self.locationX, self.locationY, self.sizeX, self.sizeY)
        self.innerButton = pygame.Rect(self.locationX + self.Bezel, self.locationY + self.Bezel, sizeX - 2 * self.Bezel, sizeY - 2 * self.Bezel)

    def draw(self):
        pygame.draw.rect(self.button, bgray1, self.outerButton)
        self.over_button()
        if self.hovering == True:
            pygame.draw.rect(self.button, bgray2, self.innerButton)
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.locationX + self.sizeX / 2, self.locationY + self.sizeY / 2))
        self.button.blit(text_surface, text_rect)
    
    def over_button(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        hovering = self.innerButton.collidepoint(mouseX, mouseY)
        return hovering