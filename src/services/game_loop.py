import pygame

class GameLoop:
    """ A class that runs the game loop """

    def __init__(self, game, renderer, clock, event_queue):
        self.game = game
        self.renderer = renderer
        self.clock = clock
        self.event_queue = event_queue

    def run(self):
        while True:
            if self.events() == False:
                break
             
            self.clock.tick(60) 
            self.render()

    def events(self):
        for event in self.event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.move_spaceship(dx=-15)
                if event.key == pygame.K_RIGHT:
                    self.game.move_spaceship(dx=15)
            elif event.type == pygame.QUIT:
                return False

    def render(self):
        self.renderer.render()
