import pygame as pg

class Paddle(object):
    """Player Paddle!"""
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.width = settings.paddle_width
        self.height = settings.paddle_height
        self.speed = settings.paddle_speed
        self.color = settings.paddle_color
        self.dir = settings.paddle_dir

        self.rect = pg.Rect((settings.screen_width / 2) - (self.width / 2), (settings.screen_height - self.height), self.width, self.height)

    def draw_paddle(self):
        pg.draw.rect(self.screen, self.color, self.rect)
