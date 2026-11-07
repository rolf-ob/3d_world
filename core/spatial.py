from constants import FOV

def world_to_screen(game: object, Xworld: int, Yworld: int, Zworld: int) -> tuple | None:
    Xc = Xworld - game.camera.x
    Yc = Yworld - game.camera.y
    Zc = Zworld - game.camera.z
    if Zc <= 0:
        return False
    
    Xproj = Xc / Zc
    Yproj = Yc / Zc

    Xscreen = Xproj * FOV + game.width  / 2
    Yscreen = Yproj * FOV + game.height / 2

    return (Xscreen, Yscreen)