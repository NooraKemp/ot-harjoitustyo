import pygame


from get_image import get_image


class Background(pygame.sprite.Sprite):
    """A class that represents the background image.

    Attributes:
        self.image: Background image.
    """

    def __init__(self, col, row):
        '''A constructor that loads backround image and defines it's position on screen.'''

        super().__init__()

        self.image = get_image("space.png")

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
