import pygame as pg
import game_functions as gf
import sys

def check_events(stats, buttons, text_input, sounds):
    """Check and apply all user input"""
    # Check all input events in queue
    for event in pg.event.get():

        # If user clicks exit button, quit game
        if event.type == pg.QUIT:
            sys.exit()

        # Check keydown inputs
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, stats, text_input, sounds)

        # Check down mouse-click inputs
        elif event.type == pg.MOUSEBUTTONDOWN:

            # Grab coordinates of click for later processing
            x, y = pg.mouse.get_pos()

            check_mouse_events(event, stats, text_input, buttons, sounds, x, y)

def check_keydown_events(event, stats, text_input, sounds):
    """Check keydown events"""
    # Exit game if esc key is pressed and text not used
    if event.key == pg.K_ESCAPE and not text_input.active:
        sys.exit()

    # If the text_box is being used, process input
    elif text_input.active:
        
        # If esc key is pressed then set inactive
        if event.key == pg.K_ESCAPE:
            text_input.set_inactive()

        # If enter key is pressed then process text
        elif event.key == pg.K_RETURN:

            # Play button click sound
            sounds.play_button_click()
            
            # Reset input box
            text_input.reset()

            # Return to main menu
            stats.scoreboard_input, stats.main_menu_active = False, True

        # Treat backspace key like a text editor
        elif event.key == pg.K_BACKSPACE:
            text_input.backspace()

        # Add input to input box's text
        else:
            text_input.addChar(event)

def check_mouse_events(event, stats, text_input, buttons, sounds, x, y):
    """Check down mouse-click events"""
    # Set box to active if clicked on
    if text_input.rect.collidepoint(x, y):

        # Box's state to opposite of current state
        if text_input.active:
            text_input.set_inactive()
        else:
            text_input.set_active()

    # If the user clicks the main menu button, return to menu and reset
    elif buttons.get("main_menu_button").rect.collidepoint(x, y):
        
        # Play the button click sound
        sounds.play_button_click()

        # Reset the input box
        text_input.reset()

        # Return to main menu
        stats.main_menu_active, stats.scoreboard_input = True, False

    # If the user clicks anywhere outside the box, set to inactive
    else:
        text_input.set_inactive()

def update_screen(menu, buttons, texts, text_input):
    """Update screen which allows user input for leaderboard"""
    # Draw game's main outline
    menu.draw_outline()

    # Draw buttons for screen
    buttons.get("main_menu_button").draw_button()

    # Draw texts for screen
    texts.get("enter_name_text").draw_text(); texts.get("level_num_text").draw_text(); texts.get("score_num_text").draw_text()

    # Draw the input box
    text_input.draw_input_box()