import pygame
import pygame.font
from pygame.sprite import Sprite
from color_constants import colors
from color_constants import RGB as RGB


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

        self.colors = list(colors.items())
        # print(self.colors[0])
        # print(self.colors[0][1].red)

        # Store a decimal value for the block's position.
        self.x = float(self.rect.x)

        self.color = settings.block_color
        self.font = pygame.font.SysFont(None, 48)

        self.value = value;

        # The block message only needs to be prepped once.
        self.prep_msg()


    def update_level(self):
        """Move the block down the screen."""
        
        # TODO move block down a specified amount from SETTINGS
        self.rect.top += 100
        self.prep_msg() # need to redraw the text/bg or it gets left behind
        

    def draw_block(self):
        """Draw the block to the screen."""
        self.screen.fill(self.block_color, self.rect)
        self.screen.blit(self.value_image, self.value_image_rect)

    def prep_msg(self):
        """Turn the current value of the block into a rendered image,
         and center text on the button."""

        #self.block_color = (self.value*40, self.value*40, self.value*40)
        self.block_color = (self.colors[int(self.value)][1].red,
                            self.colors[int(self.value)][1].blue,
                            self.colors[int(self.value)][1].green)
        self.text_color = (255, 0, 255)

        self.value_image = self.font.render(str(self.value), True, self.text_color, self.block_color)
        self.value_image_rect = self.value_image.get_rect()
        self.value_image_rect.center = self.rect.center


