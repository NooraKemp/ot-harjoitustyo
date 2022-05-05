import pygame


class GameLoop:
    """ A class that runs the gameloop.

    Attributes:
        self.game: Game object.
        self.renderer: Renderer object.
        self.clock: Clock object.
        self.event_queue: EventQueue
        self.time: Game duration time.
        self.show_main: Boolean value that determines wheather the main manu view is displayed.
        self.show_game: Boolean value that determines wheather the game view is displayed.
        self.show_game_over: Boolean value that determines wheather the game over view is displayed.
    """

    def __init__(self, game, renderer, clock, event_queue):
        '''A constructor that creates new gameloop.'''
        self.game = game
        self.renderer = renderer
        self.clock = clock
        self.event_queue = event_queue
        self.time = 0
        self.mouse = ''
        self.show_main = True
        self.show_game = False
        self.show_game_over = False

    def run(self):
        while True:
            if self._events() is False:
                break

            if self.show_main is True:
                self.main_menu()
            if self.show_game is True:
                self.run_game()
            if self.show_game_over is True:
                self.game_over()

    def main_menu(self):
        '''Shows main many view.'''
        self.mouse = pygame.mouse.get_pos()
        self.renderer.render_main_menu()

    def run_game(self):
        '''Shows game view.'''
        self.time = self.clock.get_ticks()
        self.game.update_game(self.time)
        self.renderer.render_game()

        if self.game.game_is_over() is True:
            self.show_game = False
            self.show_game_over = True

        self.clock.tick(60)

    def game_over(self):
        '''Shows game over view.'''
        self.mouse = pygame.mouse.get_pos()
        self.renderer.render_game_over()

    def _events(self):
        for event in self.event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.move_spaceship(col=-15)
                if event.key == pygame.K_RIGHT:
                    self.game.move_spaceship(col=15)
                if event.key == pygame.K_SPACE:
                    self.game.spaceship_shoot_laser(self.time)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= self.mouse[0] <= 650 and 300 <= self.mouse[1] <= 360:
                    if self.game.game_is_over() is True:
                        self.game.reset_game()
                    self.show_main = False
                    self.show_game_over = False
                    self.show_game = True
                if 350 <= self.mouse[0] <= 650 and 400 <= self.mouse[1] <= 450:
                    return False
                if 350 <= self.mouse[0] <= 650 and 500 <= self.mouse[1] <= 550:
                    self.show_main = True
                    self.show_game_over = False
            elif event.type == pygame.QUIT:
                return False
