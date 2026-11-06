import pygame as py

from constants import CAMERA_SPEED

def update_camera(game, keys):
    if keys[py.K_w]:
        game.camera.y -= CAMERA_SPEED
    if keys[py.K_a]:
        game.camera.x -= CAMERA_SPEED
    if keys[py.K_s]:
        game.camera.y += CAMERA_SPEED
    if keys[py.K_d]:
        game.camera.x += CAMERA_SPEED
    if keys[py.K_q]:
        game.camera.z += CAMERA_SPEED
    if keys[py.K_e]:
        game.camera.z -= CAMERA_SPEED

def handle_input(game: object) -> None:
    keys = py.key.get_pressed()

    update_camera(game, keys)

    for event in py.event.get():
        if event.type == py.QUIT:
            game.running = False

        elif event.type == py.VIDEORESIZE:
            game.width, game.height = event.size

        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                game.running = False