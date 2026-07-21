import pygame

from src.utils.constants import *


class Node:

    def __init__(self, row, col):

        self.row = row
        self.col = col

        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE

        self.color = EMPTY_COLOR

    def get_position(self):
        return self.row, self.col

    def reset(self):
        self.color = EMPTY_COLOR

    def make_start(self):
        self.color = START_COLOR

    def make_goal(self):
        self.color = GOAL_COLOR

    def make_obstacle(self):
        self.color = OBSTACLE_COLOR

    def make_open(self):
        if self.color not in (
            START_COLOR,
            GOAL_COLOR,
            OBSTACLE_COLOR,
        ):
            self.color = OPEN_COLOR

    def make_closed(self):
        if self.color not in (
            START_COLOR,
            GOAL_COLOR,
            OBSTACLE_COLOR,
        ):
            self.color = CLOSED_COLOR

    def make_path(self):
        if self.color not in (
            START_COLOR,
            GOAL_COLOR,
        ):
            self.color = PATH_COLOR

    def is_obstacle(self):
        return self.color == OBSTACLE_COLOR

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x,
                self.y,
                CELL_SIZE,
                CELL_SIZE,
            ),
        )

    def __lt__(self, other):
        return False

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.row == other.row
            and self.col == other.col
        )