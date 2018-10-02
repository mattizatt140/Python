import pygame as pg

class Menu(object):
    """Handler of drawing menu interface to screen"""
    def __init__(self, settings, screen, title, texts):
        self.settings = settings
        self.screen = screen
        self.title = title
        self.next_text = texts.get("next_text")
        self.level_text = texts.get("level_text")
        self.score_text = texts.get("score_text")
        self.hold_text = texts.get("hold_text")

    def draw_outline(self):
        """Draw screen outline"""
        # Fill background with black
        self.screen.fill(self.settings.screen_color)

        # Hold text and box
        self.hold_text.draw_text()
        pg.draw.line(self.screen, self.settings.style_color, (10, 60), (139, 60)), pg.draw.line(self.screen, self.settings.style_color, (10, 190), (139, 190))
        pg.draw.line(self.screen, self.settings.style_color, (10, 60), (10, 190)), pg.draw.line(self.screen, self.settings.style_color, (139, 60), (139, 190))

        pg.draw.line(self.screen, self.settings.style_color, (149, 0), (149, self.settings.screen_height))

        # Line which seperates game from menu
        pg.draw.line(self.screen, self.settings.style_color, (self.settings.game_screen_width, 0), (self.settings.game_screen_width, self.settings.screen_height))

        # Draw title image
        self.title.draw_image()

        # Draw "NEXT" text
        self.next_text.draw_text()

        # Draw box which surrounds next piece image
        pg.draw.line(self.screen, self.settings.style_color, (460, 185), (590, 185)), pg.draw.line(self.screen, self.settings.style_color, (460, 315), (590, 315))
        pg.draw.line(self.screen, self.settings.style_color, (460, 185), (460, 315)), pg.draw.line(self.screen, self.settings.style_color, (590, 185), (590, 315))

        # Write level to screen
        self.level_text.draw_text()

        pg.draw.line(self.screen, self.settings.style_color, (460, 395), (590, 395)), pg.draw.line(self.screen, self.settings.style_color, (460, 445), (590, 445))
        pg.draw.line(self.screen, self.settings.style_color, (460, 395), (460, 445)), pg.draw.line(self.screen, self.settings.style_color, (590, 395), (590, 445))

        # Write score to screen
        self.score_text.draw_text()

        pg.draw.line(self.screen, self.settings.style_color, (460, 515), (590, 515)), pg.draw.line(self.screen, self.settings.style_color, (460, 565), (590, 565))
        pg.draw.line(self.screen, self.settings.style_color, (460, 515), (460, 565)), pg.draw.line(self.screen, self.settings.style_color, (590, 515), (590, 565))