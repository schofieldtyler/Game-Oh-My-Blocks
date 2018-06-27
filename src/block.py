import pygame
import pygame.font
from pygame.sprite import Sprite


class Block(Sprite):
    """A class to manage blocks fired """

    def __init__(self, settings, screen, x, y, value):
        """Create a block object, at the current position."""
        super(Block, self).__init__()
        self.screen = screen

        # Create block rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, settings.block_width,
                                settings.block_height)

        self.rect.centerx = x
        self.rect.top = y

        # TODO check difference in using centrex
        self.rect.x = x


        # Store a decimal value for the block's position.
        self.x = float(self.rect.x)

        self.color = settings.block_color

        self.block_color = (0, 0, 255)
        self.text_color = (255, 0, 255)
        self.font = pygame.font.SysFont(None, 48)

        # The block message only needs to be prepped once.
        self.prep_msg(str(value))


    def update(self):
        # TODO
        """Move the block up the screen."""
        # Update the decimal position of the block.
        #self.x -= 1
        # Update the rect position.
        #self.rect.x = self.x

    def draw_block(self):
        """Draw the block to the screen."""
        self.screen.fill(self.block_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def prep_msg(self, msg):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.block_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


