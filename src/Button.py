import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, groups, img_path):
        super().__init__(groups)

        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.onClick = None

        self.pos = pygame.math.Vector2(self.rect.center)
