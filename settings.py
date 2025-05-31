class Settings:
    """A class to store all the game settings"""

    def __init__(self):
        """Initialize all the game setting"""
        self.screen_width = 1900
        self.screen_height = 1300
        self.bg_color = (230, 230, 230)

        self.ship_speed = 2

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bulltes_allowed = 5
        self.bullet_color = (0, 0, 0)
