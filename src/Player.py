import pygame
from Entity import Entity

class Player(Entity):
    def __init__(self, pos, groups):
        super().__init__(pos, "resources/player/placeholder.png", 300, groups)


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, deltaTime):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed * deltaTime

    def update(self, deltaTime):
        self.input()
        self.move(deltaTime)
