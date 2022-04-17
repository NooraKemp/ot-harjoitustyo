import pygame
from get_image import get_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, col=0, row=0, health=50):
        super().__init__()

        self.image = get_image(color + '_alien.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row

        self.health = health
        self.last_shoot_time = 0

    def enemy_moving_to_direction(self, direction):
        self.rect.x += direction

    def enemy_can_shoot_laser(self, time):
        if time-self.last_shoot_time < 800:
            return False
        return True
