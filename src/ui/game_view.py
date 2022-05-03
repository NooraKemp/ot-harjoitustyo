import pygame

pygame.font.init()


class GameView:
    '''A class that represents the game view.'''

    def __init__(self, display, game):
        '''A constructor that creates new game view.'''
        self.display = display
        self.game = game
        self.font = pygame.font.SysFont('Helvetica', 18)

    def draw_game_view(self):
        '''A method that draws the game view sprites and text.'''
        self.game.sprites.draw(self.display)
        self.game.spaceship_lasers.draw(self.display)
        self.game.enemy_lasers.draw(self.display)
        self.game.enemies.draw(self.display)
        self.points = self.font.render(
            f'POINTS: {self.game.spaceship.points}', False, (255, 255, 255))
        self.lives = self.font.render(
            f'LIVES: {self.game.spaceship.lives}', False, (255, 255, 255))
        self.high_score = self.font.render(
            f'HIGH SCORE: {self.game.high_score[0]}', False, (255, 255, 255))
        self.display.blit(self.points, (10, 10))
        self.display.blit(self.lives, (10, 30))
        self.display.blit(self.high_score, (800, 10))
