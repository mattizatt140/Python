import pygame
import random
from pygame.sprite import Sprite
from testRect import TestRect

class Fruit(Sprite):
    """A model for fruit the snake will eat"""

    def __init__(self, ai_settings, screen, snake):
        # Super constructor
        super().__init__()

        # Create settings and screen attributes
        self.ai_settings, self.screen = ai_settings, screen

        # TestRect for testing new fruit positions
        self.testRect = TestRect(0, 0)

        # Get possible x, y coordinates for fruit
        self.LoLocX, self.LoLocY = self.get_fruit_loc()

        # Fruit image qualities
        self.rect = pygame.Rect(0, 0, 25, 25)
        self.color = ai_settings.fruit_color

        # Start fruit at random position
        self.update(snake)

    def update(self, snake):
        '''Update fruit to new random location'''
        # Generate random positions until position doesn't land on snake
        while True:

            # Randomly choose x, y coordinate pair
            rect_left, rect_top = random.choice(self.LoLocX), random.choice(self.LoLocY)

            # Modify TestRect for testing
            self.rect.left, self.rect.top = rect_left, rect_top
            
            # Check if new rect would collide with snake
            for i in range(snake.bodyLength):

                # If new rect would collide, break check and try new rect
                if self.rect.colliderect(snake.ListOfBody[i]):
                    break

                # If last of snake blocks have been checked, keep new rect values
                elif i == (snake.bodyLength - 1):
                    return
        
    def get_fruit_loc(self):
        '''Retrieve possible x, y coordinates for fruit along grid'''
        # Lists to hold possible x, y coordinates
        LoLocX = []; LoLocY = []

        # Possible x-coordinate locations
        for i in range(0, int(self.ai_settings.screen_width / 25)):
            LoLocX.append(i * 25)

        # Possible y-coordinate locations
        for i in range(0, int(self.ai_settings.screen_height / 25)):
            LoLocY.append(i * 25)

        # Return lists
        return LoLocX, LoLocY

    def draw_fruit(self):
        """Draw fruit to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)