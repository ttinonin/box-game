import pygame

class GameState:
    def __init__(self):
        self.currentScreen = "menu"
        self.screens = {}
        self.current_level = 1

    def createScreen(self, screenName, instance):
        self.screens[screenName] = instance

    def setScreen(self, screen):
        self.currentScreen = screen

    def getScreen(self):
        return self.currentScreen
