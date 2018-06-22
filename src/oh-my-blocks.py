import pygame
from settings import Settings
import game_functions as game

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()	

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
    pygame.display.set_caption("Oh My Blocks")

    while True:
        game.check_events(settings, screen)
        game.update_screen(settings, screen)

run_game()