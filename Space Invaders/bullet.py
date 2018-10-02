import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to handle bullet sprites"""

    def __init__(self, ai_settings, screen):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)