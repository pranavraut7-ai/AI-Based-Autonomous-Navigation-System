import pygame

from src.utils.constants import *


def handle_quit():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            return True

    return False


def get_neighbors(node, grid):

    neighbors = []

    directions = [

        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)

    ]

    for dr, dc in directions:

        r = node.row + dr
        c = node.col + dc

        if 0 <= r < ROWS and 0 <= c < COLS:

            neighbor = grid[r][c]

            if not neighbor.is_obstacle():

                neighbors.append(neighbor)

    return neighbors


def reconstruct_path(came_from, current):

    path = [current]

    while current in came_from:

        current = came_from[current]

        path.append(current)

    path.reverse()

    return path


def draw_path(draw, path, start, goal):

    for node in path:

        if node != start and node != goal:

            node.make_path()

    draw()