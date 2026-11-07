import pygame as py
import math

from core.input import handle_input
from core.physics import update
from rendering.drawing import draw
from entities.frame_limiter import FrameLimiter
from entities.camera import Camera
from entities.cube import Cube
from constants import WIDTH, HEIGHT, FOV, FPS, FONT_SIZE

class Game:
    def __init__(self):
        py.init()
        self.running = True

        self.paused = True
        self.debug = False
        self.mouse_locked = True
        py.event.set_grab(True)
        py.mouse.set_visible(False)
        
        self.width = WIDTH
        self.height = HEIGHT
        fov_rad = math.radians(FOV)
        self.fov_scale = self.width / (2 * math.tan(fov_rad / 2))

        self.cubes = [
            Cube(
                0, 0, 0,
                100, 10, 100
            ),
            Cube(
                0, 30, 0,
                50, 50, 50
            ),
            Cube(
                0, 57.5, 0,
                60, 5, 60
            ),
            Cube(
                26, 15, 0,
                1, 20, 10,
                yaw=20
            ),
        ]

        self.camera = Camera()
        self.frame_limiter = FrameLimiter()
        self.font = py.font.SysFont("Arial", FONT_SIZE)
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