import sys

import pygame

def update_screen(settings, screen):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(settings.bg_color)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def check_events(settings, screen):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("mouse interaction");