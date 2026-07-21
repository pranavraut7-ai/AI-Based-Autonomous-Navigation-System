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

        screen.fill(BACKGROUND_COLOR)

        # Draw Nodes
        for row in self.grid:
            for node in row:
                node.draw(screen)

        # Draw Grid Lines
        for row in range(ROWS + 1):

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (0, row * CELL_SIZE),
                (WINDOW_WIDTH, row * CELL_SIZE),
                1,
            )

        for col in range(COLS + 1):

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (col * CELL_SIZE, 0),
                (col * CELL_SIZE, WINDOW_HEIGHT),
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