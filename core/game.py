import pygame as py

from core.input import handle_input
from core.physics import update
from rendering.drawing import draw
from entities.frame_limiter import FrameLimiter
from entities.camera import Camera
from entities.cube import Cube
from constants import WIDTH, HEIGHT, FPS, GRID

class Game:
    def __init__(self):
        py.init()
        self.running = True

        self.width = WIDTH
        self.height = HEIGHT

        self.cubes = [
            Cube(
                -GRID + x*2, -GRID + y*2, GRID,
                1, 1, 1
            )
            for x in range(GRID)
            for y in range(GRID)
        ]

        self.camera = Camera()
        self.frame_limiter = FrameLimiter()
        self.font = py.font.SysFont("Arial", 24)
        self.screen = py.display.set_mode((self.width, self.height), py.RESIZABLE)

    def run(self):
        while self.running:
            handle_input(self)
            update(self)
            draw(self)
            py.display.flip()
            self.frame_limiter.limit_fps(FPS)
            self.frame_limiter.tick()

        py.quit()