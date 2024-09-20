import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, img_path: str, speed: int, groups):
        super().__init__(groups)

        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect(center = pos)

        self.mask = pygame.mask.from_surface(self.image)
        
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = speed

    def update(self, deltaTime: float):
        pass
