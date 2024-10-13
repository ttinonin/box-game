import pygame

from Level import Level
from Ending import Ending

class GameState:
    def __init__(self):
        self.currentScreen = "menu"
        self.screens = {}
        self.current_level = 1

        pygame.mixer.music.load("resources/sound/music.mp3")

        pygame.mixer.music.play(loops=-1)

    def initGame(self):
        self.screens["level"] = Level(self)

    def nextLevel(self):
        self.current_level += 1

        self.screens["level"] = Level(self)

    def createScreen(self, screenName, instance):
        self.screens[screenName] = instance

    def endGame(self):
        pygame.mixer.music.stop()

        self.screens["ending"] = Ending(self)

    def setScreen(self, screen):
        self.currentScreen = screen

    def getScreen(self):
        return self.currentScreen
