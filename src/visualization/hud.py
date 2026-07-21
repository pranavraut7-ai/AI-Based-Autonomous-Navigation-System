import pygame

from src.utils.constants import *


class HUD:

    def __init__(self):

        pygame.font.init()

        self.font = pygame.font.SysFont("consolas", 20)

    def draw(
        self,
        screen,
        algorithm="A*",
        explored=0,
        path_length=0,
        execution_time=0,
    ):

        texts = [

            f"Algorithm : {algorithm}",
            f"Explored : {explored}",
            f"Path Length : {path_length}",
            f"Execution : {execution_time:.2f} ms",

        ]

        y = 10

        for text in texts:

            surface = self.font.render(text, True, (20, 20, 20))

            screen.blit(surface, (10, y))

            y += 25