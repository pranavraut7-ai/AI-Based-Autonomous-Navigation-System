import math
import pygame

from src.utils.constants import *


class Robot:

    def __init__(self):

        self.node = None

        self.path = []

        self.radius = CELL_SIZE // 2 - 4

        self.color = ROBOT_COLOR

        self.pixel_x = 0.0
        self.pixel_y = 0.0

        self.target_x = 0.0
        self.target_y = 0.0

        self.speed = 3.0

        self.direction = 0

        self.moving = False

    def set_position(self, node):

        self.node = node

        self.pixel_x = node.col * CELL_SIZE + CELL_SIZE / 2
        self.pixel_y = node.row * CELL_SIZE + CELL_SIZE / 2

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y

    def set_path(self, path):

        self.path = list(path)

        if len(self.path) > 0:

            first = self.path.pop(0)

            self.node = first

            self.pixel_x = first.col * CELL_SIZE + CELL_SIZE / 2
            self.pixel_y = first.row * CELL_SIZE + CELL_SIZE / 2

            self.target_x = self.pixel_x
            self.target_y = self.pixel_y

            self.moving = True

    def update(self):

        if not self.moving:
            return

        dx = self.target_x - self.pixel_x
        dy = self.target_y - self.pixel_y

        distance = math.hypot(dx, dy)

        if distance <= self.speed:

            self.pixel_x = self.target_x
            self.pixel_y = self.target_y

            if self.path:

                self.node = self.path.pop(0)

                self.target_x = (
                    self.node.col * CELL_SIZE +
                    CELL_SIZE / 2
                )

                self.target_y = (
                    self.node.row * CELL_SIZE +
                    CELL_SIZE / 2
                )

            else:

                self.moving = False

            return

        angle = math.atan2(dy, dx)

        self.direction = math.degrees(angle)

        self.pixel_x += math.cos(angle) * self.speed
        self.pixel_y += math.sin(angle) * self.speed

    def draw(self, screen):

        if self.node is None:
            return

        x = int(self.pixel_x)
        y = int(self.pixel_y)

        pygame.draw.circle(
            screen,
            self.color,
            (x, y),
            self.radius
        )

        head_x = x + math.cos(
            math.radians(self.direction)
        ) * 8

        head_y = y + math.sin(
            math.radians(self.direction)
        ) * 8

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(head_x), int(head_y)),
            3
        )