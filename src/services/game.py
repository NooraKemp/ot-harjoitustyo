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
        if not self.spaceship_can_move(dx, dy):
            return

        self.spaceship.rect.move_ip(dx, dy)

    def spaceship_can_move(self, dx=0, dy=0):
        self.spaceship.rect.move_ip(dx, dy)

        if self.spaceship.rect.x < 0:
            self.spaceship.rect.move_ip(-dx, -dy)
            return False
        if self.spaceship.rect.x + self.spaceship.width > 1000:
            self.spaceship.rect.move_ip(-dx, -dy)
            return False

        self.spaceship.rect.move_ip(-dx, -dy)
        return True

    def initialize_sprites(self):
        self.spaceship = Spaceship(500, 700)
        self.background = Background(0, 0)

        self.all_sprites.add(
            self.background,
            self.spaceship
        )
