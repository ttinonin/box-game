import os
import pygame
import csv

def import_csv(path):
    terrain_map = []
    with open("resources/ui/csv/" + path) as level_map:
        layout = csv.reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(row)
    return terrain_map

def import_folder(path):
    surface_list = []

    for _, _, img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list