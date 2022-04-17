import unittest
import pygame

from services.game import Game
from services.game_loop import GameLoop


class StubRenderer:
    def render(self):
        pass


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self.events = events

    def get(self):
        return self.events


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_can_be_over(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        ]

        gameloop = GameLoop(
            self.game,
            StubRenderer(),
            StubClock(),
            StubEventQueue(events)
        )

        gameloop.run()

        self.assertTrue(self.game.game_is_over())
