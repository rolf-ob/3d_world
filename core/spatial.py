import math

def world_to_screen(game: object, Xworld: int, Yworld: int, Zworld: int) -> tuple | None:
    dx = Xworld - game.camera.x
    dy = Yworld - game.camera.y
    dz = Zworld - game.camera.z

    yaw = math.radians(game.camera.yaw)
    pitch = math.radians(game.camera.pitch)

    cos_y, sin_y = math.cos(yaw), math.sin(yaw)
    x1 = dx * cos_y - dz * sin_y
    z1 = dx * sin_y + dz * cos_y
    y1 = dy

    cos_p, sin_p = math.cos(pitch), math.sin(pitch)
    y2 = y1 * cos_p - z1 * sin_p
    z2 = y1 * sin_p + z1 * cos_p
    x2 = x1
    
    if z2 <= 0:
        return False
    
    Xproj = x2 / z2
    Yproj = y2 / z2

    Xscreen = Xproj * game.fov_scale + game.width  / 2
    Yscreen = Yproj * game.fov_scale + game.height / 2

    return (Xscreen, Yscreen)