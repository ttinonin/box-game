import pygame

from utils import import_folder

class Animation:
    def __init__(self, entity: str):
        self.animations = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            'right_idle': [],
            'left_idle': [],
            'up_idle': [],
            'down_idle': []
        }

        self.entity = entity

        self.status = "down_idle"
        self.frame_index = 0

        self.import_assets()

    def import_assets(self):
        for animation in self.animations.keys():
            full_path = 'resources/' + self.entity + '/' + animation

            self.animations[animation] = import_folder(full_path)
