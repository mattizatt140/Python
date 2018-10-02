import game_functions as gf
from long_block import Long_Block
from square_block import Square_Block
from t_block import T_Block
from left_L_block import Left_L_Block
from right_L_block import Right_L_Block
from s_block import S_Block
from z_block import Z_Block

class Stats(object):
    """Container of game stats"""
    def __init__(self, settings, screen):
        # Seperate dynamic function for stat reset after each game
        self.init_dynamic(settings, screen)

    def init_dynamic(self, settings, screen):
        """Used to reset stats after each play"""
        self.settings = settings
        self.screen = screen
        self.main_menu_active, self.settings_active, self.continue_menu_active, self.continue_settings_active = True, False, False, False
        self.restart = False
        self.game_active = False
        self.ask_if_scoreboard = False
        self.scoreboard_input = False
        self.display_scoreboard_active = False
        self.paused = False
        self.piece_dropping = False
        self.should_exchange, self.first_exchange = False, True
        self.block_speed = 60
        self.block_drop_speed = 3
        self.temp_speed = self.block_speed
        self.level = 0
        self.lines_cleared = 0
        self.lines_per_level = 5
        self.points = 0
        self.hold_block = None
        self.move_delay = 25
        self.block_options = [S_Block(settings, screen), Z_Block(settings, screen), T_Block(settings, screen), Left_L_Block(settings, screen),
                              Right_L_Block(settings, screen), Square_Block(settings, screen), Long_Block(settings, screen)]
        self.next_block = gf.gen_block(settings, screen, self)
        