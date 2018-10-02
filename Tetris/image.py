import pygame as pg

class Image(object):
    """An image"""
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw_image(self):
        self.screen.blit(self.image, self.rect)