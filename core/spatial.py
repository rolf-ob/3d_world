from constants import FOV

def world_to_screen(game: object, world_x: int, world_y: int, world_z: int) -> tuple | None:
    Xc = world_x - game.camera.x
    Yc = world_y - game.camera.y
    Zc = world_z - game.camera.z
    if Zc <= 0:
        return False
    
    proj_x = Xc / Zc
    proj_y = Yc / Zc
    screen_x = proj_x * FOV + game.width  / 2
    screen_y = proj_y * FOV + game.height / 2
    return (screen_x, screen_y)