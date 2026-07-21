import pygame

from src.utils.constants import *


class HUD:

    def __init__(self):

        self.algorithm = "A*"

        self.status = "Ready"

    def draw(self, screen):

        panel = pygame.Rect(
            0,
            WINDOW_HEIGHT - 40,
            WINDOW_WIDTH,
            40
        )

        pygame.draw.rect(
            screen,
            (18, 18, 18),
            panel
        )

        text = HUD_FONT.render(
            f"Algorithm : {self.algorithm}      Status : {self.status}",
            True,
            TEXT_COLOR
        )

        screen.blit(
            text,
            (10, WINDOW_HEIGHT - 28)
        )