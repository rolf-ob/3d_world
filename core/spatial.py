def world_to_screen(game: object, world_x: int, world_y: int, world_z: int) -> tuple:
    screen_x = world_x - game.camera.x
    screen_y = world_y - game.camera.y

    return (screen_x, screen_y)