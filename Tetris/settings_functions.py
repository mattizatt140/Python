import pygame as pg
import sys

def check_events(settings, stats, title, buttons, texts, text_input, sounds):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            check_click_events(event, settings, stats, title, buttons, texts, text_input, sounds, x, y)

def check_keydown_events(event):
    if event.key == pg.K_ESCAPE:
        sys.exit()

def check_click_events(event, settings, stats, title, buttons, texts, text_input, sounds, x, y):
    if buttons.get("main_menu_button").rect.collidepoint(x, y):
        sounds.play_button_click()
        stats.main_menu_active, stats.settings_active = True, False

    elif buttons.get("off_button").rect.collidepoint(x, y):
        sounds.sound_on = False
        
    elif buttons.get("low_button").rect.collidepoint(x, y):
        sounds.sound_on = True
        sounds.set_volume(0.3)
        sounds.play_button_click()

    elif buttons.get("mid_button").rect.collidepoint(x, y):
        sounds.sound_on = True
        sounds.set_volume(0.5)
        sounds.play_button_click()

    elif buttons.get("high_button").rect.collidepoint(x, y):
        sounds.sound_on = True
        sounds.set_volume(0.7)
        sounds.play_button_click()

    elif buttons.get("black_button").rect.collidepoint(x, y):
        sounds.play_button_click()

        settings.screen_color = (0, 0, 0)
        settings.style_color = (255, 255, 255)
        settings.input_inactive_color = (100, 100, 100)
        settings.input_active_color = (255, 255, 255)

        text_input.recolor(settings)

        for button in buttons.allButtons():
            button.recolor(settings)
        
        for text in texts.allTexts():
            text.recolor(settings)

        settings.title_img = pg.image.load('images/tetris-logo_black.png')
        settings.block_img = [pg.image.load('images/long_block.png'), pg.image.load('images/square_block.png'), pg.image.load('images/z_block_black.png'), pg.image.load('images/s_block_black.png'),
                              pg.image.load('images/left_L_block_black.png'),  pg.image.load('images/right_L_block_black.png'), pg.image.load('images/t_block_black.png')]

        title.image = settings.title_img
    
    elif buttons.get("white_button").rect.collidepoint(x, y):
        sounds.play_button_click()

        settings.screen_color = (255, 255, 255)
        settings.style_color = (0, 0, 0)
        settings.input_inactive_color = (200, 200, 200)
        settings.input_active_color = (0, 0, 0)

        text_input.recolor(settings)

        for button in buttons.allButtons():
            button.recolor(settings)
        
        for text in texts.allTexts():
            text.recolor(settings)

        settings.title_img = pg.image.load('images/tetris-logo_white.png')
        settings.block_img = [pg.image.load('images/long_block.png'), pg.image.load('images/square_block.png'), pg.image.load('images/z_block_white.png'), pg.image.load('images/s_block_white.png'),
                              pg.image.load('images/left_L_block_white.png'),  pg.image.load('images/right_L_block_white.png'), pg.image.load('images/t_block_white.png')]

        title.image = settings.title_img

def update_screen(menu, buttons, texts):
    menu.draw_outline()

    buttons.get("main_menu_button").draw_button()

    buttons.get("off_button").draw_button()

    buttons.get("low_button").draw_button()

    buttons.get("mid_button").draw_button()

    buttons.get("high_button").draw_button()

    buttons.get("black_button").draw_button()

    buttons.get("white_button").draw_button()

    texts.get("volume_text").draw_text()

    texts.get("theme_text").draw_text()

def reposition_button(main_menu_button):
    main_menu_button.rect.y = 500
    main_menu_button.prep_msg("MAIN MENU")

def unposition_button(main_menu_button):
    main_menu_button.rect.y = 350
    main_menu_button.prep_msg("MAIN MENU")