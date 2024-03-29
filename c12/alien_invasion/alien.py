import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien on the fleet"""

    def __init__(self, ai_game) -> None:
        """Init class of Alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("c12/alien_invasion/img/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.settings = ai_game.settings

        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
