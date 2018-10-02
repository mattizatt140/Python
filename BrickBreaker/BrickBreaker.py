import pygame as pg
import game_functions as gf
import time

from win32api import GetSystemMetrics
from settings import Settings
from paddle import Paddle
from ball import Ball
from brick import Brick

def run_game():
    
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height)); pg.display.set_caption("Brick Breaker"); pg.mouse.set_visible(False)
    paddle = Paddle(settings, screen)
    ball = Ball(settings, screen)
    ListOfBricks = gf.construct_bricks(settings, screen)
    clock = pg.time.Clock()

    time.sleep(1)

    while True:

        clock.tick(60)
        
        gf.check_events(paddle)

        gf.update_game(settings, paddle, ball, ListOfBricks)

        gf.update_screen(settings, screen, paddle, ball, ListOfBricks)

        pg.display.flip()

if __name__ == '__main__':
    run_game()