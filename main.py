# TODO:
# The buttons / text do not scale with a change in size
# better colors
# center text

import pygame
import random

from cell import Cell
from CooperativeAStar import CooperativeAStar
from ConflictBasedSearch import ConflictedBasedSearch

# GLOBAL VARIABLES
WIDTH = 1080
HEIGHT = 720
SIZE = 9                        # Bigger SIZE --> Smaller tiles (best if multiple of HEIGHT)
CELL_LENGTH = HEIGHT // SIZE    # number of pixels per cell
NUM_AGENTS = 2                  # number of agents to be generated
AGENT_TEXT = []                 # information arrays for displaying text of start/end points
AGENTS = []

# Creates a 2D Array representation of the screen
# Made up of Cells w/ properties in cell.py
def init_grid(rows, cols, screen):
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
                x_coord = random_x * CELL_LENGTH
                y_coord = random_y * CELL_LENGTH
                AGENT_TEXT.append([screen, x_coord, y_coord, 'S' + str(i), random_color])
                AGENTS.append((random_y, random_x))
                break
        
        # ensure other start/end points are not written over
        while True:
            random_x = int(random.random() * SIZE)
            random_y = int(random.random() * SIZE)

            if not grid[random_y][random_x].is_start() and not grid[random_y][random_x].is_end(): 
                grid[random_y][random_x].make_end(random_color)
                x_coord = random_x * CELL_LENGTH
                y_coord = random_y * CELL_LENGTH
                AGENT_TEXT.append([screen, x_coord, y_coord, 'E' + str(i), random_color])
                AGENTS.append((random_y, random_x))
                break
    return grid

# Si = ith agents start 
# Ei = ith agents end
def draw_agent_text(screen, x_coord, y_coord, text, random_color):
    font = pygame.font.Font('freesansbold.ttf', 24)
    start_rect = pygame.draw.rect(screen, random_color, pygame.Rect(x_coord, y_coord, CELL_LENGTH, CELL_LENGTH))
    start_text = font.render(text, True, (255, 255, 255), random_color)
    screen.blit(start_text, start_rect)

# Uses grid to draw the updated array on screen
def draw_grid(grid, screen):
    for row in range(0, HEIGHT, CELL_LENGTH):
        for col in range(0, HEIGHT, CELL_LENGTH):
            pygame.draw.rect(screen, grid[row//CELL_LENGTH][col//CELL_LENGTH].color, pygame.Rect(col, row, CELL_LENGTH, CELL_LENGTH))
            for text in AGENT_TEXT:
                if text[1] == col and text[2] == row:
                    draw_agent_text(text[0], text[1], text[2], text[3], text[4])

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
    AGENT_TEXT.clear()
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
                x_coord = random_x * CELL_LENGTH
                y_coord = random_y * CELL_LENGTH
                AGENT_TEXT.append([screen, x_coord, y_coord, 'S' + str(i), random_color])
                break
        
        # ensure other start/end points are not written over
        while True:
            random_x = int(random.random() * SIZE)
            random_y = int(random.random() * SIZE)

            if not grid[random_y][random_x].is_start() and not grid[random_y][random_x].is_end(): 
                grid[random_y][random_x].make_end(random_color)
                x_coord = random_x * CELL_LENGTH
                y_coord = random_y * CELL_LENGTH
                AGENT_TEXT.append([screen, x_coord, y_coord, 'E' + str(i), random_color])
                break

# draw wall helper funciton
def draw_wall(grid):
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

# adds button text
def setup_screen(screen):
    font = pygame.font.Font('freesansbold.ttf', 64)
    clear_text = font.render('Clear', True, (255, 255, 255), (255, 0, 0))
    clear_rect = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(HEIGHT, 0*HEIGHT//4, 12*CELL_LENGTH, 3*CELL_LENGTH))
    screen.blit(clear_text, clear_rect)

    rand_text = font.render('Randomize', True, (255, 255, 255), (0, 255, 0))
    rand_rect = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(HEIGHT, 1*HEIGHT//4, 12*CELL_LENGTH, 3*CELL_LENGTH))
    screen.blit(rand_text, rand_rect)

    coop_text = font.render('Coop A*', True, (255, 255, 255), (0, 0, 255))
    coop_rect = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(HEIGHT, 2*HEIGHT//4, 12*CELL_LENGTH, 3*CELL_LENGTH))
    screen.blit(coop_text, coop_rect)

    cbs_text = font.render('CBS', True, (255, 255, 255), (100, 0, 0))
    cbs_rect = pygame.draw.rect(screen, (100, 0, 0), pygame.Rect(HEIGHT, 3*HEIGHT//4, 12*CELL_LENGTH, 3*CELL_LENGTH))
    screen.blit(cbs_text, cbs_rect)

def main():
    pygame.init()
    pygame.display.set_caption("Multi-Agent Path Planning Visualizer (MAPPV)")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    screen.fill((40, 40, 40))
    grid = init_grid(SIZE, SIZE, screen)
    draw_grid(grid, screen)
    setup_screen(screen)

    pygame.display.flip()

    running = True
    dragging = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_wall(grid)
                dragging = True

                mouse_pos_x = pygame.mouse.get_pos()[0]
                mouse_pos_y = pygame.mouse.get_pos()[1]

                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(0*HEIGHT//4, 1*HEIGHT//4):
                    clear_walls(grid)
                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(1*HEIGHT//4, 2*HEIGHT//4):
                    randomize(grid, screen, SIZE, SIZE)
                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(2*HEIGHT//4, 3*HEIGHT//4):
                    CooperativeAStar()
                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(3*HEIGHT//4, 4*HEIGHT//4):
                    paths = ConflictedBasedSearch(grid, AGENTS)
                    print(paths)
                    for path in paths:
                        for cell in path[1:len(path)-1]:
                            x, y = cell.col, cell.row
                            pygame.draw.rect(screen, (255,0,0), pygame.Rect(x*CELL_LENGTH, y*CELL_LENGTH, CELL_LENGTH, CELL_LENGTH))
                            pygame.time.delay(200)
                            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    draw_wall(grid)

        # draw_grid(grid, screen)
        pygame.display.flip()
        clock.tick(60) # 60 fps

    pygame.quit()
    
main()