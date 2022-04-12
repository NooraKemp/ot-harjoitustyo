import pygame
from sprites.background import Background
from sprites.spaceship import Spaceship
from sprites.enemy import Enemy
from sprites.laser import Laser


class Game:
    def __init__(self):
        self.spaceship = None
        self.background = None
        self.lasers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_moving_direction = 1
        self.sprites = pygame.sprite.Group()
        self.initialize_sprites()

    def move_spaceship(self, col=0, row=0):
        if not self.spaceship_can_move(col, row):
            return

        self.spaceship.rect.move_ip(col, row)

    def spaceship_can_move(self, col=0, row=0):
        self.spaceship.rect.move_ip(col, row)

        if self.spaceship.rect.x < 0:
            self.spaceship.rect.move_ip(-col, -row)
            return False
        if self.spaceship.rect.x + self.spaceship.width > 1000:
            self.spaceship.rect.move_ip(-col, -row)
            return False

        self.spaceship.rect.move_ip(-col, -row)
        return True

    def spaceship_shoot_laser(self, time):
        if self.spaceship.spaceship_can_shoot_laser(time):
            self.lasers.add(Laser(self.spaceship.rect.x +
                                  self.spaceship.width/2, self.spaceship.rect.y-20))
            self.spaceship.last_shoot_time = time

    def move_spaceship_lasers(self, col=0, row=0):
        for laser in self.lasers:
            laser.rect.move_ip(col, row)
            if laser.rect.y < 0:
                self.lasers.remove(laser)

    def enemies_set_up(self, color='red', col=100, row=100):
        for j in range(4):
            for i in range(8):
                self.enemies.add(Enemy(color, col, row))
                col += 100 + i
            row += 70 + j
            col = 100
            if color == 'red':
                color = 'green'
            elif color == 'green':
                color = 'yellow'
            elif color == 'yellow':
                color = 'red'

    def move_enemies(self):
        self.enemies_change_direction()
        for enemy in self.enemies:
            enemy.enemy_moving_to_direction(self.enemy_moving_direction)

    def enemies_change_direction(self):
        for enemy in self.enemies:
            if enemy.rect.x + enemy.width >= 1000:
                self.enemy_moving_direction = -1
                self.enemies_move_down()
            elif enemy.rect.x <= 0:
                self.enemy_moving_direction = 1
                self.enemies_move_down()

    def enemies_move_down(self):
        for enemy in self.enemies:
            enemy.rect.y += 2

    def game_is_over(self):
        for enemy in self.enemies:
            if enemy.rect.y >= 800 - enemy.height:
                return True

        return False

    def initialize_sprites(self):
        self.spaceship = Spaceship(500, 700)
        self.background = Background(0, 0)
        self.enemies_set_up()

        self.sprites.add(
            self.background,
            self.spaceship,
            self.enemies
        )
