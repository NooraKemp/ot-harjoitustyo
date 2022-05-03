import pygame
from get_image import get_image


class Enemy(pygame.sprite.Sprite):
    """A class that represents the enemy.

    Atributes:
        self.image: Image of the enemy.
        self.width: Width of the image.
        self.height: Height of the image.
        self.health: Health of the enemy.
        self.last_shoot_time: The time when the enemy last shot laser.
    """

    def __init__(self, color, col=0, row=0, health=1):
        '''A constructor that creates new enemy.'''
        super().__init__()

        self.image = get_image(color + '_alien.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row

        self.health = health
        self.last_shot_time = 0

    def enemy_moving_to_direction(self, direction):
        '''A method that moves enemy to given direction'''
        self.rect.x += direction

    def enemy_can_shoot_laser(self, time):
        '''Checks if enough time has elapsed since the previous shot.

        Returns: True, if enemy can shoot laser, otherwise False.'''
        if time-self.last_shot_time < 800:
            return False
        return True
