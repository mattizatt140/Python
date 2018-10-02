import sys
import pygame
import random
from ship_bullet import Ship_Bullet
from alien_bullet import Alien_Bullet
from alien import Alien
from time import sleep
import time

def check_keydown_events(event, ai_settings, screen, ship, ship_bullets):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
       fire_bullet(ai_settings, screen, ship, ship_bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, ship_bullets, alien_bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, ship_bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, ship_bullets, alien_bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, ship_bullets, alien_bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_lives()

        # Empty the list of aliens and bullets
        aliens.empty()
        ship_bullets.empty()
        alien_bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def fire_bullet(ai_settings, screen, ship, ship_bullets):
    """Fire a bullet if limit not reached yet"""
    # Create a new bullet and add it to the bullets group
    if len(ship_bullets) < ai_settings.ship_bullets_allowed:
        new_bullet = Ship_Bullet(ai_settings, screen, ship)
        ship_bullets.add(new_bullet)

def alien_fire_bullet(ai_settings, screen, aliens, alien_bullets):
    """Fire a bullet if stochastic bound hit"""
    # Create a new bullet and add it to alien bullet group
    for alien in aliens:
        if random.randint(0, 400 * len(aliens)) == 0:
            new_alien_bullet = Alien_Bullet(ai_settings, screen, alien)
            alien_bullets.add(new_alien_bullet)
 
def check_ship_bullets(ship_bullets):
    for bullet in ship_bullets:
        if bullet.rect.bottom <= 0:
            ship_bullets.remove(bullet)

def check_alien_bullets(ai_settings, alien_bullets):
    for bullet in alien_bullets:
        if bullet.rect.bottom >= ai_settings.screen_height:
            alien_bullets.remove(bullet)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, ship_bullets, alien_bullets):
    """Update position of bullets and get rid of old bullets"""

    # Update ship bullet positions
    ship_bullets.update()

    # Stochasticly generate new alien bullets
    alien_fire_bullet(ai_settings, screen, aliens, alien_bullets)

    # Update alien bullet positions
    alien_bullets.update()

    # Get rid of ship bullets that have disappeared
    check_ship_bullets(ship_bullets)

    # Get rid of alien bullets that have disappeared
    check_alien_bullets(ai_settings, alien_bullets)

    # Check any collisions between ship bullets and aliens
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, ship_bullets, alien_bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, ship_bullets, alien_bullets):
    """Respond to bullet-alien collisions"""
    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(ship_bullets, aliens, True, True)

    # Add points for hit
    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create new fleet
        ship_bullets.empty()
        alien_bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, ship_bullets, alien_bullets, play_button):
    """Update images on screen and refresh screen"""
    screen.fill(ai_settings.bg_color)

    # Redraw redraw ship bullets behind ship and aliens
    for bullet in ship_bullets.sprites():
        bullet.draw_bullet()

    # Copy ship and alien images to the screen
    ship.blitme()
    aliens.draw(screen)

    # Draw alien bullets
    for bullet in alien_bullets.sprites():
        bullet.draw_bullet()

    # Draw the score information
    sb.show_score()
    
    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make most recent screen visible
    pygame.display.flip()

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of row of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (4 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 1:
        # Decrememnt ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_lives()

        # Empty the list of aliens, bullets, and alien bullets
        aliens.empty()
        ship_bullets.empty()
        alien_bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause for 2 seconds
        sleep(2) 

    else:
        # Update lives
        stats.ships_left -= 1
        sb.prep_lives()

        # Write user's score if new high score
        if new_high_score:
            write_high_score(stats)

        # Restart game
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets):
    """Check if any alines have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:

            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets)
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets):
    """Check if the fleet is at an edge, update all alien positions"""
    # Change fleet direction if aliens hit edge
    check_fleet_edges(ai_settings, aliens)

    # Move alien fleet
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):

        ship_hit(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets)
        
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, ship_bullets, alien_bullets)

def read_high_score():
    """Read universal high score from file"""
    # Get high_score
    with open("High_Score.txt", 'r') as scoreRead:
        high_score = int(scoreRead.read())

    return high_score

def write_high_score(stats):
    """Write users score to high score text file for later use"""
    # Write high score
    with open("High_Score.txt", 'w') as scoreWrite:
        scoreWrite.write(str(stats.high_score))

def new_high_score(stats):
    """Return true if user's score is larger than high score for writing"""
    # Check if user's score is larger
    if stats.high_score > read_high_score():
        return True
    else:
        return False

def check_high_score(stats, sb):
    """Check if current score is greater than high score for real time"""
    if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()