import pygame

from Animation import Animation

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, groups, img_path):
        super().__init__(groups)

        self.animation = Animation("ui/" + img_path)

        self.image = self.animation.animations[self.animation.status][self.animation.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.onClick = self.defaultFunc
        self.onHover = self.defaultOnHover
        self.onMouseLeft = self.defaultOnMouseLeft

        self.pos = pygame.math.Vector2(self.rect.center)

    def defaultOnHover(self):
        self.image = self.animation.animations[self.animation.status][1]

    def defaultOnMouseLeft(self):
        self.image = self.animation.animations[self.animation.status][0]

    def defaultFunc(self):
        return None

    def checkClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.onHover()
            if pygame.mouse.get_pressed()[0]:
                self.onClick()
        else:
            self.onMouseLeft()

    def update(self):
        self.checkClick()
