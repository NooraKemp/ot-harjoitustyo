import unittest
from repositories.leaderboard_repository import leaderboard_repository
from sprites.spaceship import Spaceship


class TestLeaderboarRepository(unittest.TestCase):
    '''A class for the leaderboar repository tests.'''
    def setUp(self):
        leaderboard_repository.delete_all()
        self.spaceship = Spaceship(500, 700)
        self.spaceship.points = 10

    def test_create_new_score(self):
        leaderboard_repository.create_new_score(
            'player', self.spaceship.points)
        score = leaderboard_repository.find_high_score()
        self.assertEqual(score[0], 10)
