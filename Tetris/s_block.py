import pygame as pg
from piece import Piece
from block import Block

class S_Block(Block):
    """description of class"""
    def __init__(self, settings, screen):
        super().__init__(settings, screen)

        # Load image for each piece
        self.image = pg.image.load('images/s_piece.png')
        self.piece1_rect, self.piece2_rect, self.piece3_rect, self.piece4_rect = self.image.get_rect(), self.image.get_rect(), self.image.get_rect(), self.image.get_rect()
        self.piece1_rect.left, self.piece1_rect.top = settings.screen_width / 2 + settings.block_size, 0
        self.piece2_rect.left, self.piece2_rect.top = settings.screen_width / 2, 0
        self.piece3_rect.left, self.piece3_rect.top = settings.screen_width / 2, settings.block_size
        self.piece4_rect.left, self.piece4_rect.top = settings.screen_width / 2 - settings.block_size, settings.block_size

        self.pieces = [Piece(settings, screen, self.image, self.piece1_rect), Piece(settings, screen, self.image, self.piece2_rect),
                      Piece(settings, screen, self.image, self.piece3_rect), Piece(settings, screen, self.image, self.piece4_rect)]

    def rotate_right(self):
        if self.permutation == 0:
            self.pieces[1].rect.bottom = self.pieces[2].rect.top
            self.pieces[0].rect.left = self.pieces[1].rect.right
        elif self.permutation == 1:
            self.pieces[3].rect.left = self.pieces[2].rect.right
            self.pieces[0].rect.top = self.pieces[2].rect.bottom
        elif self.permutation == 2:
            self.pieces[1].rect.top = self.pieces[2].rect.bottom
            self.pieces[0].rect.right = self.pieces[1].rect.left
        elif self.permutation == 3:
            self.pieces[3].rect.right = self.pieces[2].rect.left
            self.pieces[0].rect.bottom = self.pieces[3].rect.top

    def rotate_left(self):
        if self.permutation == 0:
            self.pieces[0].rect.top = self.pieces[1].rect.top
            self.pieces[3].rect.right = self.pieces[2].rect.left
        elif self.permutation == 1:
            self.pieces[0].rect.left = self.pieces[3].rect.left
            self.pieces[1].rect.bottom = self.pieces[2].rect.top
        elif self.permutation == 2:
            self.pieces[0].rect.top = self.pieces[3].rect.bottom
            self.pieces[3].rect.left = self.pieces[2].rect.right
        elif self.permutation == 3:
            self.pieces[0].rect.left = self.pieces[3].rect.left
            self.pieces[1].rect.top = self.pieces[2].rect.bottom