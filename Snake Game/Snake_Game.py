import pygame
import game_functions as gf
import menu_functions as mf

from snake import Snake
from settings import Settings
from stats import Stats
from snakeBlock import SnakeBlock
from fruit import Fruit
from button import Button

def run_game():
    '''Main function to run game'''
    # Instantiate game
    pygame.init()

    # Instantiate settings object to hold game settings
    ai_settings = Settings()
    stats = Stats()

    # Set screen width, height, and settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Snake"); 

    # Instantiate snake
    snake = Snake(ai_settings, screen)
    
    # Instatiate fruit object
    fruit = Fruit(ai_settings, screen, snake)

    # Institiate clock object to cap FPS
    clock = pygame.time.Clock()
    
    title_card = Button(ai_settings, screen, ai_settings.screen_width / 2, ai_settings.screen_height / 6, 
                        (screen.get_rect().centerx, screen.get_rect().centery - 150), (222, 184, 135), (34, 139, 34), "SNAKE")
    play_button = Button(ai_settings, screen, ai_settings.screen_width / 3, ai_settings.screen_height / 8, 
                         (screen.get_rect().centerx, screen.get_rect().centery - 50), (222,184, 135), (34, 139, 34), "PLAY")
    leaderboard_button = Button(ai_settings, screen, ai_settings.screen_width / 3, ai_settings.screen_height / 8, 
                         (screen.get_rect().centerx, screen.get_rect().centery + 25), (222,184, 135), (34, 139, 34), "LEADERBOARD")
    exit_button = Button(ai_settings, screen, ai_settings.screen_width / 3, ai_settings.screen_height / 8, 
                         (screen.get_rect().centerx, screen.get_rect().centery + 100), (222, 184, 135), (34, 139, 34), "EXIT")

    '''Main game loop'''
    while True:

        while stats.main_menu_active:

          # Check user events and apply them
           mf.check_events(stats, play_button, leaderboard_button, exit_button)

           # Render screen
           mf.update_screen(ai_settings, screen, title_card, play_button, leaderboard_button, exit_button)

           # Flip to next rendered frame
           pygame.display.flip()

        while stats.leaderboard_menu_active:
            break

        while stats.game_active:
            # 12 FPS cap
            clock.tick(12)

            # Check user events and apply them
            gf.check_events(ai_settings, snake)

            # Update snake according to input
            snake.update()

            # Check snake and fruit status
            gf.check_snake_status(ai_settings, stats, screen, snake, fruit)

            # Render screen
            gf.update_screen(ai_settings, screen, snake, fruit)

            # Flip to next rendered frame
            pygame.display.flip()

        # Reset game settings before each new game
        mf.reset_game(ai_settings, screen, snake, fruit)

if __name__ == '__main__':
    run_game()