import pygame as py

from core.input import handle_input
from rendering.drawing import draw
from entities.frame_limiter import FrameLimiter
from constants import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        py.init()
        self.running = True

        self.width = WIDTH
        self.height = HEIGHT

        self.frame_limiter = FrameLimiter()
        self.screen = py.display.set_mode((self.width, self.height), py.RESIZABLE)

    def run(self):
        while self.running:
            handle_input(self)
            draw(self)
            py.display.flip()
            self.frame_limiter.limit_fps(FPS)
            self.frame_limiter.tick()

        py.quit()