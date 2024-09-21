import pygame

from Entity import Entity

class Box(Entity):
    def __init__(self, pos, groups, player):
        super().__init__(pos, "resources/wood-box.png", 400, groups)

        self.player = player

    def colideWithPLayer(self):
        if self.rect.colliderect(self.player.rect):
            self.direction = self.player.direction
        else:
            self.direction = pygame.math.Vector2(0, 0)

    def move(self, deltaTime):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed * deltaTime

    def update(self, deltaTime):
        self.colideWithPLayer()
        self.move(deltaTime)
