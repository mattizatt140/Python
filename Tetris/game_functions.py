import pygame as pg
import random
import sys
from long_block import Long_Block
from square_block import Square_Block
from t_block import T_Block
from left_L_block import Left_L_Block
from right_L_block import Right_L_Block
from s_block import S_Block
from z_block import Z_Block
from piece import Piece
from ghost_block import Ghost_Block

def check_events(settings, screen, stats, sounds, block, LoB):
    """Check and apply all user input"""
    # Check all input events in queue
    for event in pg.event.get():

        # If user clicks exit button, quit game
        if event.type == pg.QUIT:
            sys.exit()

        # Check keydown inputs
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, settings, screen, stats, sounds, block, LoB)

        # Check keyup inputs
        elif event.type == pg.KEYUP:
            check_keyup_events(event, stats, sounds, block)

def check_keydown_events(event, settings, screen, stats, sounds, block, LoB):
    """Check keydown user input"""
    # Quit game if esc key is pressed
    if event.key == pg.K_ESCAPE:
        sys.exit()

    # Attempt to move block left if left arrow key pressed
    elif event.key == pg.K_LEFT:
        move_block_left(settings, block, LoB)

    # Attempt to move block right if right arrow key pressed
    elif event.key == pg.K_RIGHT:
        move_block_right(settings, block, LoB)

    # Speed up block descent if down arrow key pressed
    elif event.key == pg.K_DOWN:
        sounds.play_piece_drop()
        stats.block_speed = stats.block_drop_speed
        stats.piece_dropping = True

    # Attempt to rotate block right if d-key is pressed
    elif event.key == pg.K_d:
        if type(block) != Square_Block:
            rotate_block_right(settings, sounds, block, LoB)

    # Attempt to rotate block left if a-key is pressed
    elif event.key == pg.K_a:
        if type(block) != Square_Block:
            rotate_block_left(settings, sounds, block, LoB)
    
    # Pause game
    elif event.key == pg.K_e:
        block.moving_left, block.moving_left_timer, block.moving_right, block.moving_right_timer = False, False, False, False
        pg.mouse.set_visible(True)
        stats.paused, stats.game_active = True, False
        stats.block_speed = stats.temp_speed
        sounds.pause_sounds(); sounds.play_button_click()

    elif event.key == pg.K_q:
        stats.should_exchange = True

def check_keyup_events(event, stats, sounds, block):
    """Check keyup user input"""
    # If user lets up left key, set left-flags to False
    if event.key == pg.K_LEFT:
        block.moving_left, block.moving_left_timer = False, False

    # If user lets up right key, set right-flags to False
    elif event.key == pg.K_RIGHT:
        block.moving_right, block.moving_right_timer = False, False

    # If user lets up down key, return descent speed to normal
    elif event.key == pg.K_DOWN:
        sounds.stop_piece_drop()
        stats.block_speed = stats.temp_speed
        stats.piece_dropping = False

def rotate_block_right(settings, sounds, block, LoB):
    """Attempt to rotate block left"""
    # Flag for sound
    block_rotates = True

    # Adjust permutation | [0, 1, 2, 3]
    if block.permutation == 3:
        block.permutation = 0
    else:
        block.permutation += 1

    # Rotate block right
    block.rotate_right()

    """Check if wall skip is needed"""
    # If block collides with other block, or breaks left or right bounds
    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):
           
        for piece in block.pieces:
            piece.rect.right += settings.block_size

    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):

        for piece in block.pieces:
            piece.rect.right -= settings.block_size * 2

    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):

        for piece in block.pieces:
            piece.rect.right += settings.block_size
            piece.rect.top -= settings.block_size

    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):

        for piece in block.pieces:
            piece.rect.top += settings.block_size

        # Adjust permutation | [0, 1, 2, 3]
        if block.permutation == 0:
            block.permutation = 3
        else:
            block.permutation -= 1

        # Rotate block back, baby
        block.rotate_left()

        block_rotates = False

    if block_rotates:
        sounds.play_rotate()

def rotate_block_left(settings, sounds, block, LoB):
    """Attempt to rotate block right"""
    # Flag for sound
    block_rotates = True

    # Adjust permutation | [0, 1, 2, 3]
    if block.permutation == 0:
        block.permutation = 3
    else:
        block.permutation -= 1

    # Rotate block left
    block.rotate_left()

    """Check if wall skip is needed"""
    # If block collides with other block, or breaks left or rights bounds
    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):
           
        for piece in block.pieces:
            piece.rect.right -= settings.block_size

    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):

        for piece in block.pieces:
            piece.rect.right += settings.block_size * 2

    if pg.sprite.groupcollide(block.pieces, LoB, False, False) or check_edges_left(settings, block) or check_edges_right(settings, block) or check_edges_bottom(settings, block):

        block_rotates = False

        for piece in block.pieces:
            piece.rect.right -= settings.block_size

        # Adjust permutation | [0, 1, 2, 3]
        if block.permutation == 3:
            block.permutation = 0
        else:
            block.permutation += 1

        # Rotate block back, baby
        block.rotate_right()

    if block_rotates:
        sounds.play_rotate()

def check_edges_left(settings, block):
    """Check if block passes left wall"""
    # Check each piece of block
    for piece in block.pieces:
        if piece.rect.left < 150:
            return True
    return False

def check_edges_right(settings, block):
    """Check if block passes right wall"""
    # Check each piece of block
    for piece in block.pieces:
        if piece.rect.right > settings.game_screen_width:
            return True
    return False

def check_edges_bottom(settings, block):
    """Check if block passes bottom wall"""
    # Check each piece of block
    for piece in block.pieces:
        if piece.rect.bottom > settings.screen_height:
            return True
    return False

def move_block_left(settings, block, LoB):
    """Attempt to move block left"""
    # Assume block will move | Set block set_down to False
    block.set_down_active = False

    # If block is touching left wall, do not move left
    for piece in block.pieces:
        if piece.rect.left == 150:
            block.set_down_active = True
            return

    # Otherwise, move block left
    for piece in block.pieces:
        piece.rect.left -= settings.block_size

    # If block collides with other blocks, move it back right
    # Set set_down_active to True to avoid player pushing into wall forever
    if pg.sprite.groupcollide(block.pieces, LoB, False, False):
        move_block_right(settings, block, LoB)
        block.set_down_active = True

    # Set timer for moving left
    block.moving_left_timer, block.moving_right_timer = True, False

def move_block_right(settings, block, LoB):
    """Attempt to move block right"""
    # Assume block will move | Set block set_down to False
    block.set_down_active = False

    # If piece touches right wall, do not move
    for piece in block.pieces:
        if piece.rect.right == settings.game_screen_width:
            block.set_down_active = True
            return

    # Move each piece in block right
    for piece in block.pieces:
        piece.rect.right += settings.block_size

    # If block collides with other blocks, move it back left
    # Set set_down_active to True to avoid player pushing into wall forever
    if pg.sprite.groupcollide(block.pieces, LoB, False, False):
        move_block_left(settings, block, LoB)
        block.set_down_active = True

    # Set timer for moving right
    block.moving_right_timer, block.moving_left_timer = True, False

def set_moving_left(stats, block):
    """Update moving_left_counter and block status"""
    # Add to counter
    block.moving_left_counter += 1

    # If counter is 25, set left to true | Creates movement delay to help with control
    if block.moving_left_counter == stats.move_delay:
        block.moving_left, block.moving_left_counter = True, 0

def set_moving_right(stats, block):
    """Update moving_right_counter and block status"""
    # Add to counter
    block.moving_right_counter += 1

    # If counter is 25, set right to true | Creates movement delay to help with control
    if block.moving_right_counter == stats.move_delay:
        block.moving_right, block.moving_right_counter = True, 0

def reset_hold_block(settings, block, hold_block, LoB):
    hold_block.moving_left, hold_block.moving_left_counter, hold_block.moving_left_timer, hold_block.moving_right, hold_block.moving_right_counter, hold_block.moving_right_timer = block.moving_left, block.moving_left_counter, block.moving_left_timer, block.moving_right, block.moving_right_counter, block.moving_right_timer

    adjust_top = hold_block.get_top() - settings.block_size
    for piece in hold_block.pieces:
        piece.rect.top -= adjust_top

    adjust_left = hold_block.get_left() - block.get_left()
    for piece in hold_block.pieces:
        piece.rect.left -= adjust_left

    while hold_block.permutation != 0:
        hold_block.permutation -= 1
        hold_block.rotate_left()

    if check_edges_right(settings, hold_block):
        while check_edges_right(settings, hold_block):
            for piece in hold_block.pieces:
                piece.rect.left -= settings.block_size

    elif check_edges_left(settings, hold_block):
        while check_edges_left(settings, hold_block):
            for piece in hold_block.pieces:
                piece.rect.right += settings.block_size

    elif pg.sprite.groupcollide(hold_block.pieces, LoB, False, False):
        while pg.sprite.groupcollide(hold_block.pieces, LoB, False, False):
            for piece in hold_block.pieces:
                piece.rect.top -= settings.block_size

def update_game(counter, settings, stats, screen, texts, sounds, block, LoB):
    """Update block, stats, and lines"""
    if stats.should_exchange and stats.first_exchange:
        stats.first_exchange, stats.should_exchange = False, False
        if type(stats.hold_block) == type(None):
            return stats.next_block, gen_block(settings, screen, stats), block
        else:
            reset_hold_block(settings, block, stats.hold_block, LoB)
            return stats.hold_block, stats.next_block, block
    else:
        stats.should_exchange = False

    # If left_timer set, update
    if block.moving_left_timer:
        set_moving_left(stats, block)

    # If right_timer set, update
    elif block.moving_right_timer:
        set_moving_right(stats, block)
            
    # Update level if appropriate
    if stats.lines_cleared >= stats.lines_per_level:
        update_level(stats, texts)

    # Restricts amount of cycles per second
    if counter % stats.block_speed == 0:

        # Set counter to 1 for later purpose
        if block.set_down_active:
            block.set_down_counter = 1

        # Move each piece in user block down a row
        for piece in block.pieces:
            piece.rect.top += settings.block_size

        # If the user's block collides with a piece in LoB:
        if pg.sprite.groupcollide(block.pieces, LoB, False, False):

            # Set set_down_active to true (wont come into play until another cycle)
            # This is why the counter is set to one before this point
            block.set_down_active = True

            # Move block up a row to get out of collision
            for piece in block.pieces:
                piece.rect.top -= settings.block_size

            # If block had been sitting without input for one cycle:
            if block.set_down_counter == 1:

                sounds.play_piece_land()
                # Append block to LoB
                for piece in block.pieces:
                    LoB.append(piece)

                # Reset counter
                block.set_down_counter = 0

                # Clear full lines
                clear_lines(settings, stats, texts, screen, sounds, LoB)

                # Check if any blocks have reached ceiling
                check_ceiling(stats, sounds, LoB)
                
                stats.first_exchange = True

                # Return new block
                return stats.next_block, gen_block(settings, screen, stats), stats.hold_block
        
        for piece in block.pieces:

            if piece.rect.bottom > settings.screen_height:
                block.set_down_active = True

                for piece in block.pieces:

                    piece.rect.bottom -= settings.block_size

                    if block.set_down_counter == 1:
                        LoB.append(piece)

                if block.set_down_counter == 1:
                    sounds.play_piece_land()

                    block.set_down_counter = 0

                    clear_lines(settings, stats, texts, screen, sounds, LoB)

                    check_ceiling(stats, sounds, LoB)

                    stats.first_exchange = True

                    return stats.next_block, gen_block(settings, screen, stats), stats.hold_block
        
    if counter % 2 == 0:
        move_block(settings, block, LoB)

    return block, stats.next_block, stats.hold_block

def move_block(settings, block, LoB):
    """Move block according to movement flags"""
    # Move left automatically
    if block.moving_left:
        move_block_left(settings, block, LoB)

    # Move right automatically
    elif block.moving_right:
        move_block_right(settings, block, LoB)

def update_counter(counter, stats):
    """Add to counter which determines updates per second"""
    # Reset counter if it reaches block speed
    if counter == stats.block_speed:
        counter = 1
    else:
        counter += 1
    return counter

def gen_block(settings, screen, stats):
    """Generate and return new block"""
    # Use random number to determine block
    if len(stats.block_options) == 0:
        stats.block_options.append(S_Block(settings, screen))
        stats.block_options.append(Z_Block(settings, screen))
        stats.block_options.append(T_Block(settings, screen))
        stats.block_options.append(Left_L_Block(settings, screen))
        stats.block_options.append(Right_L_Block(settings, screen))
        stats.block_options.append(Square_Block(settings, screen))
        stats.block_options.append(Long_Block(settings, screen))

    block = stats.block_options[random.randrange(0, len(stats.block_options))]
    stats.block_options.remove(block)
    return block

def clear_lines(settings, stats, texts, screen, sounds, LoB):
    """Clear lines which are completely filled"""
    # Container to hold cleared line y-values
    ListOfClearedLines = []

    # Used to test collision within every block of each line
    testRect = Piece(settings, screen, (0, 0, 0), pg.Rect(0, 0, settings.block_size, settings.block_size))

    # Start top of screen and go to bottom
    for i in range(0, settings.screen_height, settings.block_size):

        # Container to hold boolean values of if block occupied
        isFilled = True

        # Adjust y-coordinate position of test rect
        testRect.rect.top = i

        # Cycle through x-rect positions
        for j in range(150, settings.game_screen_width, settings.block_size):

            # Adjust x-coordinate position of test rect
            testRect.rect.left = j 

            if not pg.sprite.spritecollideany(testRect, LoB):
                isFilled = False

        # If all squares filled, add y-coordinate to list and remove pieces from ListOfBlocks
        if isFilled:
            ListOfClearedLines.append(i)
            for piece in LoB[:]:
                if piece.rect.top == i:
                    LoB.remove(piece)

    # Update number of cleared lines this level
    update_num_lines_cleared(stats, len(ListOfClearedLines))

    # Update points
    update_points(stats, len(ListOfClearedLines), texts)

    # If lines were cleared, drop lines
    if ListOfClearedLines:
        sounds.play_line_cleared()
        drop_lines(settings, ListOfClearedLines, LoB)

def drop_lines(settings, ListOfClearedLines, LoB):
    """Drop lines above cleared lines"""
    # Cycle through y-values of cleared lines
    for i in range(len(ListOfClearedLines)):

        # If piece is above cleared line y-value, drop piece one row
        for piece in LoB:
            if piece.rect.top < ListOfClearedLines[i]:
                piece.rect.top += settings.block_size
                
def check_ceiling(stats, sounds, LoB):
    """Check if pieces are past top of screen"""
    # Check all pieces
    for piece in LoB:

        # Quit game if piece has reached top
        if piece.rect.top < 0:
            sounds.stop_sounds(); sounds.play_game_over()
            stats.game_active, stats.ask_if_scoreboard, stats.restart = False, True, True
            pg.mouse.set_visible(True)
            

def update_num_lines_cleared(stats, numClearedLines):
    """Add to total lines cleared this level"""
    if numClearedLines == 1:
        stats.lines_cleared += 1
    elif numClearedLines == 2:
        stats.lines_cleared += 3
    elif numClearedLines == 3:
        stats.lines_cleared += 5
    elif numClearedLines >= 4:
        stats.lines_cleared += 8

def update_points(stats, numClearedLines, texts):
    """Add points to players score"""
    if numClearedLines == 1:
        stats.points += 50 * (stats.level + 1)

    elif numClearedLines == 2:
        stats.points += 120 * (stats.level + 1)

    elif numClearedLines == 3:
        stats.points += 200 * (stats.level + 1)

    elif numClearedLines == 4:
        stats.points += 400 * (stats.level + 1)

    texts.get("score_num_text").text = str(stats.points).zfill(6)
    texts.get("score_num_text").prep_text(str(stats.points).zfill(6))

def update_level(stats, texts):
    """Update level and associated stats"""
    # Add one to level
    stats.level += 1

    if stats.level % 10 == 0:
        stats.move_delay -= 4

    newLevel = str(stats.level).zfill(2)
    texts.get("level_num_text").text = newLevel
    texts.get("level_num_text").prep_text(newLevel)

    stats.temp_speed -= 2

    if not stats.piece_dropping:
        stats.block_speed = stats.temp_speed

    # Reset lines cleared per level
    stats.lines_cleared -= stats.lines_per_level

    stats.lines_per_level += 3

def update_screen(settings, stats, screen, menu, texts, block, LoB, ghost_block):
    """Update new game stats to screen"""
    menu.draw_outline()
    
    render_ghost_block(settings, screen, block, LoB, ghost_block)

    # Draw player block
    block.draw_block()

    # Draw all pieces in ListOfBlocks
    for piece in LoB:
        piece.draw_piece()


    # Draw next piece image
    render_next_block(settings, screen, stats)

    render_hold_block(settings, screen, stats)

    texts.get("level_num_text").draw_text()
    texts.get("score_num_text").draw_text()

def render_ghost_block(settings, screen, block, LoB, ghost_block):
    ghost_block.reset(settings, block, LoB)
    ghost_block.draw_block()

def render_next_block(settings, screen, stats):
    """Render next block inside box"""
    # Pull image depending on queued data type
    if type(stats.next_block) == Long_Block:
        image = settings.block_img[0]

    elif type(stats.next_block) == Square_Block:
        image = settings.block_img[1]

    elif type(stats.next_block) == Z_Block:
        image = settings.block_img[2]

    elif type(stats.next_block) == S_Block:
        image = settings.block_img[3]

    elif type(stats.next_block) == Left_L_Block:
        image = settings.block_img[4]

    elif type(stats.next_block) == Right_L_Block:
        image = settings.block_img[5]

    elif type(stats.next_block) == T_Block:
        image = settings.block_img[6]
        
    # Create rect and center within box
    rect = image.get_rect()
    rect.center = (525, 250)

    # Blit image to screen
    screen.blit(image, rect)

def render_hold_block(settings, screen, stats):
    """Render next block inside box"""
    # Pull image depending on queued data type
    if type(stats.hold_block) == type(None):
        return

    elif type(stats.hold_block) == Long_Block:
        image = settings.block_img[0]

    elif type(stats.hold_block) == Square_Block:
        image = settings.block_img[1]

    elif type(stats.hold_block) == Z_Block:
        image = settings.block_img[2]

    elif type(stats.hold_block) == S_Block:
        image = settings.block_img[3]

    elif type(stats.hold_block) == Left_L_Block:
        image = settings.block_img[4]

    elif type(stats.hold_block) == Right_L_Block:
        image = settings.block_img[5]

    elif type(stats.hold_block) == T_Block:
        image = settings.block_img[6]
        
    # Create rect and center within box
    rect = image.get_rect()
    rect.center = (75, 125)

    # Blit image to screen
    screen.blit(image, rect)

def validate_spawn(settings, block, LoB):
    while pg.sprite.groupcollide(block.pieces, LoB, False, False):
        for piece in block.pieces:
            piece.rect.top -= settings.block_size