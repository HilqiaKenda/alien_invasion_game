import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, alien_inva):
        """Initialize aliens and set up """
        super.__init__()
        self.screen = alien_inva.screen
        # self.screen_rect = alien_inva.screen.get_rect()

        self.image_load = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image_load, (100, 180))

        self.rectangle = self.image.get_rect()

        self.rectangle.x = self.screen_rect.width
        self.rectangle.y = self.screen_rect.height

    def blitme(self):
        """Draw alien in the screen"""
        self.screen.blit(self.image, self.rect)
