import pygame
import math

class Label(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path):
        super().__init__(groups)

        self.image = pygame.image.load("resources/" + path).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(0, 1)
        self.speed = 100
        self.amplitude = 10
        self.original_y = self.pos.y

    def move(self):
        self.pos.y = self.original_y + self.amplitude * math.sin(pygame.time.get_ticks() * 0.002)

        self.rect.center = (self.pos.x, self.pos.y)

    def update(self, deltaTime = 1):
        pass