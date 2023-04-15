import pygame
import random

from cell import Cell
from algorithms import CooperativeAStar
from algorithms import ConflictedBasedSearch

# GLOBAL VARIABLES
WIDTH = 1080
HEIGHT = 720
SIZE = 24                       # Bigger SIZE --> Smaller tiles (best if multiple of HEIGHT)
CELL_LENGTH = HEIGHT // SIZE    # number of pixels per cell
NUM_AGENTS = 5                  # number of agents to be generated

grid = []
# Creates a 2D Array representation of the screen
# Made up of Cells w/ properties in cell.py
def init_grid(rows, cols):
    grid = [ [0 for j in range(SIZE)] for i in range(SIZE) ]

    for row in range(rows):
        for col in range(cols):
            grid[row][col] = Cell(row, col)

    for i in range(NUM_AGENTS):
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

# erases any walls from the screen
def clear_walls(grid):
    for row in range(0, HEIGHT, CELL_LENGTH):
        for col in range(0, HEIGHT, CELL_LENGTH):
            if grid[row//CELL_LENGTH][col//CELL_LENGTH].is_wall():
                grid[row//CELL_LENGTH][col//CELL_LENGTH].make_normal()

# helper fucntion that removes everything from the screen
def clear_screen(grid):
    for row in range(0, HEIGHT, CELL_LENGTH):
        for col in range(0, HEIGHT, CELL_LENGTH):
            grid[row//CELL_LENGTH][col//CELL_LENGTH].make_normal()

# changes the start and end points of agents
def randomize(grid, screen, rows, cols):
    clear_screen(grid)
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = Cell(row, col)

    for i in range(NUM_AGENTS):
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

def main():
    pygame.init()
    pygame.display.set_caption("Multi-Agent Path Planning Visualizer (MAPPV)")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    screen.fill((40, 40, 40))
    grid = init_grid(SIZE, SIZE)
    draw_grid(grid, screen)

    # buttons for clear, randomize, coopa*, cbs
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(24*CELL_LENGTH, 0*CELL_LENGTH, 12*CELL_LENGTH, 3*CELL_LENGTH))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(24*CELL_LENGTH, 3*CELL_LENGTH, 12*CELL_LENGTH, 3*CELL_LENGTH))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(24*CELL_LENGTH, 6*CELL_LENGTH, 12*CELL_LENGTH, 3*CELL_LENGTH))
    pygame.draw.rect(screen, (100, 0, 0), pygame.Rect(24*CELL_LENGTH, 9*CELL_LENGTH, 12*CELL_LENGTH, 3*CELL_LENGTH))

    pygame.display.flip()

    running = True
    dragging = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True

                mouse_pos_x = pygame.mouse.get_pos()[0]//CELL_LENGTH
                mouse_pos_y = pygame.mouse.get_pos()[1]//CELL_LENGTH

                if mouse_pos_x in range(24, 36) and mouse_pos_y in range(0, 3):
                    clear_walls(grid)
                if mouse_pos_x in range(24, 36) and mouse_pos_y in range(3, 6):
                    randomize(grid, screen, SIZE, SIZE)
                if mouse_pos_x in range(24, 36) and mouse_pos_y in range(6, 9):
                    CooperativeAStar()
                if mouse_pos_x in range(24, 36) and mouse_pos_y in range(9, 12):
                    ConflictedBasedSearch()

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_pos_x = pygame.mouse.get_pos()[0] // CELL_LENGTH  # normalize for grid indexing
                    mouse_pos_y = pygame.mouse.get_pos()[1] // CELL_LENGTH
                    
                    # prevents out of bounds errors
                    try:
                        cell = grid[mouse_pos_y][mouse_pos_x]
                        # cant draw over agents
                        if not cell.is_start() and not cell.is_end():
                            cell.make_wall((10, 10, 10))
                    except:
                        pass

        draw_grid(grid, screen)
        pygame.display.flip()

        clock.tick(60) # 60 fps

    pygame.quit()

main()