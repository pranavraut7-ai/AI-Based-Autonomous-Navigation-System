import pygame

from src.core.grid import Grid
from src.navigation.robot import Robot
from src.visualization.hud import HUD
from src.planning.astar import astar

from src.utils.constants import *


class Simulation:

    def __init__(self, screen):

        self.screen = screen

        self.grid = Grid()

        self.robot = Robot()

        self.hud = HUD()

        self.start = None

        self.goal = None

    def handle_mouse(self, event):

        x, y = pygame.mouse.get_pos()

        row = y // CELL_SIZE
        col = x // CELL_SIZE

        if row >= ROWS or col >= COLS:
            return

        node = self.grid.grid[row][col]

        if event.button == 1:

            if self.start is None:

                self.start = node

                self.start.make_start()

                self.robot.set_position(node)

            elif self.goal is None and node != self.start:

                self.goal = node

                self.goal.make_goal()

            elif node != self.start and node != self.goal:

                node.make_obstacle()

        elif event.button == 3:

            node.reset()

            if node == self.start:
                self.start = None

            if node == self.goal:
                self.goal = None

    def find_path(self):

        if not self.start or not self.goal:
            return

        self.grid.clear_search(
            self.start,
            self.goal
        )

        path = astar(

            lambda: self.render(),

            self.grid.grid,

            self.start,

            self.goal

        )

        self.robot.set_path(path)

    def update(self):

        self.robot.update()

    def render(self):

        self.grid.draw(self.screen)

        self.robot.draw(self.screen)

        self.hud.draw(self.screen)

        pygame.display.update()