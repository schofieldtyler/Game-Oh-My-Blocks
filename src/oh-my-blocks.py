import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as game
from button import Button
from ship import Ship
# TODO remove block import once demo blocks are done
from block import Block
from level import Level
import spritesheet


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()
    clock = pygame.time.Clock()
    clock.tick(60)

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Oh My Blocks")

   
# Make the Play button.
    play_button = Button(settings, screen, "Play")

# Make a ship, a group of bullets and blocks.
    ship = Ship(settings, screen)
    bullets = Group()
    blocks = Group()

    # TODO flesh this out in in levels

    level = Level(settings, screen, blocks)
    level.getLevel()

    # TODO remove testing block
    new_block = Block(settings, screen, 280, 0, 50)
    blocks.add(new_block)

    while True:

        game.check_events(settings, screen, ship, bullets)
        game.update_bullets(settings, screen, ship, blocks, bullets)
        game.update_screen(settings, screen, play_button,
                           blocks, ship, bullets)


run_game()
