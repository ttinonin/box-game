import pygame

from Player import Player
from Box import Box
from Label import Label
from Tile import Tile
from Text import Text
from Door import Door

from utils import import_csv, import_folder

class Level:
    def __init__(self, gameState):
        self.display_surface = pygame.display.get_surface()

        self.gameState = gameState

        self.background = pygame.image.load("resources/map00.png").convert()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.level_label = Label((130, 685), [self.visible_sprites], "ui/level.png")

        self.create_map()

    def blit_hud(self):
        text = Text(self.gameState.current_level, (250, 660))

        self.display_surface.fill("black", pygame.Rect(0,660,1280,120))

        self.display_surface.blit(text.text, text.rect.center)
    
    def create_map(self):
        try:
            layout = {
                'floor': import_csv(f"levels/{self.gameState.current_level}/floor.csv"),
                'walls': import_csv(f"levels/{self.gameState.current_level}/walls.csv"),
                "boxes": import_csv(f"levels/{self.gameState.current_level}/boxes.csv"),
                "door": import_csv(f"levels/{self.gameState.current_level}/door.csv")
            }

            graphivs = {
                'corners': import_folder("resources/tiles/corners")
            }

            for style, layout in layout.items():
                for row_index, row in enumerate(layout):
                    for col_index, col in enumerate(row):
                        if col == "-1":
                            continue
                        
                        x = col_index * 48
                        y = row_index * 48

                        if style == "floor":
                            Tile((x,y), [self.visible_sprites], "floor", pygame.image.load("resources/tiles/floor.png").convert())
                        if style == "walls":
                            if col == "0":
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "walls", pygame.image.load("resources/tiles/wall-48.png").convert())
                            else:
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "corner", graphivs["corners"][int(col)])
                        if style == "boxes":
                            Box((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites)
                        if style == "door":
                            self.door = Door([self.visible_sprites, self.obstacle_sprites], (x, y))

            self.player = Player((200, 400), [self.visible_sprites], self.obstacle_sprites, self.door, self.gameState)

        except FileNotFoundError:
            # End of avaliable levels
            self.gameState.setScreen("menu")

    def run(self, deltaTime):
        self.blit_hud()

        self.visible_sprites.draw(self.display_surface)

        self.visible_sprites.update(deltaTime)
