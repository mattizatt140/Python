import pygame as pg
import game_functions as gf
import sys

def check_events(stats, buttons, sounds):
    """Check and apply all user input"""
    # Check all input events in queue
    for event in pg.event.get():

        # If user clicks exit button, quit game
        if event.type == pg.QUIT:
            sys.exit()

        # Check keydown inputs
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event)

        # Check mouse-click inputs
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            check_mouse_events(event, stats, buttons, sounds, x, y)

def check_keydown_events(event):
    """Process all keydown events"""
    # If esc key is pressed, quit game
    if event.key == pg.K_ESCAPE:
        sys.exit()

def check_mouse_events(event, stats, buttons, sounds, x, y):
    """Process all mouse-click down events"""
    # Proceed to username input if yes button is clicked
    if buttons.get("yes_button").rect.collidepoint(x, y):
        stats.ask_if_scoreboard, stats.scoreboard_input = False, True
        sounds.play_button_click()

    # Proceed to the main menu if no button is clicked
    elif buttons.get("no_button").rect.collidepoint(x, y):
        stats.ask_if_scoreboard, stats.main_menu_active = False, True
        sounds.play_button_click()

def update_screen(settings, stats, screen, menu, buttons, texts):
    """Render new screen"""
    # Draw the main game's outlin3e
    menu.draw_outline()

    # Draw buttons
    buttons.get("yes_button").draw_button(); buttons.get("no_button").draw_button()

    # Draw texts
    texts.get("ask_text").draw_text(); texts.get("level_num_text").draw_text(); texts.get("score_num_text").draw_text()