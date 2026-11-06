import pygame as py

from core.spatial import world_to_screen

def draw(game: object) -> None:
    screen = game.screen
    screen.fill((255,)*3)

    for cube in game.cubes:
        for corner in cube.corners:
            x, y = world_to_screen(game, corner[0], corner[1], corner[2])
            py.draw.rect(screen, (0,)*3, (x, y, 2, 2))