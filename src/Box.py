import pygame

from Entity import Entity

class Box(Entity):
    def __init__(self, pos, groups, obstacles):
        super().__init__(pos, "box", 300, groups, obstacles)

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
                if sprite == self:
                    continue
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving rightself
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving leftself
                        self.rect.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacles:
                if sprite == self:
                    continue
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self, deltaTime):
        self.move(deltaTime)
