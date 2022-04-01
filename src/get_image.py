import pygame
import os

dirname = os.path.dirname(__file__)

def get_image(imagename):
    """ A method to load images """
    return pygame.image.load(
        os.path.join(dirname, "assets", imagename)
    )