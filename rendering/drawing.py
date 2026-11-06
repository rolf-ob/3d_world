import pygame as py

from core.spatial import world_to_screen

def connect_corners(game, screen, corner1, corner2):
    point1 = world_to_screen(game, corner1[0], corner1[1], corner1[2])
    point2 = world_to_screen(game, corner2[0], corner2[1], corner2[2])
    if point1 and point2:
        py.draw.line(screen, (0,)*3, point1, point2)

def draw(game: object) -> None:
    screen = game.screen
    screen.fill((255,)*3)

    for cube in game.cubes:
        connect_corners(game, screen, cube.corners[0], cube.corners[1])
        connect_corners(game, screen, cube.corners[1], cube.corners[2])
        connect_corners(game, screen, cube.corners[2], cube.corners[3])
        connect_corners(game, screen, cube.corners[3], cube.corners[0])
        
        connect_corners(game, screen, cube.corners[4], cube.corners[5])
        connect_corners(game, screen, cube.corners[5], cube.corners[6])
        connect_corners(game, screen, cube.corners[6], cube.corners[7])
        connect_corners(game, screen, cube.corners[7], cube.corners[4])
        
        connect_corners(game, screen, cube.corners[0], cube.corners[4])
        connect_corners(game, screen, cube.corners[1], cube.corners[5])
        connect_corners(game, screen, cube.corners[2], cube.corners[6])
        connect_corners(game, screen, cube.corners[3], cube.corners[7])