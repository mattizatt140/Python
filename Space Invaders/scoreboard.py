import pygame.font
from pygame.sprite import Group
from lives import Lives

class Scoreboard(object):
    """A class to report scoring information"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)
        
        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        rounded_score = int(round(self.stats.high_score, -1))
        score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the high score at the top middle of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = (self.ai_settings.screen_width / 2) + (self.high_score_rect.width / 2)
        self.high_score_rect.top = 10

    def prep_lives(self):
        """Show how many lives are left"""
        self.lives = Group()
        for lives_number in range(self.stats.ships_left):
            life = Lives(self.ai_settings, self.screen)
            life.rect.x = 10 + lives_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def show_score(self):
        """Draw score to the screen"""
        # Draw score
        self.screen.blit(self.score_image, self.score_rect)
        
        # Draw high score

        self.screen.blit(self.high_score_image, self.high_score_rect)

        # Draw lives
        self.lives.draw(self.screen)

    def show_high_score(self):
        """Draw high score to the screen"""