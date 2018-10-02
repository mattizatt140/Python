import pygame
from pygame.sprite import Sprite

class TestRect(Sprite):
    """For testing rect collisions"""
    def __init__(self, rect_left, rect_top):

        # Create test object's rect
        self.rect = pygame.Rect(rect_left, rect_top, 25, 25)