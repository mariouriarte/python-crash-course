import sys
import pygame
from alien_invasion.settings import Settings

class KeyPress:
    '''A simple app to log event buttons'''

    def __init__(self) -> None:
        '''Initialize the game'''
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.settings.screen_height = 100
        self.settings.screen_width = 300

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Key event logger")

    def run_game(self):
        '''Run app'''
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''Respond to keypress and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f'You press {event}')

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    print('Hola mundo')
    key_press = KeyPress()
    key_press.run_game()
