import pygame

from Animation import Animation

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_name: str, speed: int, groups, obstacles):
        super().__init__(groups)

        self.prev_pos = pygame.math.Vector2(pos)

        self.animation = Animation(sprite_name)

        self.image = self.animation.animations[self.animation.status][self.animation.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.mask = pygame.mask.from_surface(self.image)
        
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = speed
        
        self.obstacles = obstacles
        

    def colision(self, direction = 'horizontal'):
        if direction == 'horizontal':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving rightself
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving leftself
                        self.rect.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self, deltaTime: float):
        pass
