import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, groups, img_path):
        super().__init__(groups)

        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.onClick = self.defaultFunc
        self.onHover = self.defaultFunc

        self.pos = pygame.math.Vector2(self.rect.center)

    def defaultFunc(self):
        return None

    def checkClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.onHover()
            if pygame.mouse.get_pressed()[0]:
                self.onClick()

    def update(self):
        self.checkClick()
