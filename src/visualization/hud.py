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

            "DFS PLANNING": (243, 156, 18),

            "MOVING": (41, 128, 185),

            "GOAL REACHED": (39, 174, 96),

            "A* SELECTED": (52, 152, 219),

            "DIJKSTRA SELECTED": (155, 89, 182),

            "BFS SELECTED": (230, 126, 34),

            "DFS SELECTED": (26, 188, 156)

        }

        return colors.get(self.status, TEXT_COLOR)

    # --------------------------------------------------

    def draw(self, screen):

        padding = 18

        y = 24

        # ==================================================
        # Title
        # ==================================================

        title = TITLE_FONT.render(
             "AI Navigation",
             True,
             TEXT_COLOR
         )

        subtitle = SUBTITLE_FONT.render(
             "Path Planning Simulator",
             True,
             (140, 140, 140)
         )

        screen.blit(title, (padding, y))

        screen.blit(
           subtitle,
           (padding + 2, y + 30)
         )

        y += 66


        # ==================================================
        # Information
        # ==================================================

        def item(label, value, color=TEXT_COLOR):

            nonlocal y

            label_surface = HUD_FONT.render(
                label,
                True,
                (110, 110, 110)
            )

            value_surface = HUD_FONT.render(
                value,
                True,
                color
            )

            screen.blit(label_surface, (padding, y))
            screen.blit(value_surface, (138, y))

            y += 34

        item("Algorithm", self.algorithm)

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

        # ==================================================
        # Divider
        # ==================================================

        y += 12

        pygame.draw.line(
            screen,
            PANEL_BORDER,
            (padding, y),
            (HUD_WIDTH - padding, y),
            1
        )

        y += 24

        # ==================================================
        # Controls
        # ==================================================

        controls_title = TITLE_FONT.render(
            "Controls",
            True,
            TEXT_COLOR
        )

        screen.blit(
            controls_title,
            (padding, y)
        )

        y += 42

        controls = [

            ("1", "A*"),

            ("2", "Dijkstra"),

            ("3", "BFS"),

            ("4", "DFS"),

            ("SPACE", "Run"),

            ("R", "Reset"),

            ("C", "Clear"),

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
                (padding, y)
            )

            screen.blit(
                action_surface,
                (110, y)
            )

            footer = SUBTITLE_FONT.render(
                 "Version 1.0",
                 True,
                 (160, 160, 160)
             )

            screen.blit(
                 footer,
                 (padding, WINDOW_HEIGHT - 28)
             )


            y += 30