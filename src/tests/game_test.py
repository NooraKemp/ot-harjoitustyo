import unittest
from services.game import Game
from sprites.enemy import Enemy


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def assert_placement_equal(self, sprite, col, row):
        self.assertEqual(sprite.rect.x, col)
        self.assertEqual(sprite.rect.y, row)

    def test_spaceship_can_move(self):
        self.assert_placement_equal(self.game.spaceship, 500, 700)

        self.game.move_spaceship(col=-15)
        self.assert_placement_equal(self.game.spaceship, 500-15, 700)

        self.game.move_spaceship(col=15)
        self.assert_placement_equal(self.game.spaceship, 500, 700)

    def test_spaceship_cant_move_outside_screen(self):
        self.game.move_spaceship(col=-600)
        self.assert_placement_equal(self.game.spaceship, 500, 700)

        self.game.move_spaceship(col=600)
        self.assert_placement_equal(self.game.spaceship, 500, 700)

    def test_spaceship_can_move_returs_correct_value(self):
        self.assertEqual(self.game.spaceship_can_move(col=-600), False)
        self.assertEqual(self.game.spaceship_can_move(col=-600), False)
        self.assertEqual(self.game.spaceship_can_move(col=-15), True)
        self.assertEqual(self.game.spaceship_can_move(col=-15), True)

    def test_spaceship_shoots_laser(self):
        self.game.spaceship_shoot_laser(1000)
        self.assertEqual(len(self.game.lasers), 1)

    def test_spaceship_can_shoot_laser_returs_correct_value(self):
        self.assertEqual(
            self.game.spaceship.spaceship_can_shoot_laser(1000), True)
        self.assertEqual(
            self.game.spaceship.spaceship_can_shoot_laser(1), False)

    def test_spaceship_lasers_can_move(self):
        self.game.spaceship_shoot_laser(1000)
        self.game.move_spaceship_lasers(row=-10)
        for laser in self.game.lasers:
            self.assertEqual(laser.rect.y, self.game.spaceship.rect.y-20-10)
        self.game.move_spaceship_lasers(row=-800)
        self.assertEqual(len(self.game.lasers), 0)

    def test_move_enemies(self):
        self.game.move_enemies()
        self.assertEqual(self.game.enemy_moving_direction, 1)

    def test_enemies_change_moving_direction(self):
        i = 1
        while i <= 150:
            self.game.move_enemies()
            i += 1
        self.assertEqual(self.game.enemy_moving_direction, -1)
        i = 1
        while i <= 300:
            self.game.move_enemies()
            i += 1
        self.assertEqual(self.game.enemy_moving_direction, 1)
