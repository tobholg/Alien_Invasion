import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """ The alien class. """

    def __init__(self, ai_game):
        super()__init__():

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.alien_color
        self.rect = pygame.Rect(0, 0, self.settings.alien_width,
                                self.settings.alien_height)
        self.rect.midtop = ai_game.screen.midtop

        self.y = float(self.rect.y)
        self.starting_x = float(random.randrange(0, ai_game.settings.screen_width))

    def update(self):
        self.y += self.settings.alien_speed
        self.rect.y = self.y

    def draw_alien(self):
        # Draw the bullet to the screen.
        pygame.draw.rect(self.screen, self.color, self.rect)
