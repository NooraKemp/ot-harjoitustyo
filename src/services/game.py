import pygame
from sprites.background import Background
from sprites.spaceship import Spaceship

class Game:
    def __init__(self):
        self.spaceship = None
        self.background = None
        self.all_sprites = pygame.sprite.Group()
        self.initialize_sprites()

    def move_spaceship(self, dx=0, dy=0):
        self.spaceship.rect.move_ip(dx,dy)

    def initialize_sprites(self):
        self.spaceship = Spaceship(500,700)
        self.background = Background(0,0)

        self.all_sprites.add(
            self.background,
            self.spaceship
        )
