import pygame as py
import math

from core.input import handle_input
from core.physics import update
from rendering.drawing import draw
from entities.frame_limiter import FrameLimiter
from entities.camera import Camera
from entities.cube import Cube
from constants import WIDTH, HEIGHT, FOV, FPS, GRID

class Game:
    def __init__(self):
        py.init()
        self.running = True

        self.paused = True
        self.width = WIDTH
        self.height = HEIGHT
        fov_rad = math.radians(FOV)
        self.fov_scale = self.width / (2 * math.tan(fov_rad / 2))

        self.cubes = [
            Cube(
                (x - (GRID-1) / 2)*2, (y - (GRID-1) / 2)*2, GRID*2,
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
            if not self.paused:
                update(self)
            draw(self)
            py.display.flip()
            self.frame_limiter.limit_fps(FPS)
            self.frame_limiter.tick()

        py.quit()