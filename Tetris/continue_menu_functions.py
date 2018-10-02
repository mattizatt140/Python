import pygame as pg
import game_functions as gf
import sys

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
    if buttons.get("continue_button").rect.collidepoint(x, y):
        stats.continue_menu_active, stats.game_active = False, True
        pg.mouse.set_visible(False)
        sounds.unpause_sounds(); sounds.play_button_click()
    elif buttons.get("settings_button").rect.collidepoint(x, y):
        stats.continue_settings_active, stats.continue_menu_active = True, False
        sounds.play_button_click()
    elif buttons.get("quit_button").rect.collidepoint(x, y):
        sys.exit()

def update_screen(settings, stats, screen, menu, buttons, texts):
    """Update continue menu screen for when game is still playing"""
    menu.draw_outline()

    gf.render_next_block(settings, screen, stats)

    gf.render_hold_block(settings, screen, stats)

    buttons.get("continue_button").draw_button()

    buttons.get("quit_button").draw_button()

    buttons.get("settings_button").draw_button()

    texts.get("level_num_text").draw_text()

    texts.get("score_num_text").draw_text()