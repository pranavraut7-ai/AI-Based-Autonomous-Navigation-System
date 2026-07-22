from collections import deque
import pygame

from src.utils.constants import *


def get_neighbors(node, grid):

    neighbors = []

    directions = [

        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),

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


def bfs(draw, grid, start, goal):

    queue = deque([start])

    came_from = {}

    visited = {start}

    while queue:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return []

        current = queue.popleft()

        if current == goal:

            path = reconstruct_path(
                came_from,
                goal
            )

            for node in path:

                if node != start and node != goal:
                    node.make_path()

            draw()

            return path

        if current != start:
            current.make_closed()

        for neighbor in get_neighbors(
            current,
            grid
        ):

            if neighbor not in visited:

                visited.add(neighbor)

                came_from[neighbor] = current

                queue.append(neighbor)

                if neighbor != goal:
                    neighbor.make_open()

        draw()

    return []