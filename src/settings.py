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
        # Bullet burst firing settings
        self.bullet_burst = True
        self.bullet_burst_firing = False
        # Do we allow multiple bursts at once
        self.bullet_burst_multiple = False
        self.bullet_burst_total = 3
        self.bullet_burst_remaining = 3
        # Interval between bullets when bursting
        self.bullet_burst_rate = 30
        self.bullet_burst_rate_remaining = 5

        # Block settings.
        self.block_width = 30
        self.block_height = 30
        self.block_color = 255, 255, 255
