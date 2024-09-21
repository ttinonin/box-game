import pygame

from Button import Button

class Menu:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()
        self.gameState = gameState

        self.buttons = pygame.sprite.Group()

        self.start_btn = Button((500, 500), [self.buttons], "resources/ui/start-btn.png")
        self.start_btn.onClick(self.startGame)

    def startGame(self):
        print("xd")

    def run(self, deltaTime):
        self.buttons.draw(self.display_surface)

        self.buttons.update()
