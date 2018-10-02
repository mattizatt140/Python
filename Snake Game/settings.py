class Settings(object):
    """Container for game settings"""

    def __init__(self):
        self.main_menu_active = True
        self.game_active = False
        # Screen settings
        self.screen_width = 525
        self.screen_height = 475
        self.screen_color = (222,184,135)

        # Snake settings
        self.snake_speed = 25
        self.snake_color = (0, 128, 0)

        # Fruit settings
        self.fruit_color = (255, 0, 0)