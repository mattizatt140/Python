import pygame
from pygame.sprite import Sprite

class Lives(Sprite):
    """Class to hold lives"""

    def __init__(self, ai_settings, screen):
        super().__init__()

        # Load heart image and get its rect
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
           

