import pygame

# =====================================================
# Window
# =====================================================

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 900

FPS = 60

# =====================================================
# Layout
# =====================================================

HUD_WIDTH = 260

GRID_WIDTH = WINDOW_WIDTH - HUD_WIDTH
GRID_HEIGHT = WINDOW_HEIGHT

# =====================================================
# Grid
# =====================================================

ROWS = 36
COLS = 36

CELL_SIZE = min(
    GRID_WIDTH // COLS,
    GRID_HEIGHT // ROWS
)

# =====================================================
# Actual Grid Size
# =====================================================

GRID_PIXEL_WIDTH = COLS * CELL_SIZE
GRID_PIXEL_HEIGHT = ROWS * CELL_SIZE

# =====================================================
# Center Grid inside Simulation Area
# =====================================================

GRID_START_X = HUD_WIDTH + (GRID_WIDTH - GRID_PIXEL_WIDTH) // 2

GRID_START_Y = (GRID_HEIGHT - GRID_PIXEL_HEIGHT) // 2

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

SUBTITLE_FONT = pygame.font.SysFont(
    "Segoe UI",
    13
)

HUD_FONT = pygame.font.SysFont(
    "Segoe UI",
    18
)