import pygame as pg
from pygame.sprite import Sprite

class Piece(Sprite):
    """One piece in a block"""
    def __init__(self, settings, screen, image, rect):
        super().__init__()
        # Personal settings, screen atrributes
        self.settings = settings
        self.screen = screen

        # Image passed in depending on which block piece is apart of
        self.image = image
        self.rect = rect

    def draw_piece(self):
        """Blit piece to screen"""
        self.screen.blit(self.image, self.rect)