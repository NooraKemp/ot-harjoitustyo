import pygame


from get_image import get_image


class Background(pygame.sprite.Sprite):
    def __init__(self, col, row):
        super().__init__()

        self.image = get_image("space.png")

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
