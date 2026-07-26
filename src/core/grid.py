import pygame

from src.utils.constants import *
from src.core.node import Node


class Grid:

    def __init__(self):

        self.grid = [
            [Node(row, col) for col in range(COLS)]
            for row in range(ROWS)
        ]

    def draw(self, screen):

        # Background
        screen.fill(BACKGROUND_COLOR)

        # ----------------------------------------------------
        # HUD Panel
        # ----------------------------------------------------

        pygame.draw.rect(
            screen,
            PANEL_COLOR,
            (0, 0, HUD_WIDTH, WINDOW_HEIGHT)
        )

        # Divider
        pygame.draw.line(
             screen,
             PANEL_BORDER,
             (HUD_WIDTH, 0),
             (HUD_WIDTH, WINDOW_HEIGHT),
             2,
        )

        # ----------------------------------------------------
        # Draw Nodes
        # ----------------------------------------------------

        for row in self.grid:
            for node in row:
                node.draw(screen)

        # ----------------------------------------------------
        # Draw Horizontal Grid Lines
        # ----------------------------------------------------

        for row in range(ROWS + 1):

            y = GRID_START_Y + (row * CELL_SIZE)

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (GRID_START_X, y),
                (GRID_START_X + GRID_PIXEL_WIDTH, y),
                1,
            )

        # ----------------------------------------------------
        # Draw Vertical Grid Lines
        # ----------------------------------------------------

        for col in range(COLS + 1):

            x = GRID_START_X + (col * CELL_SIZE)

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (x, GRID_START_Y),
                (x, GRID_START_Y + GRID_PIXEL_HEIGHT),
                1,
            )

    def clear_search(self, start=None, goal=None):

        """
        Clears only search visualization.
        Keeps:
        - Obstacles
        - Start
        - Goal
        """

        for row in self.grid:
            for node in row:

                if node == start or node == goal:
                    continue

                if node.is_obstacle():
                    continue

                node.reset()

        if start:
            start.make_start()

        if goal:
            goal.make_goal()

    def reset_all(self):

        """
        Clears the complete grid.
        """

        for row in self.grid:
            for node in row:
                node.reset()