import pygame as py

def handle_input(game):
    for event in py.event.get():
        if event.type == py.QUIT:
            game.running = False

        elif event.type == py.VIDEORESIZE:
            game.width, game.height = event.size

        elif event.type == py.KEYDOWN:
            if event.key == py.K_w:
                print(game.width, game.height)