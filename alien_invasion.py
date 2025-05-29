import sys
import pygame
from aliens import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game asset and behaviors"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()

        # Screen settigs
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien = Alien(self)

        self.moving_right = False
        self.moving_left = False

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._get_ride_of_bullet()
            self._updat_screen()
            self.alien.blitme

    def _get_ride_of_bullet(self):
        """Remove fired bullets after reaching to the top"""
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self._check_keydown_event(event)
            self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Respond to keypress down"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True

            elif event.key == pygame.K_q:
                sys.exit()

            elif event.key == pygame.K_SPACE:
                self.bullet = Bullet(self).fire_bullet
                self.bullet = True

    def _check_keyup_event(self, event):
        """Respond to key up"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_SPACE:
                # self.fire_bullet = False
                self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the new bullet group"""
        if len(self.bullets) < self.settings.bulltes_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # print("bullet fired")

    def _updat_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
