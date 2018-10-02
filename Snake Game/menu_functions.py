import pygame
import sys

def check_events(stats, play_button, leaderboard_button, exit_button):
    '''Check and apply user input'''
    # Cycle through all events
    for event in pygame.event.get():

        # Quit game if x-button has been pressed
        if event.type == pygame.QUIT:
            sys.exit()

        # Check and apply key presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        
        # Check and apply mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Get x, y coordinates of mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check mouse event
            check_mouse_events(stats, play_button, leaderboard_button, exit_button, mouse_x, mouse_y)

def check_keydown_events(event):
    '''Check user key inputs'''
    # Quit game if ESC key is pressed
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def check_mouse_events(stats, play_button, leaderboard_button, exit_button, mouse_x, mouse_y):
    '''Check user mouse clicks'''
    # Check if user clicked on play button
    if play_button.rect.collidepoint(mouse_x, mouse_y):

        # Set menu to false, game to true
        stats.main_menu_active, stats.game_active = False, True

        # Turn off mouse image for gameplay duration
        pygame.mouse.set_visible(False)

    elif leaderboard_button.rect.collidepoint(mouse_x, mouse_y):
        
        stats.main_menu_active, stats.leaderboard_menu_active = False, True

    elif exit_button.rect.collidepoint(mouse_x, mouse_y):
        sys.exit()

def update_screen(ai_settings, screen, title_card, play_button, leaderboard_button, exit_button):
    '''Fill main menu screen'''
    # Apply black background
    screen.fill(ai_settings.screen_color)

    # Draw title card
    title_card.draw_button()

    # Draw play button on screen
    play_button.draw_button()

    # Draw leaderboard button on screen
    leaderboard_button.draw_button()

    # Draw exit button on screen
    exit_button.draw_button()

def reset_game(ai_settings, screen, snake, fruit):
    '''Reset game'''
    snake.ListOfBody = []; snake.bodyLength = 0
    snake.add_body()
    fruit.update(snake)
    pygame.mouse.set_visible(True)