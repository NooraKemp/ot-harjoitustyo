import pygame

pygame.font.init()


class GameOverView:
    '''A class that represents the game over view.'''

    def __init__(self, display, game):
        '''A constructor that creates new game over view.'''
        self.display = display
        self.game = game
        self.font = pygame.font.SysFont('Helvetica', 100)
        self.points_font = pygame.font.SysFont('Helvetica', 30)
        self.button_font = pygame.font.SysFont('Helvetica', 50)

    def draw_game_over_view(self):
        '''A method that draws the game over view text and buttons.'''
        self.game.sprites.draw(self.display)
        self.game_over = self.font.render(
            'GAME OVER', False, (255, 255, 255))
        self.points = self.points_font.render(
            f'YOUR SCORE: {self.game.spaceship.points}', False, (255, 255, 255))
        pygame.draw.rect(self.display, (0, 0, 0), [300, 300, 400, 60])
        self.start = self.button_font.render(
            'PLAY', False, (255, 255, 255))
        pygame.draw.rect(self.display, (0, 0, 0), [300, 400, 400, 60])
        self.quit = self.button_font.render(
            'QUIT', False, (255, 255, 255))
        pygame.draw.rect(self.display, (0, 0, 0), [300, 500, 400, 60])
        self.main_menu = self.button_font.render(
            'MAIN MENU', False, (255, 255, 255))
        self.display.blit(self.game_over, (200, 100))
        self.display.blit(self.points, (350, 210))
        self.display.blit(self.start, (450, 300))
        self.display.blit(self.quit, (450, 400))
        self.display.blit(self.main_menu, (365, 500))
