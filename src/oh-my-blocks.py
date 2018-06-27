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

# Make a ship, a group of bullets and blocks.
    ship = Ship(settings, screen)
    bullets = Group()
    blocks = Group()

    # make some blocks for now
    # TODO implement this in levels

    level = [0, 1, 3, 2, 4, 5, 1]

    for b in level:
        print("Block value", 0)        
        if b > 0:
        	new_block = Block(settings, screen, b*50, 0, b)
        	blocks.add(new_block)

    #TODO remove testing block
    new_block = Block(settings, screen, 280, 0, 3)
    blocks.add(new_block)

    while True:

        game.check_events(settings, screen, ship, bullets)
        game.update_bullets(settings, screen, ship, blocks, bullets)
        game.update_screen(settings, screen, play_button,
                           blocks, ship, bullets)


run_game()