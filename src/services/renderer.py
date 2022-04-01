import pygame

class Renderer:
    """ A class that renders the game view"""
    def __init__(self, display, game):
        self.display = display
        self.game = game

    def render(self):
        self.game.all_sprites.draw(self.display)
        pygame.display.update()