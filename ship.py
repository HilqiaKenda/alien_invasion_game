import pygame
from settings import Settings


class Ship:
    """A class to manage the ship"""

    def __init__(self, alien_invas):
        """Initialize the ship and set its starting position"""
        self.screen = alien_invas.screen
        self.screen_rect = alien_invas.screen.get_rect()
        self.settings = Settings()

        # Load he ship Image
        self.image_load = pygame.image.load("images/ship2.png")
        self.image = pygame.transform.scale(self.image_load, (100, 180))

        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x_position = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # self.rect.x = self.x_position

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
