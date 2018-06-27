import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as game
from button import Button
from ship import Ship
from block import Block


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Oh My Blocks")


# Make the Play button.
    play_button = Button(settings, screen, "Play")

    #play_block = Block(settings, screen)

# Make a ship, a group of bullets.
    ship = Ship(settings, screen)
    bullets = Group()
    blocks = Group()

    # make some blocks for now
    # TODO implement this in levels
    """
    n = 4
    a = [0] * n
    a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
    for row in a:
    	print(row[0])
    	new_block = Block(settings, screen, str(100 * row[0]), 0, 0 )
    	blocks.add(new_block)
        #print(' '.join([str(elem) for elem in row]))
"""
    level = [0, 1, 3, 0, 4, 5, 6]

    for b in level:
        print(b)        
        new_block = Block(settings, screen, b*50, 0, b)
        blocks.add(new_block)

    while True:

        game.check_events(settings, screen, ship, bullets)
        game.update_bullets(settings, screen, ship, blocks, bullets)
        game.update_screen(settings, screen, play_button,
                           blocks, ship, bullets)


run_game()
