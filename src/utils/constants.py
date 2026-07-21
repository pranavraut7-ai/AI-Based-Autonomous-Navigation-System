import pygame

# -----------------------------
# Window
# -----------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 60

# -----------------------------
# Grid
# -----------------------------
ROWS = 20
COLS = 20

CELL_SIZE = WINDOW_WIDTH // COLS

# -----------------------------
# Colors
# -----------------------------
BACKGROUND_COLOR = (25, 25, 25)

GRID_COLOR = (60, 60, 60)

EMPTY_COLOR = (35, 35, 35)

START_COLOR = (46, 204, 113)

GOAL_COLOR = (231, 76, 60)

OBSTACLE_COLOR = (15, 15, 15)

OPEN_COLOR = (52, 152, 219)

CLOSED_COLOR = (241, 196, 15)

PATH_COLOR = (155, 89, 182)

ROBOT_COLOR = (52, 152, 219)

TEXT_COLOR = (240, 240, 240)

# -----------------------------
# Fonts
# -----------------------------
pygame.font.init()

HUD_FONT = pygame.font.SysFont("Segoe UI", 18)

TITLE_FONT = pygame.font.SysFont("Segoe UI", 24, bold=True)