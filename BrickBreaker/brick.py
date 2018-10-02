import pygame as pg

class Brick(object):
    """description of class"""
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.width = settings.brick_width
        self.height = settings.brick_height
        self.color = settings.brick_color
        self.rect = pg.Rect(0, 0, self.width, self.height)

    def draw_brick(self):
        pg.draw.rect(self.screen, (255, 255, 255), self.rect)
        pg.draw.rect(self.screen, self.color, pg.Rect(self.rect.left + 5, self.rect.top + 5, self.rect.width - 10, self.rect.height - 10))