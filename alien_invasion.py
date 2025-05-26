import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game asset and behaviors"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self._updat_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 2
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 2

    def _updat_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
