import pygame
import sys
from time import sleep

def check_events(ai_settings, snake):
    '''Check and apply user input'''
    # Boolean value to restrict one key press per frame
    isFirstKey = True

    # Evaluate user input
    for event in pygame.event.get():

        # Quit if exit button is clicked
        if event.type == pygame.QUIT:
            sys.exit()

        # Check keydown events
        elif event.type == pygame.KEYDOWN and isFirstKey:
            check_keydown_events(event, snake)
            isFirstKey = False

def check_keydown_events(event, snake):
    '''Check arrow keys and ESC key'''
    # Use ESC key to quit game
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    # Change snake direction to up
    # Cannot move up if direction is down | Avoids snake moving into self
    elif event.key == pygame.K_UP and not snake.ListOfBody[0].moving_down:
            snake.ListOfBody[0].moving_up = True
            snake.ListOfBody[0].moving_right = False
            snake.ListOfBody[0].moving_left = False

    # Change snake direction to down
    # Cannot move down if direction is up | Avoids snake moving into self
    elif event.key == pygame.K_DOWN and not snake.ListOfBody[0].moving_up:
            snake.ListOfBody[0].moving_down = True
            snake.ListOfBody[0].moving_right = False
            snake.ListOfBody[0].moving_left = False

    # Change snake direction to right
    # Cannot move right if direction is left | Avoids snake moving into self
    elif event.key == pygame.K_RIGHT and not snake.ListOfBody[0].moving_left:
            snake.ListOfBody[0].moving_right = True
            snake.ListOfBody[0].moving_up = False
            snake.ListOfBody[0].moving_down = False

    # Change snake direction to left
    # Cannot move left if direction is right | Avoids snake moving into self
    elif event.key == pygame.K_LEFT and not snake.ListOfBody[0].moving_right:
            snake.ListOfBody[0].moving_left = True
            snake.ListOfBody[0].moving_up = False
            snake.ListOfBody[0].moving_down = False

def check_snake_status(ai_settings, stats, screen, snake, fruit):
    '''Check snake status'''
    # Check if snake has traveled beyond map | Exit game if it has
    if check_snake_overreach(ai_settings, snake):
        sleep(0.5)
        stats.main_menu_active, stats.game_active = True, False

    # Check if snake has eaten itself | Exit game if it has
    if check_snake_eat_self(snake):
        sleep(0.5)
        stats.main_menu_active, stats.game_active = True, False

    # Check if snake has eaten fruit | Update snake and fruit if it has
    if check_snake_fruit(snake, fruit):

        # Add new block to snake
        snake.add_body()

        # Update fruit to new position
        fruit.update(snake)

def check_snake_overreach(ai_settings, snake):
    '''Check if snake has traveled beyond the map'''
    # Return True if snake has exceeded boundries
    if snake.ListOfBody[0].rect.top < 0 or snake.ListOfBody[0].rect.left < 0 or snake.ListOfBody[0].rect.right > ai_settings.screen_width or snake.ListOfBody[0].rect.bottom > ai_settings.screen_height:
        return True

    # Return False otherwise
    else:
        return False
8
def check_snake_eat_self(snake):
    '''Exit game if snake has eaten itself'''
    # Check collision between head and rest of body
    for i in range(1, snake.bodyLength):

        # Exit game if head has collided with other body part
        if snake.ListOfBody[0].rect.colliderect(snake.ListOfBody[i]):
            return True

    # Return False otherise
    return False

def check_snake_fruit(snake, fruit):
    '''Update game if snake eats fruit'''
    # If snake rect collides with fruit rect return True
    if snake.ListOfBody[0].rect.colliderect(fruit):
        return True

    # Return False otherwise
    else:
        return False

def update_screen(ai_settings, screen, snake, fruit):
    '''Update game screen'''
    # Fill screen objects surface with black
    screen.fill(ai_settings.screen_color)

    # Draw fruit to screen
    fruit.draw_fruit()

    # Draw snake to screen
    snake.draw_snake()