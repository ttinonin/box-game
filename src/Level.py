import pygame

from Player import Player
from Box import Box

class Level:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()

        self.gameState = gameState

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        self.player = Player((200, 300), [self.visible_sprites], self.boxes)
        Box((500, 500), [self.visible_sprites, self.boxes], self.boxes)

    def run(self, deltaTime):
        self.visible_sprites.draw(self.display_surface)

        self.visible_sprites.update(deltaTime)
