from src.planning.common import (
    handle_quit,
    get_neighbors,
    reconstruct_path,
    draw_path,
)


def dfs(draw, grid, start, goal):

    stack = [start]

    came_from = {}

    visited = {start}

    while stack:

        if handle_quit():
            return []

        current = stack.pop()

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

        neighbors = get_neighbors(
            current,
            grid
        )

        # Reverse to maintain a predictable traversal order
        for neighbor in reversed(neighbors):

            if neighbor not in visited:

                visited.add(neighbor)

                came_from[neighbor] = current

                stack.append(neighbor)

                if neighbor != goal:

                    neighbor.make_open()

        draw()

    return []