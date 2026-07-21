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

            if neighbor.color != OBSTACLE_COLOR:
                neighbors.append(neighbor)

    return neighbors


def reconstruct_path(draw, came_from, current, start):

    path = [current]      # Goal node included first

    while current in came_from:

        current = came_from[current]

        if current != start:
            current.make_path()

        path.append(current)

        draw()

    path.reverse()
    return path
    
def astar(draw, grid, start, goal):

    open_set = []

    heapq.heappush(open_set, (0, id(start), start))

    came_from = {}

    g_score = {start: 0}

    while open_set:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = heapq.heappop(open_set)[2]

        if current == goal:

           path = reconstruct_path(
              draw,
              came_from,
              goal,
              start
            )

           return path

        for neighbor in get_neighbors(current, grid):

            temp_g = g_score[current] + 1

            if temp_g < g_score.get(neighbor, float("inf")):

                came_from[neighbor] = current
                g_score[neighbor] = temp_g

                f = temp_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f, id(neighbor), neighbor))

                if neighbor != goal:
                    neighbor.make_open()

        if current != start:
            current.make_closed()

        draw()

    return []