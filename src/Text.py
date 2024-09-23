import pygame

class Text:
    def __init__(self, text, pos):
        self.font = pygame.font.Font('resources/font.ttf', 45)

        self.text = self.font.render(str(text), True, (255, 255, 255))

        self.rect = self.text.get_rect(center = pos)
