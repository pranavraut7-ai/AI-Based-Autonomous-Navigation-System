from collections import deque

from src.planning.common import (
    handle_quit,
    get_neighbors,
    reconstruct_path,
    draw_path,
)


def bfs(draw, grid, start, goal):

    queue = deque([start])

    came_from = {}

    visited = {start}

    while queue:

        if handle_quit():
            return []

        current = queue.popleft()

        if current == goal:

            path = reconstruct_path(
                came_from,
                goal
            )

            draw_path(
                draw,
                path,
                start,
                goal
            )

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