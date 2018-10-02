from button import Button

class Button_Container(object):
    """Container for all buttons in the game"""
    # Initialize game's buttons
    def __init__(self, settings, screen):

        # Container contains references to settings and screen
        self.settings, self.screen = settings, screen

        # Initialize button dictionary
        self.buttons = {}

        """All buttons accessible by dictionary name"""
        # Functional buttons
        self.add("play_button", "PLAY", 300, 300)
        self.add("continue_button", "CONTINUE", 300, 300)
        self.add("quit_button", "QUIT", 300, 400)
        self.add("pause_button", "PAUSED", 300, 300)
        self.add("yes_button", "YES", 300, 300)
        self.add("no_button", "NO", 300, 350)
        self.add("main_menu_button", "MAIN MENU", 300, 375)
        self.add("settings_button", "SETTINGS", 300, 350)
        self.add("restart_button", "RESTART", 300, 425)

        # Settings buttons
        self.add("off_button", "OFF", 300, 90)
        self.add("low_button", "LOW", 300, 140)
        self.add("mid_button", "MID", 300, 190)
        self.add("high_button", "HIGH", 300, 240)
        self.add("black_button", "BLACK", 300, 360)
        self.add("white_button", "WHITE", 300, 410)

    def add(self, name, contents, x_coord, y_coord, width=200, height=50):
        """Add a button to the container's dictionary"""
        # @name the button's dictionary key
        # @contents the words the button display
        self.buttons[name] = Button(self.settings, self.screen, contents, x_coord, y_coord, width, height)

    def get(self, button_name):
        """Retrieve a button from the dictionary"""
        # Try-catch block is for dubugging purposes | Will be removed
        try:
            return self.buttons[button_name]
        except:
            raise NameError("ERROR: BUTTON DOES NOT EXIST")

    def allButtons(self):
        """Return all buttons in the game"""
        # Dictionary returns list of values which are the buttons
        return self.buttons.values()

    def recolor(self, settings):
        """Recolor all buttons"""
        # Retrieve each button and recolor it individually
        for button in self.buttons.values():
            button.recolor(settings)