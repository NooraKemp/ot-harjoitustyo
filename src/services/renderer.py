import pygame
from ui.main_menu_view import MainMenuView
from ui.game_over_view import GameOverView
from ui.game_view import GameView


class Renderer:
    """ A class that renders the views"""

    def __init__(self, display, game):
        self.display = display
        self.game = game
        self.main_manu_view = MainMenuView(self.display)
        self.game_over_view = GameOverView(self.display, self.game)
        self.game_view = GameView(self.display, self.game)

    def render_main_menu(self):
        '''A method that renders the main menu view'''
        self.game.sprites.draw(self.display)
        self.main_manu_view.draw_main_menu()
        pygame.display.update()

    def render_game(self):
        '''A method that renders the game view'''
        self.game_view.draw_game_view()
        pygame.display.update()

    def render_game_over(self):
        '''A method tht renders the game over view'''
        self.game.sprites.draw(self.display)
        self.game_over_view.draw_game_over_view()
        pygame.display.update()
