import pygame as pg

class Settings(object):
    """Container of game settings"""
    def __init__(self):
        # Width of game window
        self.screen_height = 600
        self.game_screen_width = 450

        # Width of full window
        self.screen_width = 600
        self.block_size = 30

        # Game color
        self.screen_color = (0, 0, 0)
        self.style_color = (255, 255, 255)
        self.input_inactive_color = (100, 100, 100)
        self.input_active_color = (255, 255, 255)

        self.ghost_img = pg.image.load("images/ghost_piece.png")
        self.title_img = pg.image.load("images/tetris-logo_black.png")
        self.block_img = [pg.image.load('images/long_block.png'), pg.image.load('images/square_block.png'), pg.image.load('images/z_block_black.png'), pg.image.load('images/s_block_black.png'),
                          pg.image.load('images/left_L_block_black.png'),  pg.image.load('images/right_L_block_black.png'), pg.image.load('images/t_block_black.png')]