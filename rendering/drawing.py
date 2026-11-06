import pygame as py

def draw(game: object) -> None:
    screen = game.screen
    screen.fill((255,)*3)

    py.draw.rect(screen, (0,)*3, (game.width / 2, game.height / 2, 20, 20))