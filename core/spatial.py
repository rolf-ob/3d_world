def world_to_screen(game: object, world_x: int, world_y: int, world_z: int) -> tuple:
    screen_x = world_x - game.camera.x
    screen_y = world_y - game.camera.y
    screen_z = world_z - game.camera.z

    return screen_x, screen_y, screen_z

def screen_to_world(game: object, screen_x: int, screen_y: int, screen_z: int) -> tuple:
    world_x = screen_x
    world_y = screen_y
    world_z = screen_z

    return world_x, world_y, world_z