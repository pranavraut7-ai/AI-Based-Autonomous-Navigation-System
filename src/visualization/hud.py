import pygame

from src.utils.constants import *


class HUD:

    def __init__(self):

        self.algorithm = "A*"
        self.status = "READY"
        self.path_length = 0
        self.robot_state = "IDLE"

    # --------------------------------------------------

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def set_status(self, status):
        self.status = status

    def set_path_length(self, length):
        self.path_length = length

    def set_robot_state(self, state):
        self.robot_state = state

    # --------------------------------------------------

    def get_status_color(self):

        colors = {

            "READY": (90, 90, 90),

            "START SET": (52, 152, 219),

            "GOAL SET": (52, 152, 219),

            "A* PLANNING": (243, 156, 18),
            "DIJKSTRA PLANNING": (243, 156, 18),
            "BFS PLANNING": (243, 156, 18),

            "MOVING": (41, 128, 185),

            "GOAL REACHED": (39, 174, 96),

            "A* SELECTED": (52, 152, 219),

            "DIJKSTRA SELECTED": (155, 89, 182),

            "BFS SELECTED": (230, 126, 34)

        }

        return colors.get(
            self.status,
            TEXT_COLOR
        )

    # --------------------------------------------------

    def draw(self, screen):

        panel_width = 275

        panel = pygame.Surface(
            (
                panel_width,
                WINDOW_HEIGHT
            ),
            pygame.SRCALPHA
        )

        panel.fill(
            (
                255,
                255,
                255,
                150
            )
        )

        pygame.draw.rect(

            panel,

            PANEL_BORDER,

            panel.get_rect(),

            width=2,

            border_radius=18

        )

        screen.blit(
            panel,
            (0, 0)
        )

        y = 22

        title = TITLE_FONT.render(

            "AI Navigation",

            True,

            TEXT_COLOR

        )

        screen.blit(
            title,
            (20, y)
        )

        y += 45

        def item(label, value, color=TEXT_COLOR):

            nonlocal y

            label_surface = HUD_FONT.render(

                label,

                True,

                (100, 100, 100)

            )

            value_surface = HUD_FONT.render(

                value,

                True,

                color

            )

            screen.blit(
                label_surface,
                (20, y)
            )

            screen.blit(
                value_surface,
                (150, y)
            )

            y += 32

        item(
            "Algorithm",
            self.algorithm
        )

        item(
            "Status",
            self.status,
            self.get_status_color()
        )

        item(
            "Path Length",
            str(self.path_length)
        )

        robot_color = (

            (39, 174, 96)

            if self.robot_state == "ACTIVE"

            else (120, 120, 120)

        )

        item(
            "Robot",
            self.robot_state,
            robot_color
        )

        y += 25

        pygame.draw.line(

            screen,

            PANEL_BORDER,

            (20, y),

            (250, y),

            1

        )

        y += 20

        controls_title = TITLE_FONT.render(

            "Controls",

            True,

            TEXT_COLOR

        )

        screen.blit(
            controls_title,
            (20, y)
        )

        y += 40

        controls = [

            ("1", "Select A*"),

            ("2", "Select Dijkstra"),

            ("3", "Select BFS"),

            ("SPACE", "Run Selected"),

            ("R", "Reset"),

            ("C", "Clear Obstacles"),

            ("N", "New Map"),

            ("ESC", "Exit")

        ]

        for key, action in controls:

            key_surface = HUD_FONT.render(

                key,

                True,

                (41, 128, 185)

            )

            action_surface = HUD_FONT.render(

                action,

                True,

                TEXT_COLOR

            )

            screen.blit(
                key_surface,
                (20, y)
            )

            screen.blit(
                action_surface,
                (90, y)
            )

            y += 28