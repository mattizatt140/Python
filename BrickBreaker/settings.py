import pygame as pg
from win32api import GetSystemMetrics

class Settings(object):
    """Settings contianer"""
    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 520
        self.screen_color = (0, 0, 0)

        # Paddle settings
        self.paddle_width = 100
        self.paddle_height = 20
        self.paddle_speed = 8
        self.paddle_dir = 0
        self.paddle_color = (255, 255, 255)

        # Ball settings
        self.ball_width = 10
        self.ball_speed = 5
        self.ball_color = (255, 0, 0)

        # Brick settings
        self.brick_width = 100
        self.brick_height = 40
        self.brick_color = (200, 0, 0)