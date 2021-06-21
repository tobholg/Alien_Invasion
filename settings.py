class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the games settings."""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed = 1.0
        self.alien_width = 50
        self.alien_height = 50
        self.alien_color = (255, 0, 0)
