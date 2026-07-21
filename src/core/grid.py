import pygame

from src.utils.constants import *
from src.core.node import Node


class Grid:

    def __init__(self):

        self.grid = []

        for row in range(ROWS):

            self.grid.append([])

            for col in range(COLS):

                self.grid[row].append(Node(row, col))

    def draw(self, screen):

        screen.fill(BACKGROUND_COLOR)

        for row in self.grid:

            for node in row:

                node.draw(screen)

        for row in range(ROWS + 1):

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (0, row * CELL_SIZE),
                (WINDOW_WIDTH, row * CELL_SIZE),
            )

        for col in range(COLS + 1):

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (col * CELL_SIZE, 0),
                (col * CELL_SIZE, WINDOW_HEIGHT),
            )