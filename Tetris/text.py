import pygame as pg

class Text(object):
    """On-screen text"""
    def __init__(self, settings, screen, contents, x, y, size):
        self.screen = screen
        self.x, self.y = x, y
        self.text = contents
        self.text_color = settings.style_color
        self.background_color = settings.screen_color
        self.font = pg.font.SysFont(None, size)
        self.image = self.font.render(self.text, True, self.text_color, self.background_color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def prep_text(self, text):
        self.image = self.font.render(text, True, self.text_color, self.background_color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

    def draw_text(self):
        self.screen.blit(self.image, self.rect)

    def recolor(self, settings):
       self.text_color = settings.style_color
       self.background_color = settings.screen_color
       self.prep_text(self.text)