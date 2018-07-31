import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired """

    def __init__(self, settings, screen, ship):
        """Create a bullet object, at the current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(
            0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        # TODO tweak bullet size
        #pygame.draw.rect(self.screen, self.color, self.rect)
        #pygame.draw.circle(self.screen, self.color, self.rect, 20, width=0)
        pygame.draw.circle(self.screen, self.color, [
                           self.rect.x, self.rect.y], 10)