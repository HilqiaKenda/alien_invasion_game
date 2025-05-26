import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, alien_invas):
        """Initialize the ship and set its starting position"""
        self.screen = alien_invas.screen
        self.screen_rect = alien_invas.screen.get_rect()

        # Load he ship Image
        self.image_load = pygame.image.load("images/ship2.png")
        # original_image = pygame.image.load("images/ship2.png")
        self.image = pygame.transform.scale(self.image_load, (100, 180))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
