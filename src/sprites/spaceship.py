import pygame
from get_image import get_image


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, col=0, row=0, health=100):
        super().__init__()

        self.image = get_image("spaceship.png")
        self.width = self.image.get_width()

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row

        self.health = health
        self.last_shoot_time = 0

    def spaceship_can_shoot_laser(self, time):
        if time-self.last_shoot_time < 800:
            return False
        return True
