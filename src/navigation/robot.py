import math
import pygame

from src.utils.constants import *


class Robot:

    def __init__(self):

        self.x = 0
        self.y = 0

        self.path = []
        self.index = 0

        self.speed = 4

        self.active = False

        # Robot heading (degrees)
        self.angle = 0

    # ---------------------------------

    def set_position(self, node):

        self.x = node.x + CELL_SIZE // 2
        self.y = node.y + CELL_SIZE // 2

        self.path = []
        self.index = 0
        self.active = False
        self.angle = 0

    # ---------------------------------

    def set_path(self, path):

        if not path:
            return

        self.path = path
        self.index = 0
        self.active = True

    # ---------------------------------

    def update(self):

        if not self.active:
            return

        if self.index >= len(self.path):

            self.active = False
            return

        target = self.path[self.index]

        target_x = target.x + CELL_SIZE // 2
        target_y = target.y + CELL_SIZE // 2

        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.hypot(dx, dy)

        if distance < self.speed:

            self.x = target_x
            self.y = target_y

            self.index += 1

        else:

            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

            self.angle = math.degrees(
                math.atan2(dy, dx)
            )

    # ---------------------------------

    def draw(self, screen):

        if self.x == 0 and self.y == 0:
            return

        body_radius = CELL_SIZE // 3

        # Main robot body
        pygame.draw.circle(
            screen,
            (40, 170, 255),
            (int(self.x), int(self.y)),
            body_radius
        )

        # Body outline
        pygame.draw.circle(
            screen,
            (230, 230, 230),
            (int(self.x), int(self.y)),
            body_radius,
            2
        )

        # Front heading indicator
        front_length = body_radius + 4

        hx = self.x + front_length * math.cos(
            math.radians(self.angle)
        )

        hy = self.y + front_length * math.sin(
            math.radians(self.angle)
        )

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            (int(hx), int(hy)),
            3
        )

        pygame.draw.circle(
            screen,
            (255, 80, 80),
            (int(hx), int(hy)),
            4
        )