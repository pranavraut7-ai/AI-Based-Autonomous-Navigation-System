import math
import pygame

from src.utils.constants import *


class Robot:

    def __init__(self):

        self.x = 0
        self.y = 0

        self.path = []
        self.index = 0

        self.max_speed = 4.0
        self.speed = 0.0
        self.acceleration = 0.18

        self.active = False

        self.angle = 0
        self.target_angle = 0
        self.turn_speed = 6

        # Goal animation
        self.goal_animation = False
        self.goal_timer = 0
        self.goal_duration = 40

    # --------------------------------------------------

    def set_position(self, node):

        self.x = node.x + CELL_SIZE // 2
        self.y = node.y + CELL_SIZE // 2

        self.path = []
        self.index = 0

        self.speed = 0

        self.angle = 0
        self.target_angle = 0

        self.active = False

        self.goal_animation = False
        self.goal_timer = 0

    # --------------------------------------------------

    def set_path(self, path):

        if not path:
            return

        self.path = path
        self.index = 0

        self.speed = 0

        self.goal_animation = False
        self.goal_timer = 0

        self.active = True

    # --------------------------------------------------

    def update(self):

        # Goal pulse animation
        if self.goal_animation:

            self.goal_timer += 1

            if self.goal_timer >= self.goal_duration:

                self.goal_animation = False

            return

        if not self.active:
            return

        if self.index >= len(self.path):

            self.active = False
            self.speed = 0

            self.goal_animation = True
            self.goal_timer = 0

            return

        target = self.path[self.index]

        target_x = target.x + CELL_SIZE // 2
        target_y = target.y + CELL_SIZE // 2

        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.hypot(dx, dy)

        if distance > 0:

            self.target_angle = math.degrees(
                math.atan2(dy, dx)
            )

        angle_diff = (
            self.target_angle - self.angle + 180
        ) % 360 - 180

        if abs(angle_diff) > self.turn_speed:

            self.angle += (
                self.turn_speed
                if angle_diff > 0
                else -self.turn_speed
            )

        else:

            self.angle = self.target_angle

        if self.speed < self.max_speed:

            self.speed += self.acceleration

            if self.speed > self.max_speed:
                self.speed = self.max_speed

        if distance < self.speed:

            self.x = target_x
            self.y = target_y

            self.index += 1

        else:

            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    # --------------------------------------------------

    def draw(self, screen):

        if self.x == 0 and self.y == 0:
            return

        radius = CELL_SIZE // 3

        body_color = (45, 170, 255)

        # Green pulse after reaching goal
        if self.goal_animation:

            pulse = radius + int(
                8 * abs(math.sin(self.goal_timer * 0.25))
            )

            pygame.draw.circle(
                screen,
                (80, 255, 120),
                (int(self.x), int(self.y)),
                pulse,
                3
            )

            body_color = (80, 255, 120)

        pygame.draw.circle(
            screen,
            body_color,
            (int(self.x), int(self.y)),
            radius
        )

        pygame.draw.circle(
            screen,
            (240, 240, 240),
            (int(self.x), int(self.y)),
            radius,
            2
        )

        rad = math.radians(self.angle)

        nose_x = self.x + math.cos(rad) * (radius + 6)
        nose_y = self.y + math.sin(rad) * (radius + 6)

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (self.x, self.y),
            (nose_x, nose_y),
            3
        )

        pygame.draw.circle(
            screen,
            (255, 90, 90),
            (int(nose_x), int(nose_y)),
            4
        )

        left = math.radians(self.angle + 140)
        right = math.radians(self.angle - 140)

        lx = self.x + math.cos(left) * radius
        ly = self.y + math.sin(left) * radius

        rx = self.x + math.cos(right) * radius
        ry = self.y + math.sin(right) * radius

        pygame.draw.circle(
            screen,
            (70, 70, 70),
            (int(lx), int(ly)),
            3
        )

        pygame.draw.circle(
            screen,
            (70, 70, 70),
            (int(rx), int(ry)),
            3
        )