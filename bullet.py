import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullet fire from the ship"""

    def __init__(self, inav_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = inav_game.screen
        self.settings = inav_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = inav_game.ship.rect.midtop

        # Store the bullet's position as a decimal
        self.y_position = float(self.rect.y)

    def update(self):
        """Move the bulet up the screen"""

        self.y_position -= self.settings.bullet_speed
        self.rect.y = self.y_position

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        print("bullet has been draw")
