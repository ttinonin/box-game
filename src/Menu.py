import pygame

from Button import Button
from Label import Label

class Menu:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()
        self.gameState = gameState

        self.bg_image = pygame.image.load("resources/ui/menu-bg.png").convert()

        self.visible_sprites = pygame.sprite.Group()

        self.menu_label = Label((640, 200), [self.visible_sprites], "ui/menu-logo.png")

        self.start_btn = Button((400, 500), [self.visible_sprites], "start")
        self.start_btn.onClick = self.startGame

        self.start_btn = Button((630, 500), [self.visible_sprites], "quit")
        self.start_btn.onClick = self.quitGame

    def startGame(self):
        self.gameState.setScreen("level") 

    def quitGame(self):
        self.gameState.setScreen("quit")

    def run(self, deltaTime):
        self.display_surface.blit(self.bg_image, (0,0))

        self.menu_label.move()

        self.visible_sprites.draw(self.display_surface)

        self.visible_sprites.update()
