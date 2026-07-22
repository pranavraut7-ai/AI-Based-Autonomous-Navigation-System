import pygame

# =====================================================
# Window
# =====================================================

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

FPS = 60

# =====================================================
# Grid
# =====================================================

ROWS = 20
COLS = 20

CELL_SIZE = WINDOW_WIDTH // COLS

# =====================================================
# Professional Light Theme
# =====================================================

BACKGROUND_COLOR = (245, 247, 250)

GRID_COLOR = (220, 224, 229)

EMPTY_COLOR = (255, 255, 255)

START_COLOR = (46, 204, 113)

GOAL_COLOR = (231, 76, 60)

OBSTACLE_COLOR = (55, 55, 55)

OPEN_COLOR = (102, 204, 255)

CLOSED_COLOR = (223, 230, 238)

PATH_COLOR = (255, 193, 7)

ROBOT_COLOR = (52, 152, 219)

TEXT_COLOR = (35, 35, 35)

PANEL_COLOR = (255, 255, 255)

PANEL_BORDER = (205, 210, 218)

# =====================================================
# Fonts
# =====================================================

pygame.font.init()

TITLE_FONT = pygame.font.SysFont(
    "Segoe UI",
    24,
    bold=True
)

HUD_FONT = pygame.font.SysFont(
    "Segoe UI",
    18
)