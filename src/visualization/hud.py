import pygame

from src.utils.constants import *


class HUD:

    def __init__(self):

        self.algorithm = "A*"

        self.status = "READY"

        self.path_length = 0

        self.robot_state = "IDLE"

    # -------------------------------------

    def set_status(self, status):

        self.status = status

    # -------------------------------------

    def set_path_length(self, length):

        self.path_length = length

    # -------------------------------------

    def set_robot_state(self, state):

        self.robot_state = state

    # -------------------------------------

    def draw(self, screen):

        panel_width = 260

        panel = pygame.Surface(
            (panel_width, WINDOW_HEIGHT),
            pygame.SRCALPHA
        )

        panel.fill((15, 15, 15, 210))

        screen.blit(panel, (0, 0))

        y = 20

        def title(text):

            nonlocal y

            surface = TITLE_FONT.render(
                text,
                True,
                (255, 255, 255)
            )

            screen.blit(surface, (15, y))

            y += 35

        def item(label, value):

            nonlocal y

            label_surface = HUD_FONT.render(
                label,
                True,
                (170, 170, 170)
            )

            value_surface = HUD_FONT.render(
                value,
                True,
                (255, 255, 255)
            )

            screen.blit(label_surface, (15, y))
            screen.blit(value_surface, (140, y))

            y += 28

        title("AI Navigation")

        item("Algorithm", self.algorithm)

        item("Status", self.status)

        item(
            "Path Length",
            str(self.path_length)
        )

        item(
            "Robot",
            self.robot_state
        )

        y += 15

        title("Controls")

        controls = [

            "SPACE  Run",

            "R      Reset",

            "C      Clear",

            "N      New Map",

            "ESC    Exit"

        ]

        for control in controls:

            text = HUD_FONT.render(
                control,
                True,
                (230, 230, 230)
            )

            screen.blit(text, (15, y))

            y += 24