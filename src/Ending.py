import pygame

from Button import Button
from Label import Label
from Level import Level

class Ending:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()
        self.gameState = gameState

        self.sound = pygame.mixer.Sound("resources/sound/ending.mp3")

        self.bg_image = pygame.image.load("resources/ui/ending_png.png").convert()

        pygame.mixer.Sound.play(self.sound)

    def run(self, deltaTime):
        self.display_surface.blit(self.bg_image, (0,0))