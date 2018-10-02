import pygame as pg

class Input_Box(object):
    """Box for text input"""

    def __init__(self, settings, screen, x, y):
        """Initialize starting attributes"""
        # Input_Box's personal screen for drawing purposes
        self.screen = screen

        # The box's rect attributes
        self.rect = pg.Rect(0, 0, 200, 50)
        self.rect.center = (x, y)

        # Standard pygame font for text inside box
        self.font = pg.font.Font(None, 40)

        # Input box's color attributes
        # The color changes when click/unclicked
        self.recolor(settings)
        
        # Box initially inactive with no text
        self.active = False
        self.text = ''
        
        # Create initial text surface
        self.prep_text()

    def prep_text(self):
        """Prepare text for use"""
        # Create text surface to be blit onto screen
        self.txt_surface = self.font.render(self.text, True, self.color_outline)

    def draw_input_box(self):
        """Draw Input_Box object"""
        # Draw input box outline
        pg.draw.rect(self.screen, self.color_outline, pg.Rect(self.rect.left - 1, self.rect.top - 1, self.rect.width + 2, self.rect.height + 2))

        # Draw the contained box
        pg.draw.rect(self.screen, self.color_box, self.rect)

        # Blit the current text onto box
        self.screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 12))

    def recolor(self, settings):
        """Recolor box if theme changes"""
        # Active/inactive color of box corresponds to box's active/inactive status
        self.color_active, self.color_inactive = settings.input_active_color, settings.input_inactive_color

        # The color of the box's outline
        # Begins with inactive color
        self.color_outline = self.color_inactive

        # The color of the text box's interior
        self.color_box = settings.screen_color

    def set_active(self):
        """Set input box to an active state"""
        # Set to active state
        self.active = True

        # Set color to active color
        self.color_outline = self.color_active

        # Prepare fresh text surface
        self.prep_text()

    def set_inactive(self):
        """Set input box to an inactive state"""
        # Set to inactive state
        self.active = False

        # Reset color to inactive color
        self.color_outline = self.color_inactive

        # Prepare fresh text surface
        self.prep_text()

    def reset(self):
        """Reset box to base state"""
        # Reset text
        self.text = ''
        
        # Set to inactive sate
        self.set_inactive()

    def backspace(self):
        """Remove a character from text"""
        # Remove the last letter of the word
        self.text = self.text[:-1]

        # Prepare text surface from new redacted text
        self.prep_text()

    def addChar(self, event):
        """Add a new character to the text"""
        # Limit length of input to 10 characters
        if len(self.text) < 10:

            # Add character to the text if letter
            if event.key >= 97 and event.key <= 122:
                self.text += event.unicode

            # Prepare text surface from new redacted text
            self.prep_text()