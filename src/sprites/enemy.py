import pygame
from get_image import get_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, col=0, row=0):
        super().__init__()

        self.image = get_image(color + '_alien.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row

    def enemy_moving_to_direction(self, direction):
        self.rect.x += direction
