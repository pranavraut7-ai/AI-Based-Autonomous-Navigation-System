import heapq

from src.planning.common import (
    handle_quit,
    get_neighbors,
    reconstruct_path,
    draw_path,
)


def heuristic(a, b):

    return abs(a.row - b.row) + abs(a.col - b.col)


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

        if handle_quit():
            return []

        current = heapq.heappop(
            open_set
        )[2]

        if current in visited:
            continue

        visited.add(current)

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

                priority = (
                    tentative
                    + heuristic(
                        neighbor,
                        goal
                    )
                )

                heapq.heappush(

                    open_set,

                    (
                        priority,
                        counter,
                        neighbor
                    )

                )

                if neighbor != goal:

                    neighbor.make_open()

        draw()

    return []