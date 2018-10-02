import pygame.font
import pygame as pg

class Button(object):
    """Class to create button instances"""

    def __init__(self, settings, screen, msg, x, y, width, height):
        """Initialize button attributes"""
        # Button's personal screen for drawing purposes
        self.screen = screen

        # Set the dimensions and properties of the button
        self.width, self.height = width, height

        self.button_color = settings.screen_color
        self.text_color = settings.style_color

        # Create font object
        self.font = pygame.font.SysFont(None, 30)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.msg = msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        # Create text surface from button's text
        self.txt_surface = self.font.render(msg, True, self.text_color, self.button_color)

        # Get the text image's rect
        self.txt_surface_rect = self.txt_surface.get_rect()

        # Reposition the text
        self.txt_surface_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        # Draw the button's outline
        pg.draw.rect(self.screen, self.text_color, pg.Rect(self.rect.left - 1, self.rect.top - 1, self.rect.width + 2, self.rect.height + 2))

        # Draw the button
        pg.draw.rect(self.screen, self.button_color, self.rect)

        # Blit the button's text onto it
        self.screen.blit(self.txt_surface, self.txt_surface_rect)

    def recolor(self, settings):
        """Recolor the button"""
        # Change button and text color
        self.button_color, self.text_color = settings.screen_color, settings.style_color
        
        # Prepare mesage with new color
        self.prep_msg(self.msg)