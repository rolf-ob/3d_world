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
        for i in range(4):
            connect_corners(game, screen, cube.corners[i], cube.corners[[1, 2, 3, 0][i]])

        for i in range(4, 8):
            connect_corners(game, screen, cube.corners[i], cube.corners[[5, 6, 7, 4][i-4]])

        for i, j in zip(range(4), range(4, 8)):
            connect_corners(game, screen, cube.corners[i], cube.corners[j])

    fps = f"FPS: {round(game.frame_limiter.get_fps())}"
    text_surface = game.font.render(fps, False, (0,)*3)
    screen.blit(text_surface, (20, 20))