import sys

import pygame
from bullet import Bullet
from block import Block


def update_screen(settings, screen, play_button, blocks, ship, bullets):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(settings.bg_color)

    # TODO play button
    # play_button.draw_button()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouseline(settings, screen, ship, mouse_x, mouse_y)

    # check if we need to continue adding bullets for a burst
    if settings.bullet_burst and settings.bullet_burst_firing:
        # slow down the burst by it's rate
        if settings.bullet_burst_rate_remaining > 0:
            settings.bullet_burst_rate_remaining -= 1
        else:
            # fire bullet and reset rate
            fire_bullet_burst(settings, screen, ship, bullets)
            settings.bullet_burst_rate_remaining = settings.bullet_burst_rate

    # Redraw all bullets, behind ship and blocks.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

        # Redraw all blocks
    for block in blocks.sprites():
        block.draw_block()
        # block.update()

    # ship.center -= 1
    # ship.rect.centerx = ship.center
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def mouseline(settings, screen, ship, mouse_x, mouse_y):
    """ draw a line to the mouse pos """
    pygame.draw.line(screen, (0, 0, 255), (mouse_x, mouse_y),
                     (ship.rect.centerx, ship.rect.centery))

    # basic height loop until i can follow the line with proper dots
    px = 0
    while px < mouse_x:
        pygame.draw.circle(screen, (55, 55, 255), [px, mouse_y], 5)
        px+=20

    py = 0
    while py < mouse_y:
        pygame.draw.circle(screen, (55, 55, 255), [mouse_x, py], 5)
        py+=20

def check_events(settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse interaction")
            fire_bullet(settings, screen, ship, bullets)


def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.

    # TODO remove ship movement
    ship.center -= 10
    ship.rect.centerx = ship.center
    ship.blitme()

    if settings.bullet_burst and (settings.bullet_burst_firing != True):
        # burst fire
        if settings.bullet_burst_multiple or len(bullets) == 0:
            print("burst")
            settings.bullet_burst_firing = True
            # as we are starting a new burst, reset remaining to total
            settings.bullet_burst_remaining = settings.bullet_burst_total

            # most bullets fired in screen update but we need to call the first
            fire_bullet_burst(settings, screen, ship, bullets)

    else:
        print("not burst")
        if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)
            print("bullet", new_bullet.rect)


def fire_bullet_burst(settings, screen, ship, bullets):
    """Fire a burst bullet, if limit not reached yet."""
    print("Firing burst", settings.bullet_burst_remaining,
          "of", settings.bullet_burst_total)

    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
        settings.bullet_burst_remaining -= 1
        if settings.bullet_burst_remaining == 0:
            settings.bullet_burst_firing = False


def update_bullets(settings, screen, ship, blocks, bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            print("bullet out of bounds", len(bullets))
            bullets.remove(bullet)
            if len(bullets) == 0:
                print("no more bullets")
                update_level(settings, screen, blocks)

    check_bullet_block_collisions(settings, screen, ship, blocks, bullets)


def check_bullet_block_collisions(settings, screen, ship,
                                  blocks, bullets):
    """Respond to bullet-block collisions."""
    # Remove any bullets and blocks that have collided.
    collisions = pygame.sprite.groupcollide(bullets, blocks, True, False)

    # groupcollide using true will remove items

    if collisions:
        for blocks_hit in collisions.values():
            print("HIT", len(blocks), len(blocks_hit))
            for block in blocks_hit:
                block.value -= 1
                block.prep_msg()
                if block.value <= 0:
                    blocks.remove(block)

            # stats.score += ai_settings.block_points * len(blocks)
            # sb.prep_score()
        # check_high_score(stats, sb)

def update_level(settings, screen, blocks):
    """ once we have expended our bullets, move the level down toward the player """
    print("moving level/blocks down") 
    for block in blocks.sprites():
        # check whether the level has reached the player, ending the game
        if block.update_level() == False:
            # we have lost
            ship_collision()

def ship_collision():
    """ the level has reached the player, ending the game """
    print("TODO: die - end level")

def next_level():
    """ start the new level, or a new one if there was no previous level """
    # TODO: start a new level
    # clean up old elements
    # increment level
    # track stats
    # increase level specifc increments (speed etc)
    # start level