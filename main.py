import pygame

from src.navigation.robot import Robot
from src.visualization.hud import HUD
from src.utils.constants import *
from src.core.grid import Grid
from src.planning.astar import astar

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AI Autonomous Navigation System")

clock = pygame.time.Clock()

grid = Grid()
hud = HUD()
robot = Robot()

start = None
goal = None

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if start and goal:

                 for row in grid.grid:
                   for node in row:
                      if node not in (start, goal) and node.color not in (OBSTACLE_COLOR,):
                          node.reset()

                 start.make_start()
                 goal.make_goal()

                path = astar(
                  lambda: (
                          robot.update(),

                          grid.draw(screen),

                          robot.draw(screen),

                          hud.draw(screen),

                          pygame.display.update()
                      ),
                          grid.grid,
                          start,
                          goal
                     )

                robot.set_path(path)

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()

            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if row < ROWS and col < COLS:

                node = grid.grid[row][col]

                # Left Click
                if event.button == 1:

                    if start is None:

                        start = node
                        start.make_start()
                        robot.set_position(start)

                    elif goal is None and node != start:

                        goal = node
                        goal.make_goal()

                    elif node != start and node != goal:

                        node.make_obstacle()

                # Right Click
                elif event.button == 3:

                    node.reset()

                    if node == start:
                        start = None

                    if node == goal:
                        goal = None

    grid.draw(screen)

    pygame.display.update()

pygame.quit()