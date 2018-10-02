import pygame as pg
from pygame.sprite import Sprite

class Block(Sprite):
    """Block superclass"""
    def __init__(self, settings, screen):
        super().__init__()

        # Personal settings, screen for piece associated objects
        self.settings = settings
        self.screen = screen

        # Track where in rotation piece is
        self.permutation = 0
        self.init_dynamic()

    def init_dynamic(self):
        # Allow for holding key to keep constant movement
        self.moving_left, self.moving_right = False, False

        # Create delay between first move-left/rigth and settings moving_left/moving_right to true
        self.moving_left_counter, self.moving_right_counter = 0, 0
        self.moving_left_timer, self.moving_right_timer = False, False

        # Allow delay between piece/ground contact and next-piece generation
        self.set_down_counter, self.set_down_active = 0, False

    def draw_block(self):
        """Draw block"""
        # Call draw method of each piece
        for piece in self.pieces:
            piece.draw_piece()

    def get_top(self):
        top = 600
        for piece in self.pieces:
            if piece.rect.top < top:
                top = piece.rect.top
        return top

    def get_left(self):
        left = 600
        for piece in self.pieces:
            if piece.rect.left < left:
                left = piece.rect.left
        return left