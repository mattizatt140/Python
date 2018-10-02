from text import Text

class Text_Container(object):
    """Container for all texts in the game"""
    # Initialize game's texts
    def __init__(self, settings, screen):

        # Container contains references to settings and screen
        self.settings, self.screen = settings, screen

        # Initialize text dictionary
        self.texts = {}

        """All texts accessible by dictionary name"""
        # Functional texts
        self.add("next_text", "NEXT", 525, 175)
        self.add("hold_text", "HOLD", 75, 50)
        self.add("level_text", "LEVEL", 525, 385)
        self.add("level_num_text", "0".zfill(2), 525, 435)
        self.add("score_text", "SCORE", 525, 505)
        self.add("score_num_text", "0".zfill(6), 525, 555)
        self.add("ask_text", "ENTER SCORE ON LEADERBOARD?", 300, 250, 23)
        self.add("enter_name_text", "ENTER NAME", 300, 260, 38)

        # Settings texts
        self.add("screen_color_text", "SCREEN COLOR", 300, 310)
        self.add("volume_text", "VOLUME", 300, 50)
        self.add("theme_text", "THEME", 300, 320)

    def add(self, name, contents, x_coord, y_coord, size = 40):
        """Add a text to the container's dictionary"""
        # Text is retrievable through the name argument
        # The text object's contained text is the contents argument
        self.texts[name] = Text(self.settings, self.screen, contents, x_coord, y_coord, size)

    def get(self, text_name):
        """Retrieve a text from the dictionary"""
        # Try-catch block is for dubugging purposes | Will be removed
        try:
            return self.texts[text_name]
        except:
            raise NameError("ERROR: TEXT DOES NOT EXIST")

    def allTexts(self):
        """Return all texts in the game"""
        # Dictionary returns list of values which are the texts
        return self.texts.values()

    def recolor(self, settings):
        """Recolor all texts"""
        # Retrieve each text and recolor it individually
        for text in self.texts.values():
            text.recolor(settings)