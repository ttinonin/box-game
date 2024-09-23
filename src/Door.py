import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.image.load("resources/tiles/door.png").convert()

        self.rect = self.image.get_rect(topleft = pos)