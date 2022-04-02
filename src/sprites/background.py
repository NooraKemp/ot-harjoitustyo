import pygame


from get_image import get_image


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = get_image("space.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
