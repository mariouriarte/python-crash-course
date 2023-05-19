import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien on the fleet'''

    def __init__(self, ai_game) -> None:
        '''Init class of Alien'''
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('c12/alien_invasion/img/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
