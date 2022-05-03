from random import choice
import pygame
from sprites.background import Background
from sprites.spaceship import Spaceship
from sprites.enemy import Enemy
from sprites.laser import Laser
from repositories.leaderboard_repository import (
    leaderboard_repository as default_leaderboard_repository)


class Game:
    '''A class that is responsible for application logic.

    Attributes:
        self.background: Backgroud-sprite.
        self.spaceship: Spaceship-sprite.
        self.spaceship_lasers: Sprite group for spaceship lasers.
        self.enemies: Sprite group for enemies.
        self.enemy_moving_direction: The direction that enemies are movin (left or right).
        self.enemy_lasers: Sprite group for enemy lasers.
        self.sprites: Sprite group for background and spaceship.
        self._leaderboard_repository: Database for game points.
        self.high_score: The highest score in the game.
        '''

    def __init__(self, leaderboar_repository=default_leaderboard_repository):
        '''A constructor that creates new game.'''
        self.background = None
        self.spaceship = None
        self.spaceship_lasers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_moving_direction = 1
        self.enemy_lasers = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()

        self._leaderboard_repository = leaderboar_repository
        self.high_score = self._leaderboard_repository.find_high_score()

        self._initialize_sprites()

    def move_spaceship(self, col=0, row=0):
        '''Moves spaceship in the given direction.'''
        if not self.spaceship_can_move(col, row):
            return

        self.spaceship.rect.move_ip(col, row)

    def spaceship_can_move(self, col=0, row=0):
        '''Checks is spaceship can move.
        Returns: True, if spaceship can move, otherwise False.
        '''

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
        '''Creates a laser for spaceship and adds it to sprite group spaceship_lasers.'''
        if self.spaceship.spaceship_can_shoot_laser(time):
            self.spaceship_lasers.add(Laser(self.spaceship.rect.x +
                                            self.spaceship.width/2, self.spaceship.rect.y-20))
            self.spaceship.last_shoot_time = time

    def move_all_lasers(self, col=0, row=0):
        '''Moves spaceahip lasers and enemy lasers,
        checks collisions, updates points and lives,
        removes enemy if it is hit by spaseship laser.
        '''
        for laser in self.spaceship_lasers:
            laser.rect.move_ip(col, row)
            for enemy in self.enemies:
                colliding_spaceship_lasers = self._get_colliding_lasers(
                    enemy, self.spaceship_lasers)
                if colliding_spaceship_lasers:
                    self.enemies.remove(enemy)
                    self.spaceship.points += 10
            if laser.rect.y < 0:
                self.spaceship_lasers.remove(laser)
        for laser in self.enemy_lasers:
            laser.rect.move_ip(col, -row)
            colliding_enemy_lasers = self._get_colliding_lasers(
                self.spaceship, self.enemy_lasers)
            if colliding_enemy_lasers:
                self.spaceship.lives -= 1
            if laser.rect.y > 800:
                self.enemy_lasers.remove(laser)

    def enemies_set_up(self, color='red', col=100, row=100):
        '''Creates new group of enemies.'''
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
        '''Checks if enemies should change direction and moves enemies
        left or right based on current direction.
        '''
        self.enemies_change_direction()
        for enemy in self.enemies:
            enemy.enemy_moving_to_direction(self.enemy_moving_direction)

    def enemies_change_direction(self):
        '''Changes moving direction of enemies and calls enemies_move_down method,
        when enemies hit left or right side of the screen.
        '''
        for enemy in self.enemies:
            if enemy.rect.x + enemy.width >= 1000:
                self.enemy_moving_direction = -1
                self.enemies_move_down()
            elif enemy.rect.x <= 0:
                self.enemy_moving_direction = 1
                self.enemies_move_down()

    def enemies_move_down(self):
        '''Moves enemies down the screen.'''
        for enemy in self.enemies:
            enemy.rect.y += 5

    def enemy_shoot_laser(self, time):
        '''Creates a laser for random enemy and adds it to sprite group enemy_lasers.'''
        shooting_enemy = choice(self.enemies.sprites())
        if shooting_enemy.enemy_can_shoot_laser(time):
            self.enemy_lasers.add(Laser(shooting_enemy.rect.x +
                                  shooting_enemy.width/2, shooting_enemy.rect.y +
                                  shooting_enemy.height))
            for enemy in self.enemies:
                enemy.last_shot_time = time

    def _get_colliding_lasers(self, sprite, lasers):
        return pygame.sprite.spritecollide(sprite, lasers, True)

    def game_is_over(self):
        '''Checks if game is over.
        Returns: True, if lives are less than 1 or
        enemy hits the bottom of the screen, otherwise False.
        '''
        for enemy in self.enemies:
            if enemy.rect.y >= 800 - enemy.height:
                self._leaderboard_repository.create_new_score(
                    'player', self.spaceship.points)
                return True
        if self.spaceship.lives <= 0:
            self._leaderboard_repository.create_new_score(
                'player', self.spaceship.points)
            return True

        return False

    def reset_game(self):
        '''Resets game for new game.'''
        self.spaceship.rect.x = 500
        self.spaceship.rect.y = 700
        self.spaceship.points = 0
        self.spaceship.lives = 5
        self.spaceship_lasers.empty()
        self.enemies.empty()
        self.enemy_lasers.empty()
        self.high_score = self._leaderboard_repository.find_high_score()

    def update_game(self, time):
        '''Updates the game.'''
        if len(self.enemies) < 1:
            self.enemies_set_up()
        self.enemy_shoot_laser(time)
        self.move_all_lasers(row=-4)
        self.move_enemies()

    def _initialize_sprites(self):
        self.spaceship = Spaceship(500, 700)
        self.background = Background(0, 0)
        self.enemies_set_up()

        self.sprites.add(
            self.background,
            self.spaceship
        )
