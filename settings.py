class Settings:
    """A class to store all the game settings"""

    def __init__(self):
        """Initialize all the game setting"""
        self.screen_width = 950
        self.screen_height = 1300
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
