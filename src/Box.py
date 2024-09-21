import pygame

from Entity import Entity

class Box(Entity):
    def __init__(self, pos, groups, boxes):
        super().__init__(pos, "resources/wood-box.png", 400, groups)

        self.boxes = boxes

    def colision(self):
        for sprite in self.boxes:
            if sprite.rect.colliderect(self.rect):
                print(sprite)

    def move(self, deltaTime):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed * deltaTime

    def update(self, deltaTime):
        self.colision()
        self.move(deltaTime)
