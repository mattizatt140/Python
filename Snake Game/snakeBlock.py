import pygame
from pygame.sprite import Sprite

class SnakeBlock(Sprite):
    """Model of snake"""
    def __init__(self, ai_settings, screen, snake, position):
        # Super constructor
        super().__init__()

        # Create screen and settings attributes
        self.screen = screen

        # Snake settings
        self.speed, self.color = ai_settings.snake_speed, ai_settings.snake_color

        # Movement flags
        self.moving_up, self.moving_down, self.moving_right, self.moving_left = False, False, False, False

        # Start snake at center of screen
        if position == 0:
            self.rect_left, self.rect_top = float(ai_settings.screen_width / 2) - 12.5, float(ai_settings.screen_height / 2) + 12.5
        
        # Create new block at position of last block
        else:
            self.rect_left, self.rect_top = snake.ListOfBody[position - 1].rect.left, snake.ListOfBody[position - 1].rect.top

        # Create snakeBlock's rect
        self.rect = pygame.Rect(self.rect_left, self.rect_top, 25, 25)