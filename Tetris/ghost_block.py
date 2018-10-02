import pygame as pg
import game_functions as gf
from piece import Piece

class Ghost_Block(object):
    """Shows where piece will land"""
    def __init__(self, settings, screen, block):
        self.settings = settings
        self.screen = screen
        self.pieces = []
        for piece in block.pieces:
            self.pieces.append(Piece(settings, screen, settings.ghost_img, pg.Rect(piece.rect.left, piece.rect.top, settings.block_size, settings.block_size)))

    def draw_block(self):
        for piece in self.pieces:
            piece.draw_piece()

    def reset(self, settings, block, LoB):
        for i in range(4):
            self.pieces[i].rect.topleft = block.pieces[i].rect.topleft
        while not pg.sprite.groupcollide(self.pieces, LoB, False, False) and not gf.check_edges_bottom(settings, self):
            for piece in self.pieces:
                piece.rect.top += settings.block_size
        for piece in self.pieces:
            piece.rect.top -= settings.block_size