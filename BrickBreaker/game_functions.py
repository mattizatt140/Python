import pygame as pg
import sys
from brick import Brick

def check_events(paddle):
    """Check user events during game"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, paddle)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, paddle)

def check_keydown_events(event, paddle):
    """Check keydown events"""
    if event.key == pg.K_ESCAPE:
        sys.exit()
    elif event.key == pg.K_LEFT:
        paddle.dir = -1
    elif event.key == pg.K_RIGHT:
        paddle.dir = 1

def check_keyup_events(event, paddle):
    if event.key == pg.K_LEFT and paddle.dir != 1:
        paddle.dir = 0
    elif event.key == pg.K_RIGHT and paddle.dir != -1:
        paddle.dir = 0

def update_game(settings, paddle, ball, ListOfBricks):
    if paddle.rect.left > 3 and paddle.dir == -1:
        paddle.rect.left -= paddle.speed
    elif paddle.rect.right < settings.screen_width and paddle.dir == 1:
        paddle.rect.right += paddle.speed

    ball.rect.left += ball.vel[0]
    ball.rect.top += ball.vel[1]

    ball_piece_collide(ball, ListOfBricks)

    if ball.rect.colliderect(paddle) or ball.rect.top <= 0:
            ball.vel[1] =  -ball.vel[1]
    elif ball.rect.right >= settings.screen_width or ball.rect.left <= 0:
        ball.vel[0] = -ball.vel[0]

def ball_piece_collide(ball, ListOfBricks):
    for brick in ListOfBricks:
        if ball.rect.colliderect(brick):
            if hit_from_top(ball, brick) or hit_from_bottom(ball, brick):
                ball.vel[1] = -ball.vel[1]

            elif hit_from_left(ball, brick) or hit_from_right:
                ball.vel[0] = -ball.vel[0]

            ListOfBricks.remove(brick)

def hit_from_top(ball, brick):
    return ball.rect.bottom >= brick.rect.top and ball.rect.bottom < brick.rect.top + 3

def hit_from_bottom(ball, brick):
    return ball.rect.top <= brick.rect.bottom and ball.rect.top >= brick.rect.bottom - 5

def hit_from_left(ball, brick):
    return ball.rect.right >= brick.rect.left and ball.rect.right < brick.rect.left + 3

def hit_from_right(ball, brick):
    return ball.rect.left <= brick.rect.right and ball.rect.left > brick.rect.right - 3

def update_screen(settings, screen, paddle, ball, ListOfBricks):
    """Render the next frame of screen"""
    screen.fill(settings.screen_color)
    paddle.draw_paddle()
    ball.draw_ball()
    
    for brick in ListOfBricks:
        brick.draw_brick()

def construct_bricks(settings, screen):
    bricks = []
    for i in range(0, 180, settings.brick_height):
        for j in range(0, settings.screen_width, settings.brick_width):
            newBrick = Brick(settings, screen)
            newBrick.rect.topleft = (j, i)
            bricks.append(newBrick)

    return bricks