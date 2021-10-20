
import pygame
from pygame import font
pygame.init()
class FONT:
    """
    FONT\n
    create a pygame font asset to use if for text\n
    """
    def __init__(self, path:str, size:int):
        """
        Parameters:\n
        :path (str): String path to the .ttf file(or other pygame supported formats)\n
        :size (int): the size of the font\n
        :bakground(COLOUR): background colour \n
        """
        if path is None:
            path = "../Resources/font_big.ttf"
        self.path = path
        self.size = size
        self.font = pygame.font.Font(self.path, self.size)

font_16 = pygame.font.Font("Resources/font_small.ttf", 10)
font_8 = pygame.font.Font("Resources/font_small.ttf", 8)

