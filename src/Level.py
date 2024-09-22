import pygame

from Player import Player
from Box import Box
from WalkingBox import WalkingBox
from Label import Label

class Level:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()

        self.gameState = gameState

        self.background = pygame.image.load("resources/map-test.png").convert()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.level_label = Label((130, 685), [self.visible_sprites], "ui/level.png")

        self.create_map()

    def blit_hud(self):
        self.display_surface.fill("black", pygame.Rect(0,660,1280,120))
    
    def create_map(self):
        self.player = Player((200, 300), [self.visible_sprites], self.obstacle_sprites)
        Box((500, 500), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        Box((300, 500), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        Box((500, 700), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        Box((600, 500), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
        WalkingBox((300, 300), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)

    def run(self, deltaTime):
        self.display_surface.blit(self.background, (0,0))

        self.blit_hud()

        self.visible_sprites.draw(self.display_surface)

        self.visible_sprites.update(deltaTime)
