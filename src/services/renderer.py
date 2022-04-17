import pygame
pygame.font.init()


class Renderer:
    """ A class that renders the game view"""

    def __init__(self, display, game):
        self.display = display
        self.game = game
        self.font = pygame.font.SysFont('Helvetica', 18)
        self.points = 0
        self.high_score = 0
        self.lives = 0

    def render(self):
        self.game.sprites.draw(self.display)
        self.game.spaceship_lasers.draw(self.display)
        self.game.enemy_lasers.draw(self.display)
        self.game.enemies.draw(self.display)
        self.points = self.font.render(
            f'POINTS: {self.game.spaceship.points}', False, (255, 255, 255))
        self.lives = self.font.render(
            f'LIVES: {self.game.spaceship.lives}', False, (255, 255, 255))
        self.high_score = self.font.render(
            f'HIGH SCORE: {self.game.high_score}', False, (255, 255, 255))
        self.display.blit(self.points, (10, 10))
        self.display.blit(self.lives, (10, 30))
        self.display.blit(self.high_score, (800, 10))
        pygame.display.update()
