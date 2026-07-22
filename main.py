import pygame

from src.simulation.simulation import Simulation
from src.utils.constants import *


def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )
    )

    pygame.display.set_caption(
        "AI Autonomous Navigation System"
    )

    clock = pygame.time.Clock()

    simulation = Simulation(screen)

    # Keep HUD synchronized with the default algorithm
    simulation.hud.set_algorithm(simulation.current_algorithm)

    running = True

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                simulation.handle_mouse(event)

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_SPACE:
                    simulation.find_path()

                elif event.key == pygame.K_1:

                    simulation.current_algorithm = "A*"
                    simulation.hud.set_algorithm("A*")
                    simulation.hud.set_status("A* SELECTED")

                elif event.key == pygame.K_2:

                    simulation.current_algorithm = "DIJKSTRA"
                    simulation.hud.set_algorithm("DIJKSTRA")
                    simulation.hud.set_status("DIJKSTRA SELECTED")

                elif event.key == pygame.K_r:
                    simulation.reset_simulation()

                elif event.key == pygame.K_c:
                    simulation.clear_obstacles()

                elif event.key == pygame.K_n:
                    simulation.new_map()

        simulation.update()

        simulation.render()

    pygame.quit()


if __name__ == "__main__":

    main()