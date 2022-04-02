import unittest
from services.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def assert_placement_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_spaceship_can_move(self):
        spaceship = self.game.spaceship

        self.assert_placement_equal(spaceship, 500, 700)

        self.game.move_spaceship(dx=-15)
        self.assert_placement_equal(spaceship, 500-15, 700)

        self.game.move_spaceship(dx=15)
        self.assert_placement_equal(spaceship, 500, 700)

    def test_spaceship_cant_move_outside_screen(self):
        spaceship = self.game.spaceship

        self.game.move_spaceship(dx=-600)
        self.assert_placement_equal(spaceship, 500, 700)
