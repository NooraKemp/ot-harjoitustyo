import pygame

pygame.font.init()


class MainMenuView:
    '''A class that represents the main menu view.'''

    def __init__(self, display):
        self.display = display
        self.font = pygame.font.SysFont('Helvetica', 100)
        self.button_font = pygame.font.SysFont('Helvetica', 50)

    def draw_main_menu(self):
        '''A method that draws the main menu view text and buttons.'''

        self.main_menu = self.font.render(
            'MAIN MENU', False, (255, 255, 255))
        pygame.draw.rect(self.display, (0, 0, 0), [300, 300, 400, 60])
        self.start = self.button_font.render(
            'PLAY', False, (255, 255, 255))
        pygame.draw.rect(self.display, (0, 0, 0), [300, 400, 400, 60])
        self.quit = self.button_font.render(
            'QUIT', False, (255, 255, 255))
        self.display.blit(self.main_menu, (220, 100))
        self.display.blit(self.start, (450, 300))
        self.display.blit(self.quit, (450, 400))
