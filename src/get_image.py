import os
import pygame


dirname = os.path.dirname(__file__)


def get_image(imagename):
    """ Loads images."""
    return pygame.image.load(
        os.path.join(dirname, "assets", imagename)
    )
