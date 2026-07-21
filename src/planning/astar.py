import heapq
import pygame

from src.utils.constants import *


def heuristic(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


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


def astar(draw, grid, start, goal):

    open_set = []

    heapq.heappush(
        open_set,
        (
            0,
            0,
            start
        )
    )

    came_from = {}

    g_score = {
        start: 0
    }

    visited = set()

    counter = 0

    while open_set:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return []

        current = heapq.heappop(open_set)[2]

        if current in visited:
            continue

        visited.add(current)

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

        for neighbor in get_neighbors(current, grid):

            tentative = (
                g_score[current]
                + 1
            )

            if tentative < g_score.get(
                neighbor,
                float("inf")
            ):

                came_from[neighbor] = current

                g_score[neighbor] = tentative

                counter += 1

                f = (
                    tentative
                    + heuristic(
                        neighbor,
                        goal
                    )
                )

                heapq.heappush(
                    open_set,
                    (
                        f,
                        counter,
                        neighbor
                    )
                )

                if neighbor != goal:
                    neighbor.make_open()

        draw()

    return []