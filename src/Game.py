import pygame
import sys

from Level import Level
from Menu import Menu
from GameState import GameState

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720), vsync=0)
        pygame.display.set_caption("Game")

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.gameState = GameState()
        self.menu = Menu(self.gameState)
        self.level = Level(self.gameState)

        self.screens = {'menu': self.menu, 'level': self.level}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime = self.clock.tick(self.FPS) / 1000

            self.screen.fill('white')

            self.screens[self.gameState.getScreen()].run(deltaTime)

            pygame.display.update()
