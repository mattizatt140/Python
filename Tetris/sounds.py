import pygame as pg

class Sounds(object):
    """Container for sounds"""
    def __init__(self):
        # Allow for player to turn off sounds
        self.sound_on = True

        # Sound for when game starts
        self.power_on_sound = pg.mixer.Sound('sounds/power_on.wav')
        self.power_on_sound.set_volume(0.3)
        self.music = pg.mixer.Sound('sounds/clair.wav')

        # Sound for player button clicks
        self.button_click_sound = pg.mixer.Sound('sounds/button_click.wav')
        self.button_click_sound.set_volume(0.3)

        # Sound for when piece drops with down-key
        self.piece_drop_sound = pg.mixer.Sound('sounds/piece_drop.wav')
        self.piece_drop_sound.set_volume(0.3)

        # Sound for when line clears
        self.line_cleared_sound = pg.mixer.Sound('sounds/line_cleared.wav')
        self.line_cleared_sound.set_volume(0.3)

        # Sound when blocks exceed top boundry
        self.game_over_sound = pg.mixer.Sound('sounds/game_over.wav')
        self.game_over_sound.set_volume(0.2)

        # Sound for when piece lands on ground
        self.piece_land_sound = pg.mixer.Sound('sounds/piece_land.wav')
        self.piece_land_sound.set_volume(0.3)

        # Rotate sound for a, d keys
        self.rotate_sound = pg.mixer.Sound('sounds/rotate.wav')
        self.rotate_sound.set_volume(0.2)

    def set_volume(self, volume):
        self.button_click_sound.set_volume(volume)
        self.piece_drop_sound.set_volume(volume)
        self.line_cleared_sound.set_volume(volume)
        self.piece_land_sound.set_volume(volume)
        self.rotate_sound.set_volume(volume - 0.1)
        self.game_over_sound.set_volume(volume - 0.1)

    def play_power_on(self):
        self.power_on_sound.play()

    def play_button_click(self):
        if self.sound_on:
            self.button_click_sound.play()

    def play_piece_drop(self):
        if self.sound_on:
            self.piece_drop_sound.play()

    def stop_piece_drop(self):
        self.piece_drop_sound.stop()

    def play_line_cleared(self):
        if self.sound_on:
            self.line_cleared_sound.play()

    def play_game_over(self):
        if self.sound_on:
            self.game_over_sound.play()

    def play_piece_land(self):
        if self.sound_on:
            self.piece_land_sound.play()

    def play_rotate(self):
        if self.sound_on:
            self.rotate_sound.play()

    def pause_sounds(self):
        pg.mixer.pause()

    def unpause_sounds(self):
        pg.mixer.unpause()

    def stop_sounds(self):
        pg.mixer.stop()