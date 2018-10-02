import pygame as pg
from piece import Piece
from block import Block

class T_Block(Block):
    """Long block"""
    def __init__(self, settings, screen):
        super().__init__(settings, screen)

        # Load image for each piece
        self.image = pg.image.load('images/t_piece.png')
        self.piece1_rect, self.piece2_rect, self.piece3_rect, self.piece4_rect = self.image.get_rect(),self.image.get_rect(),self.image.get_rect(),self.image.get_rect()
        self.piece1_rect.left, self.piece1_rect.top = settings.screen_width / 2, 0
        self.piece2_rect.left, self.piece2_rect.top = settings.screen_width / 2, settings.block_size
        self.piece3_rect.left, self.piece3_rect.top = settings.screen_width / 2 - settings.block_size, settings.block_size
        self.piece4_rect.left, self.piece4_rect.top = settings.screen_width / 2 + settings.block_size, settings.block_size

        self.pieces = [Piece(settings, screen, self.image, self.piece1_rect), Piece(settings, screen, self.image, self.piece2_rect),
                      Piece(settings, screen, self.image, self.piece3_rect), Piece(settings, screen, self.image, self.piece4_rect)]
    
    def rotate_right(self):
        if self.permutation == 0:
            self.pieces[2].rect.topleft = self.pieces[0].rect.topleft
            self.pieces[0].rect.topleft = self.pieces[3].rect.topleft
            self.pieces[3].rect.topleft = self.pieces[1].rect.topright

        elif self.permutation == 1:
            self.pieces[2].rect.topleft = self.pieces[1].rect.bottomleft

        elif self.permutation == 2:
            self.pieces[0].rect.topright = self.pieces[1].rect.topleft

        elif self.permutation == 3:
            self.pieces[3].rect.bottomleft = self.pieces[1].rect.topleft

    def rotate_left(self):
        if self.permutation == 0:
            self.pieces[2].rect.topright = self.pieces[1].rect.topleft

        elif self.permutation == 1:
            self.pieces[0].rect.bottomleft = self.pieces[1].rect.topleft

        elif self.permutation == 2:
            self.pieces[3].rect.topleft = self.pieces[1].rect.topright

        elif self.permutation == 3:
            self.pieces[3].rect.topleft = self.pieces[0].rect.topleft
            self.pieces[0].rect.topleft = self.pieces[2].rect.topleft
            self.pieces[2].rect.topleft = self.pieces[1].rect.bottomleft