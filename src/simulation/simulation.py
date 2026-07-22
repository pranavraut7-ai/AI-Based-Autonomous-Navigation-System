import pygame

from src.core.grid import Grid
from src.navigation.robot import Robot
from src.visualization.hud import HUD

from src.planning.astar import astar
from src.planning.dijkstra import dijkstra
from src.planning.bfs import bfs

from src.utils.constants import *


class Simulation:

    def __init__(self, screen):

        self.screen = screen

        self.grid = Grid()

        self.robot = Robot()

        self.hud = HUD()

        self.start = None
        self.goal = None

        self.current_algorithm = "A*"

        self.algorithms = {
            "A*": astar,
            "DIJKSTRA": dijkstra,
            "BFS": bfs
        }

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

                self.hud.set_status("START SET")

            elif self.goal is None and node != self.start:

                self.goal = node
                self.goal.make_goal()

                self.hud.set_status("GOAL SET")

            elif node != self.start and node != self.goal:

                node.make_obstacle()

        elif event.button == 3:

            node.reset()

            if node == self.start:
                self.start = None

            if node == self.goal:
                self.goal = None

    def find_path(self):

        if self.start is None or self.goal is None:
            return

        self.hud.set_status(f"{self.current_algorithm} PLANNING")

        self.grid.clear_search(
            self.start,
            self.goal
        )

        planner = self.algorithms.get(
            self.current_algorithm,
            astar
        )

        path = planner(
            lambda: self.render(),
            self.grid.grid,
            self.start,
            self.goal
        )

        self.robot.set_path(path)

        self.hud.set_status("MOVING")

        self.hud.set_robot_state("ACTIVE")

        self.hud.set_path_length(len(path))

    def clear_obstacles(self):

        for row in self.grid.grid:

            for node in row:

                if (
                    node != self.start and
                    node != self.goal and
                    node.is_obstacle()
                ):
                    node.reset()

        self.hud.set_status("READY")

    def new_map(self):

        self.grid.reset_all()

        self.start = None
        self.goal = None

        self.robot = Robot()

        self.hud = HUD()

        self.current_algorithm = "A*"

        self.hud.set_algorithm("A*")

    def reset_simulation(self):

        self.new_map()

    def update(self):

        self.robot.update()

        if not self.robot.active and self.hud.robot_state == "ACTIVE":

            self.hud.set_status("GOAL REACHED")

            self.hud.set_robot_state("IDLE")

    def render(self):

        self.grid.draw(self.screen)

        self.robot.draw(self.screen)

        self.hud.draw(self.screen)

        pygame.display.update()