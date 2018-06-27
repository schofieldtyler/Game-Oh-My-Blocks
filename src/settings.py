class Settings():
    """A class to store the settings for the game"""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings.
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (66, 66, 66)

        # Bullet settings.
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 30
        self.bullet_speed_factor = 3

        # Block settings.
        self.block_width = 30
        self.block_height = 30
        self.block_color = 255, 255, 255