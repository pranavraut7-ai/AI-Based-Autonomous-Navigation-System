from src.utils.constants import *


class Node:

    def __init__(self, row, col):

        self.row = row
        self.col = col

        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE

        self.color = BACKGROUND_COLOR

    def draw(self, screen):

        import pygame

        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, CELL_SIZE, CELL_SIZE)
        )

    def make_start(self):
        self.color = START_COLOR

    def make_goal(self):
        self.color = GOAL_COLOR

    def make_obstacle(self):
        self.color = OBSTACLE_COLOR

    def make_path(self):
        self.color = PATH_COLOR

    def make_open(self):
        self.color = OPEN_COLOR

    def make_closed(self):
        self.color = CLOSED_COLOR    

    def reset(self):
        self.color = BACKGROUND_COLOR