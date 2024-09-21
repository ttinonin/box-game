import pygame

class GameState:
    def __init__(self):
        self.currentScreen = "menu"

    def setScreen(self, screen):
        self.currentScreen = screen

    def getScreen(self):
        return self.currentScreen
