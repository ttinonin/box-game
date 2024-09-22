import pygame
import sys

from Level import Level
from Menu import Menu
from GameState import GameState

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720), vsync=0)
        pygame.display.set_caption("Daniel's Path")

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.gameState = GameState()
        self.menu = Menu(self.gameState)
        self.level = Level(self.gameState)

        self.screens = {'menu': self.menu, 'level': self.level, 'quit': self.quit}

    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.quit()

            deltaTime = self.clock.tick(self.FPS) / 1000

            self.screen.fill('black')

            if self.gameState.getScreen() == "quit":
                self.quit()

            self.screens[self.gameState.getScreen()].run(deltaTime)

            pygame.display.update()
