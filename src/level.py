import pygame
from pygame.sprite import Sprite
from block import Block


class Level(Sprite):

    def __init__(self, settings, screen, blocks):
        """Initialize the level, and set its starting position."""
        super(Level, self).__init__()
        self.screen = screen
        self.settings = settings
        self.blocks = blocks

        # self.screen_rect = screen.get_rect()

        print("level init")

    def center_level(self):
        """Center the level on the screen."""
        self.center = self.screen_rect.centerx

    def blitme(self):
        """Draw the level at its current location."""
        self.screen.blit(self.rect)

    def getLevel(self):
        """ build blocks to screen based on current level """
        # TODO: level selection/input
        level = level_1

        rownum = 0        
        for row in level:
            rownum += 1
            print(rownum)
            colnum = 0
            for col in row:
                colnum += 1
                if col > 0:
                    new_block = Block(self.settings, self.screen, colnum * (self.settings.block_col_spacing), rownum * (self.settings.block_row_spacing), col)
                    self.blocks.add(new_block)


# Levels
level_1 = [
    [0, 1, 3, 2, 4, 0, 27, 9, 7, 6, 3, 5],
    [1, 3, 4, 2, 8, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 3, 2, 0, 0, 1, 4, 3, 2, 1, 0],
]

level_2 = [
    [2, 2, 2, 2, 4, 9, 1],
    [2, 2, 2, 2, 8, 9, 1]
]
