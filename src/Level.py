import pygame

from Player import Player
from Box import Box
from WalkingBox import WalkingBox

class Level:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()

        self.gameState = gameState

        self.background = pygame.image.load("resources/map-test.png").convert()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        self.player = Player((200, 300), [self.visible_sprites], self.obstacle_sprites)
        Box((500, 500), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        Box((300, 500), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        Box((500, 700), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        Box((600, 500), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        WalkingBox((300, 300), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)

    def run(self, deltaTime):
        self.display_surface.blit(self.background, (0,0))

        self.visible_sprites.draw(self.display_surface)

        self.visible_sprites.update(deltaTime)
