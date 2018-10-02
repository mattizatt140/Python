from pygame.sprite import Group
import pygame as pg
from piece import Piece
from block import Block

class Square_Block(Block):
    """Square block"""
    def __init__(self, settings, screen):
        super().__init__(settings, screen)

        # Load image for each piece
        self.image = pg.image.load('images/square_piece.png')
        self.piece1_rect, self.piece2_rect, self.piece3_rect, self.piece4_rect = self.image.get_rect(),self.image.get_rect(),self.image.get_rect(),self.image.get_rect()
        self.piece1_rect.left, self.piece1_rect.top = settings.screen_width / 2 - settings.block_size, 0
        self.piece2_rect.left, self.piece2_rect.top = settings.screen_width / 2 - settings.block_size, settings.block_size
        self.piece3_rect.left, self.piece3_rect.top = settings.screen_width / 2, 0
        self.piece4_rect.left, self.piece4_rect.top = settings.screen_width / 2, settings.block_size
        
        self.pieces = [Piece(settings, screen, self.image, self.piece1_rect), Piece(settings, screen, self.image, self.piece2_rect),
                      Piece(settings, screen, self.image, self.piece3_rect), Piece(settings, screen, self.image, self.piece4_rect)]