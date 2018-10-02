import pygame as pg
import game_functions as gf
import sys

def check_events(stats, buttons, sounds, LoB):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, stats, sounds)

        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            check_mouse_events(event, stats, buttons, sounds, LoB, x, y)

def check_keydown_events(event, stats, sounds):
    if event.key == pg.K_ESCAPE:
        sys.exit()

    elif event.key == pg.K_e:
        pg.mouse.set_visible(False)
        stats.paused, stats.game_active = False, True
        sounds.unpause_sounds(); sounds.play_button_click()

def check_mouse_events(event, stats, buttons, sounds, LoB, x, y):
   if buttons.get("pause_button").rect.collidepoint(x, y):
        pg.mouse.set_visible(False)
        stats.paused, stats.game_active = False, True
        sounds.unpause_sounds(); sounds.play_button_click()

   elif buttons.get("main_menu_button").rect.collidepoint(x, y):
        stats.paused, stats.continue_menu_active = False, True
        sounds.play_button_click()

   elif buttons.get("restart_button").rect.collidepoint(x, y):
        pg.mouse.set_visible(False)
        stats.paused, stats.game_active, stats.restart = False, True, True
        sounds.play_button_click()

def update_screen(settings, stats, screen, menu, buttons, texts, block, LoB, ghost_block):
    """Render paused screen"""
    menu.draw_outline()

    gf.render_ghost_block(settings, screen, block, LoB, ghost_block)

    # Draw player block
    block.draw_block()

    # Draw all pieces in ListOfBlocks
    for piece in LoB:
        piece.draw_piece()

    # Draw next piece image
    gf.render_next_block(settings, screen, stats)

    gf.render_hold_block(settings, screen, stats)

    buttons.get("pause_button").draw_button()

    buttons.get("main_menu_button").draw_button()

    buttons.get("restart_button").draw_button()

    texts.get("level_num_text").draw_text()

    texts.get("score_num_text").draw_text()