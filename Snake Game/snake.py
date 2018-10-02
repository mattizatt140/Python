import pygame
from settings import Settings
from snakeBlock import SnakeBlock

class Snake(object):
    '''Class to bind snake blocks together'''
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        # Stores length of snake body
        self.bodyLength = 0

        # List to hold the snake's body blocks
        self.ListOfBody = []
        self.add_body()

    def update(self):
        '''Update location of all snake body blocks'''
        # Cycle through body blocks from last to start
        for i in range(self.bodyLength - 1, -1, -1):

            # If block is not the head, move block to position of next block down
            if i > 0:
                self.ListOfBody[i].rect.left = self.ListOfBody[i - 1].rect.left
                self.ListOfBody[i].rect.top = self.ListOfBody[i - 1].rect.top

            # If block is head, move according to movement flags
            else:

                # Move up
                if self.ListOfBody[i].moving_up:
                    self.ListOfBody[i].rect.top -= self.ListOfBody[i].speed

                # Move down
                elif self.ListOfBody[i].moving_down:
                    self.ListOfBody[i].rect.top += self.ListOfBody[i].speed

                # Move right
                elif self.ListOfBody[i].moving_right:
                    self.ListOfBody[i].rect.left += self.ListOfBody[i].speed

                # Move left
                elif self.ListOfBody[i].moving_left:
                    self.ListOfBody[i].rect.left -= self.ListOfBody[i].speed 

    def draw_snake(self):
        '''Draw snake to the screen'''
        # Draw all body blocks to screen
        for i in range(self.bodyLength):
            pygame.draw.rect(self.ListOfBody[i].screen, self.ListOfBody[i].color, self.ListOfBody[i])

    def add_body(self):
        '''Add one body block to snake'''
        # Create new body block to add
        newBody = SnakeBlock(self.ai_settings, self.screen, self, self.bodyLength)

        # Add one to body length
        self.bodyLength += 1

        # Append newBody to list of body
        self.ListOfBody.append(newBody)