import pygame as py
import math

from constants import FOV, CAMERA_MOVEMENT_SPEED, CAMERA_ROTATION_SPEED

def update_camera(game, keys):
    yaw = math.radians(game.camera.yaw)
    cos_y, sin_y = math.cos(yaw), math.sin(yaw)

    if keys[py.K_w]:
        game.camera.z += cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.x += sin_y * CAMERA_MOVEMENT_SPEED
    if keys[py.K_a]:
        game.camera.x -= cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.z += sin_y * CAMERA_MOVEMENT_SPEED
    if keys[py.K_s]:
        game.camera.z -= cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.x -= sin_y * CAMERA_MOVEMENT_SPEED
    if keys[py.K_d]:
        game.camera.x += cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.z -= sin_y * CAMERA_MOVEMENT_SPEED
    
    if keys[py.K_LSHIFT]:
        game.camera.y += CAMERA_MOVEMENT_SPEED
    if keys[py.K_SPACE]:
        game.camera.y -= CAMERA_MOVEMENT_SPEED
    print(game.camera.pitch)
    if keys[py.K_i]:
        game.camera.pitch = max(-90, game.camera.pitch - CAMERA_ROTATION_SPEED)
    if keys[py.K_j]:
        game.camera.yaw -= CAMERA_ROTATION_SPEED
    if keys[py.K_k]:
        game.camera.pitch = min(90, game.camera.pitch + CAMERA_ROTATION_SPEED)
    if keys[py.K_l]:
        game.camera.yaw += CAMERA_ROTATION_SPEED

def handle_input(game: object) -> None:
    keys = py.key.get_pressed()

    update_camera(game, keys)

    for event in py.event.get():
        if event.type == py.QUIT:
            game.running = False

        elif event.type == py.VIDEORESIZE:
            game.width, game.height = event.size
            fov_rad = math.radians(FOV)
            game.fov_scale = game.width / (2 * math.tan(fov_rad / 2))

        elif event.type == py.KEYDOWN:
            if event.key == py.K_p:
                game.paused = not game.paused

            elif event.key == py.K_ESCAPE:
                game.running = False