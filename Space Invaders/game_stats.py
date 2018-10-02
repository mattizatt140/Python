from game_functions import read_high_score

class GameStats(object):
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings

        # Start game with fresh stats
        self.reset_stats()

        # Start Space Invaders with an active state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0