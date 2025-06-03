import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, alien_inva):
        """Initialize aliens and set up """
        super().__init__()
        self.screen = alien_inva.screen
        self.settings = alien_inva.settings

        # self.screen_rect = alien_inva.screen.get_rect()
        self.image_load = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image_load, (90, 50))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x_position = float(self.rect.x)
        self.y_position = float(self.rect.y)

    def update(self):
        """"""
        self.x_position += self.settings.alien_speed
        self.rect.x = self.x_position
