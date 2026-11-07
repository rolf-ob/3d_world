def update(game):
    for cube in game.cubes:
        cube.roll += 1
        cube.pitch += 1
        cube.yaw += 1
        cube.recompute()