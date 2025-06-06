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
        self.aliens = pygame.sprite.Group()
        print("Please select the screen mode to play the game 'any to quit'")
        print("\t1. Fullscreen mode\n\t2. adjust mode")
        self.screen_size = int(input("Enter your screen size mode (1 or 2): "))
        self.screen = ''

        # Screen settigs
        if self.screen_size == 1:
            # Fullscreen
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        elif self.screen_size == 2:
            # Screen size 1900 x 1300
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))

        else:
            sys.exit()

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self._create_alien_fleet()
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
            self._update_alien()
            self._get_ride_of_bullet()
            self._updat_screen()

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

    def _create_alien_fleet(self):
        """Create the fllet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - \
            (2 * alien_width)
        number_of_alien_x = available_space_x // (
            2 * alien_width)

        # Detrimining number of rows of aleins that fit on the screen
        ship_height = self.ship.rect.height
        avaalable_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_of_rows = avaalable_space_y // (3 * alien_height)

        for row_nnumber in range(number_of_rows):
            for alien_number in range(number_of_alien_x + 1):
                self._create_alien(alien_number, row_nnumber)

    def _create_alien(self, number_of_alien, row_nnumber):
        """Create aliens and place it in a row"""
        # Create first row of alien fleet
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Get available space of with of the game board
        alien.x = alien_width + 2 * alien_width * number_of_alien
        alien.rect.x = alien.x

        # Get available space of height of the game board
        alien.y = alien_height + 2 * alien_height * row_nnumber
        alien.rect.y = alien.y

        self.aliens.add(alien)

    def _updat_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # make the most recently drawn screen visible
        pygame.display.flip()

    def _update_alien(self):
        """ Update the positions of all aliens in the fleet. """
        self.alien.update()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.screen_size
    alien_invasion.run_game()
