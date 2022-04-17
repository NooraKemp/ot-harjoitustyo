from random import choice
import pygame
from sprites.background import Background
from sprites.spaceship import Spaceship
from sprites.enemy import Enemy
from sprites.laser import Laser
from repositories.leaderboard_repository import (
    leaderboard_repository as default_leaderboard_repository)


class Game:
    def __init__(self, leaderboar_repository=default_leaderboard_repository):
        self.spaceship = None
        self.background = None
        self.spaceship_lasers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_moving_direction = 1
        self.enemy_lasers = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()

        self._leaderboard_repository = leaderboar_repository
        self.high_score = self._leaderboard_repository.find_high_score()

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
            self.spaceship_lasers.add(Laser(self.spaceship.rect.x +
                                            self.spaceship.width/2, self.spaceship.rect.y-20))
            self.spaceship.last_shoot_time = time

    def move_all_lasers(self, col=0, row=0):
        for laser in self.spaceship_lasers:
            laser.rect.move_ip(col, row)
            for enemy in self.enemies:
                colliding_spaceship_lasers = self.get_colliding_lasers(
                    enemy, self.spaceship_lasers)
                if colliding_spaceship_lasers:
                    self.enemies.remove(enemy)
                    self.spaceship.points += 10
            if laser.rect.y < 0:
                self.spaceship_lasers.remove(laser)
        for laser in self.enemy_lasers:
            laser.rect.move_ip(col, -row)
            colliding_enemy_lasers = self.get_colliding_lasers(
                self.spaceship, self.enemy_lasers)
            if colliding_enemy_lasers:
                self.spaceship.lives -= 1
            if laser.rect.y > 800:
                self.enemy_lasers.remove(laser)

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

    def enemy_shoot_laser(self, time):
        shooting_enemy = choice(self.enemies.sprites())
        if shooting_enemy.enemy_can_shoot_laser(time):
            self.enemy_lasers.add(Laser(shooting_enemy.rect.x +
                                  shooting_enemy.width/2, shooting_enemy.rect.y +
                                  shooting_enemy.height))
            for enemy in self.enemies:
                enemy.last_shoot_time = time

    def get_colliding_lasers(self, sprite, lasers):
        return pygame.sprite.spritecollide(sprite, lasers, True)

    def game_is_over(self):
        for enemy in self.enemies:
            if enemy.rect.y >= 800 - enemy.height:
                self._leaderboard_repository.create_new_score(
                    'player', self.spaceship.points)
                return True
        if self.spaceship.lives <= 0:
            # Tämä tulostaa 0 eli aiemmat tulokset eivät ole tietokannassa
            self.all = self._leaderboard_repository.find_all()
            print(len(self.all))

            self._leaderboard_repository.create_new_score(
                'player', self.spaceship.points)

            self.all = self._leaderboard_repository.find_all()
            # Tässä kohtaa tulostaa 1 eli muka tallentuu tietokantaan
            print(len(self.all))
            return True

        return False

    def update_game(self, time):
        if len(self.enemies) < 1:
            self.enemies_set_up()
        self.enemy_shoot_laser(time)
        self.move_all_lasers(row=-4)
        self.move_enemies()

    def initialize_sprites(self):
        self.spaceship = Spaceship(500, 700)
        self.background = Background(0, 0)
        self.enemies_set_up()

        self.sprites.add(
            self.background,
            self.spaceship
        )
