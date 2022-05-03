import pygame


class Laser(pygame.sprite.Sprite):
    """A class that represents the laser.

    Atributes:
        self.image: Laser surfase..
        self.color: Color of the laser."""

    def __init__(self, col=0, row=0):
        '''A constructor that creates new laser.'''

        super().__init__()

        self.image = pygame.Surface((4, 20))
        self.color = (250, 250, 250)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
