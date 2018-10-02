import pygame
import game_functions as gf
import sys

from time import clock
from pygame.sprite import Group
from settings import Settings

from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """Main function to run game"""

    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()

    # Set screen width and height
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.RESIZABLE) 
    pygame.display.set_caption("CharLee MacDennis 2: Electric Bugaloo")

    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    # Make the Puase button
    pause_button = Button(ai_settings, screen, "Paused")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings);

    # Set stats.high_score to be equal to universal high score
    stats.high_score = gf.read_high_score()

    # Create a scoreboard
    sb = Scoreboard(ai_settings, screen, stats)


    # Make a ship, a group of ship bullets
    ship = Ship(ai_settings, screen)
    ship_bullets = Group()
    
    # Create alien and group of alien bullets
    aliens = Group()
    alien_bullets = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create clock for FPS limit
    clock = pygame.time.Clock()

    # Start the main game loop
    while True:
        # 60 fps
        clock.tick(120)

        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, ship_bullets, alien_bullets)

        if stats.game_active:

            # Update ship status
            ship.update()

            # Update all bullets on screen
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, ship_bullets, alien_bullets)

            # Update aliens status
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets)

        # Draw and refresh the screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, ship_bullets, alien_bullets, play_button)

if __name__ == '__main__':
    run_game()