import pygame
from event_queue import EventQueue
from services.clock import Clock
from services.game import Game
from services.game_loop import GameLoop
from services.renderer import Renderer


def main():
    width = 1000
    height = 800
    display = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Space Invaders")
    game = Game()
    renderer = Renderer(display, game)
    clock = Clock()
    event_queue = EventQueue()
    game_loop = GameLoop(game, renderer, clock, event_queue)

    pygame.init()
    game_loop.run()


if __name__ == '__main__':
    main()
