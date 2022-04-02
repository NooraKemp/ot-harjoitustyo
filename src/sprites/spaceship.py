import pygame
from get_image import get_image


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = get_image("spaceship.png")
        self.width = self.image.get_width()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
