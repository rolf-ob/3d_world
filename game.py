import pygame as py

from input import handle_input
from drawing import draw
from constants import WIDTH, HEIGHT

class Game:
    def __init__(self):
        py.init()
        self.running = True

        self.width = WIDTH
        self.height = HEIGHT

        self.screen = py.display.set_mode((self.width, self.height), py.RESIZABLE)

    def run(self):
        while self.running:
            handle_input(self)
            draw(self)
            py.display.flip()

        py.quit()