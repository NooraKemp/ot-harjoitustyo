import unittest

from services.game import Game
from services.game_loop import GameLoop


class StubRenderer:
    def render(self):
        pass


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0


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
