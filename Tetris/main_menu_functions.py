import pygame as pg
import sys
import game_functions as gf

def check_events(stats, buttons, sounds):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            check_mouse_events(event, stats, buttons, sounds, x, y)
            
def check_keydown_events(event):
    if event.key == pg.K_ESCAPE:
        sys.exit()

def check_mouse_events(event, stats, buttons, sounds, x, y):
    if buttons.get("play_button").rect.collidepoint(x, y):
        sounds.play_button_click()
        stats.main_menu_active, stats.game_active = False, True
        pg.mouse.set_visible(False)

    elif buttons.get("settings_button").rect.collidepoint(x, y):
        sounds.play_button_click()
        stats.main_menu_active, stats.settings_active = False, True

    elif buttons.get("quit_button").rect.collidepoint(x, y):
        sys.exit()

def update_screen(menu, buttons):
    """Update menu screen"""
    menu.draw_outline()

    buttons.get("play_button").draw_button()

    buttons.get("settings_button").draw_button()

    buttons.get("quit_button").draw_button()