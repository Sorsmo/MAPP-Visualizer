import pygame
import random

from cell import Cell
from algorithms import CooperativeAStar
from algorithms import ConflictedBasedSearch

# GLOBAL VARIABLES
WIDTH = 1080
HEIGHT = 720
SIZE = 15                       # Bigger SIZE --> Smaller tiles (best if multiple of HEIGHT)
CELL_LENGTH = HEIGHT // SIZE    # number of pixels per cell
NUM_AGENTS = 5                  # number of agents to be generated

# Creates a 2D Array representation of the screen
# Made up of Cells w/ properties in cell.py
def init_grid(rows, cols):
    grid = [ [0 for j in range(SIZE)] for i in range(SIZE) ]

    for row in range(rows):
        for col in range(cols):
            grid[row][col] = Cell(row, col)

    for n in range(NUM_AGENTS):
        random_color = (int(random.random()*255), int(random.random()*255), int(random.random()*255))
        
        # ensure other start/end points are not written over
        while True:
            random_x = int(random.random() * SIZE)
            random_y = int(random.random() * SIZE)

            if not grid[random_y][random_x].is_start() and not grid[random_y][random_x].is_end(): 
                grid[random_y][random_x].make_start(random_color)
                break
        
        # ensure other start/end points are not written over
        while True:
            random_x = int(random.random() * SIZE)
            random_y = int(random.random() * SIZE)

            if not grid[random_y][random_x].is_start() and not grid[random_y][random_x].is_end(): 
                grid[random_y][random_x].make_end(random_color)
                break

    return grid

# Uses grid to draw the updated array on screen
def draw_grid(grid, screen):
    for row in range(0, HEIGHT, CELL_LENGTH):
        for col in range(0, HEIGHT, CELL_LENGTH):
            # TODO: add indicators for start and end with text
            pygame.draw.rect(screen, grid[row//CELL_LENGTH][col//CELL_LENGTH].color, pygame.Rect(col, row, CELL_LENGTH, CELL_LENGTH))

def main():
    pygame.init()
    pygame.display.set_caption("Multi-Agent Path Planning Visualizer (MAPPV)")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    screen.fill((40, 40, 40))
    grid = init_grid(SIZE, SIZE)
    draw_grid(grid, screen)
    pygame.display.flip()

    running = True
    dragging = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_pos_x = pygame.mouse.get_pos()[0] // CELL_LENGTH  # normalize for grid indexing
                    mouse_pos_y = pygame.mouse.get_pos()[1] // CELL_LENGTH
                    
                    # prevents out of bounds errors
                    try:
                        cell = grid[mouse_pos_y][mouse_pos_x]
                    except:
                        pass

                    # cant draw over agents
                    if not cell.is_start() and not cell.is_end():
                        cell.make_wall((10, 10, 10))

        draw_grid(grid, screen)
        pygame.display.flip()

        clock.tick(60) # 60 fps

    pygame.quit()

main()