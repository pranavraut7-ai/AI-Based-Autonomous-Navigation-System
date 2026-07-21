import pygame

from src.utils.constants import *


class Robot:

    def __init__(self):

        self.node = None

        self.path = []

        self.radius = CELL_SIZE // 2 - 2

        self.color = (30, 30, 255)

        self.move_delay = 8
        self.counter = 0

        self.pixel_x = 0
        self.pixel_y = 0

        self.target_x = 0
        self.target_y = 0

        self.speed = 4

    def set_position(self, node):

        self.node = node

        self.pixel_x = node.col * CELL_SIZE + CELL_SIZE // 2
        self.pixel_y = node.row * CELL_SIZE + CELL_SIZE // 2

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y

    def set_path(self, path):

        self.path = list(path)

        if self.path:
            # Reset robot to the first node of the new path
            first = self.path.pop(0)

            self.node = first

            self.pixel_x = first.col * CELL_SIZE + CELL_SIZE // 2
            self.pixel_y = first.row * CELL_SIZE + CELL_SIZE // 2

            self.target_x = self.pixel_x
            self.target_y = self.pixel_y

    def update(self):

        # Move to the next node only after reaching the current target
        if (
            abs(self.pixel_x - self.target_x) < 1
            and
            abs(self.pixel_y - self.target_y) < 1
         ):

            self.pixel_x = self.target_x
            self.pixel_y = self.target_y

            if self.path:

                next_node = self.path.pop(0)

                self.node = next_node

                self.target_x = (
                    next_node.col * CELL_SIZE
                    + CELL_SIZE // 2
                 )

                self.target_y = (
                    next_node.row * CELL_SIZE
                    + CELL_SIZE // 2
                 )

         # Smooth X movement
        if self.pixel_x < self.target_x:
           self.pixel_x = min(self.pixel_x + self.speed, self.target_x)

        elif self.pixel_x > self.target_x:
             self.pixel_x = max(self.pixel_x - self.speed, self.target_x)

         # Smooth Y movement
        if self.pixel_y < self.target_y:
           self.pixel_y = min(self.pixel_y + self.speed, self.target_y)

        elif self.pixel_y > self.target_y:
            self.pixel_y = max(self.pixel_y - self.speed, self.target_y)

        # Snap exactly onto the target
        if abs(self.pixel_x - self.target_x) < 1:
            self.pixel_x = self.target_x

        if abs(self.pixel_y - self.target_y) < 1:
            self.pixel_y = self.target_y    

    def draw(self, screen):

        if self.node is None:
            return

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.pixel_x), int(self.pixel_y)),
            self.radius,
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.pixel_x), int(self.pixel_y)),
            5,
        )