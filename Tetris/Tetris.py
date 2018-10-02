import pygame as pg
import game_functions as gf
import main_menu_functions as mf
import paused_functions as pag
import scoreboard_input_functions as sif
import ask_if_scoreboard_functions as aisf
import continue_menu_functions as cmf
import settings_functions as sf
import continue_settings_functions as csf

from menu import Menu
from sounds import Sounds
from settings import Settings
from stats import Stats
from text import Text
from image import Image
from button import Button
from input_box import Input_Box
from text_container import Text_Container
from button_container import Button_Container
from ghost_block import Ghost_Block

def run_game():

    pg.init()
    # Initialize game
    pg.mixer.init()

    # Settings container
    settings = Settings()

    # Initialize gameplay window
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Tetris")
    
    # Stats container
    stats = Stats(settings, screen)

    # Contains all button objects
    buttons = Button_Container(settings, screen)

    # Contains all text objects
    texts = Text_Container(settings, screen)

    # Title image
    title = Image(screen, settings.title_img, 456, 5)

    # Text input box
    text_input = Input_Box(settings, screen, 300, 300)

    # Sounds container
    sounds = Sounds(); sounds.play_power_on()

    # Menu container
    menu = Menu(settings, screen, title, texts)
    
    # Block object contains player-controlled block
    block = gf.gen_block(settings, screen, stats)

    # Shows where player block will land
    ghost_block = Ghost_Block(settings, screen, block)

    # List of landed blocks
    LoB = []
    counter = 0

    # Set FPS cap
    clock = pg.time.Clock()

    while True:

        while stats.main_menu_active:

                # 60 FPS cap
                clock.tick(60)

                mf.check_events(stats, buttons, sounds)

                mf.update_screen(menu, buttons)

                pg.display.flip()

        if stats.game_active and stats.restart:
            stats.restart = False
            LoB.clear()
            stats.init_dynamic(stats.settings, stats.screen); stats.main_menu_active, stats.game_active = False, True
            texts.get("level_num_text").prep_text(str(stats.level).zfill(2))
            texts.get("score_num_text").prep_text(str(stats.points).zfill(6))
            block = gf.gen_block(settings, screen, stats)

        while stats.continue_menu_active:

            cmf.check_events(stats, buttons, sounds)

            cmf.update_screen(settings, stats, screen, menu, buttons, texts)

            pg.display.flip()

        if stats.settings_active or stats.continue_settings_active:

            sf.reposition_button(buttons.get("main_menu_button"))

        while stats.settings_active:

            sf.check_events(settings, stats, title, buttons, texts, text_input, sounds)

            sf.update_screen(menu, buttons, texts)

            pg.display.flip()

        while stats.continue_settings_active:

            csf.check_events(settings, stats, title, buttons, texts, text_input, sounds)

            csf.update_screen(settings, screen, stats, menu, buttons, texts)

            pg.display.flip()

        sf.unposition_button(buttons.get("main_menu_button"))

        while stats.game_active:

            # 60 FPS cap
            clock.tick(60)
           
            # Check and apply user input
            gf.check_events(settings, screen, stats, sounds, block, LoB)

            # Limit player events while keeping 60 FPS
            counter = gf.update_counter(counter, stats)

            # Update block and rest of game
            block, stats.next_block, stats.hold_block = gf.update_game(counter, settings, stats, screen, texts, sounds, block, LoB)

            gf.validate_spawn(settings, block, LoB)

            # Bool check avoids screen flash when player dies
            if stats.game_active:

                # Render next frame
                gf.update_screen(settings, stats, screen, menu, texts, block, LoB, ghost_block)

                # Flip to next frame
                pg.display.flip()

        while stats.ask_if_scoreboard:

            # 60 FPS cap
            clock.tick(60)

            aisf.check_events(stats, buttons, sounds)
            
            aisf.update_screen(settings, stats, screen, menu, buttons, texts)

            pg.display.flip()

        while stats.scoreboard_input:

            # 60 FPS cap
            clock.tick(60)

            sif.check_events(stats, buttons, text_input, sounds)

            sif.update_screen(menu, buttons, texts, text_input)

            pg.display.flip()

        while stats.display_scoreboard_active:
            pass

        while stats.paused:

            # 60 FPS cap
            clock.tick(60)

            pag.check_events(stats, buttons, sounds, LoB)

            pag.update_screen(settings, stats, screen, menu, buttons, texts, block, LoB, ghost_block)

            pg.display.flip()

if __name__ == '__main__':
    run_game()