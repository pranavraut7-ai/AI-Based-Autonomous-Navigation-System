import heapq

from src.planning.common import (
    handle_quit,
    get_neighbors,
    reconstruct_path,
    draw_path,
)


def dijkstra(draw, grid, start, goal):

    open_set = []

    counter = 0

    heapq.heappush(

        open_set,

        (
            0,
            counter,
            start
        )

    )

    came_from = {}

    distance = {

        start: 0

    }

    visited = set()

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

            new_distance = (
                distance[current]
                + 1
            )

            if new_distance < distance.get(
                neighbor,
                float("inf")
            ):

                distance[neighbor] = new_distance

                came_from[neighbor] = current

                counter += 1

                heapq.heappush(

                    open_set,

                    (
                        new_distance,
                        counter,
                        neighbor
                    )

                )

                if neighbor != goal:

                    neighbor.make_open()

        draw()

    return []