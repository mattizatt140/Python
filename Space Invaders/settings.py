# Used to get user's screen width and height
from win32api import GetSystemMetrics 

class Settings(object):
    """Stores all settings for Alien Invaders"""

    def __init__(self):
        """Initialize the games static settings"""
        # Screen settings
        self.screen_width = int(GetSystemMetrics(0) / 1.5)
        self.screen_height = int(GetSystemMetrics(1) / 1.5)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Universal bullet settings
        self.bullet_width = 3
        self.bullet_height = 20

        # Ship bullet settings
        self.ship_bullets_allowed = 5
        self.ship_bullet_color = (0, 0, 255)

        # Alien bullet settings
        self.alien_bullet_color = (255, 0, 0)

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.ship_speedup_scale = 1.015
        self.ship_bullet_speedup_scale = 1.01
        self.alien_speedup_scale = 1.07
        
        # How quickly the point value increase
        self.score_scale = 1.3

        # Start game with fresh settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        # ship, bullet, alien speeds
        self.ship_speed_factor = 4
        self.ship_bullet_speed_factor = 5
        self.alien_bullet_speed_factor = 3
        self.alien_speed_factor = 0.6

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Points awarded for hit
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.ship_speedup_scale
        self.ship_bullet_speed_factor *= self.ship_bullet_speedup_scale
        self.alien_speed_factor *= self.alien_speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)