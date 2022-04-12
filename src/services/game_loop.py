import pygame


class GameLoop:
    """ A class that runs the gameloop """

    def __init__(self, game, renderer, clock, event_queue):
        self.game = game
        self.renderer = renderer
        self.clock = clock
        self.event_queue = event_queue
        self.time = 0

    def run(self):
        while True:
            if self.events() is False:
                break

            self.time = self.clock.get_ticks()
            self.clock.tick(60)
            self.game.move_spaceship_lasers(row=-4)
            self.game.move_enemies()
            self.render()

            if self.game.game_is_over() is True:
                break

    def events(self):
        for event in self.event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.move_spaceship(col=-15)
                if event.key == pygame.K_RIGHT:
                    self.game.move_spaceship(col=15)
                if event.key == pygame.K_SPACE:
                    self.game.spaceship_shoot_laser(self.time)
            elif event.type == pygame.QUIT:
                return False

    def render(self):
        self.renderer.render()
