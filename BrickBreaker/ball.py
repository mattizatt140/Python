import pygame as pg
import random

class Ball(object):
    """A ball"""
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.vel = [4, 5]
        self.width = settings.ball_width
        self.color = settings.ball_color
        self.rect = pg.Rect(settings.screen_width / 2 - self.width / 2, settings.screen_height / 2 - self.width / 2, self.width, self.width)

    def draw_ball(self):
        pg.draw.circle(self.screen, self.color, self.rect.center, self.width)