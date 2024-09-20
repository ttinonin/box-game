import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Game")

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime = self.clock.tick() / 1000
