def on_ground(game):
    for cube in game.cubes:
        on_top = cube.y + cube.height/2 - 10 <= game.camera.y - 20 <= cube.y + cube.height/2
        within_bounds = (
            cube.x - cube.width/2 - 10 < game.camera.x < cube.x + cube.width/2 + 10 and
            cube.z - cube.depth/2 - 10 < game.camera.z < cube.z + cube.depth/2 + 10
        )

        if on_top and within_bounds:
            return cube.y + cube.height/2

    return False

def jump(game):
    if on_ground(game):
        game.camera.y += 0.1
        game.y_vel = 1

def update(game):
    ground = on_ground(game)

    if not ground:
        game.y_vel = max(-10, game.y_vel - 0.01)
        game.camera.y = max(-100, game.camera.y + game.y_vel)
    else:
        game.y_vel = 0
        game.camera.y = ground + 20