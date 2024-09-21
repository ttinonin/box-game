import pygame
from Entity import Entity

from Box import Box
from WalkingBox import WalkingBox

class Player(Entity):
    def __init__(self, pos, groups, obstacles):
        super().__init__(pos, "resources/player/placeholder.png", 300, groups, obstacles)

     #   self.rect = self.rect.inflate(0, -10)
        self.isHoldingBox = False

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

        self.rect.x += self.direction.x * self.speed * deltaTime
        self.colision('horizontal')
        self.rect.y += self.direction.y * self.speed * deltaTime
        self.colision('vertical')
    
    def colision(self, direction = 'horizontal'):
        if direction == 'horizontal':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if isinstance(sprite, Box):
                        sprite.direction.x = self.direction.x
                    if isinstance(sprite, WalkingBox):
                        sprite.direction.x = self.direction.x

                    if self.direction.x > 0: # moving rightself
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving leftself
                        self.rect.left = sprite.rect.right
                else:
                    if isinstance(sprite, Box):
                       sprite.direction.x = 0

        if direction == 'vertical':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if isinstance(sprite, Box):
                        sprite.direction.y = self.direction.y
                    if isinstance(sprite, WalkingBox):
                        sprite.direction.y = self.direction.y

                    if self.direction.y > 0: # moving rightself
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving leftself
                        self.rect.top = sprite.rect.bottom
                else:
                    if isinstance(sprite, Box):
                        sprite.direction.y = 0

    def update(self, deltaTime):
        self.input()
        self.move(deltaTime)
