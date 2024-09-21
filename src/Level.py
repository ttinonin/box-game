import pygame

from Player import Player
from Box import Box

class Level:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()

        self.gameState = gameState

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        self.player = Player((200, 300), [self.visible_sprites])
        Box((500, 500), [self.obstacle_sprites], self.player)
    
    def run(self, deltaTime):
        self.obstacle_sprites.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)

        self.obstacle_sprites.update(deltaTime)
        self.visible_sprites.update(deltaTime)
