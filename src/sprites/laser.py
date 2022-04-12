import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, col=0, row=0):
        super().__init__()

        self.image = pygame.Surface((4, 20))
        self.color = (250, 250, 250)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
