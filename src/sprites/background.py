import pygame

from get_image import get_image

class Background(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = get_image("space.png")

        self.rect = self.image.get_rect()
