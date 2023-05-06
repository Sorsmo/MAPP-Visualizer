import pygame
import random

from cell import Cell
from CooperativeAStar import CooperativeAStar
from ConflictBasedSearch import ConflictedBasedSearch

# GLOBAL VARIABLES
WIDTH = 1080
HEIGHT = 720
NUM_AGENTS = 2                  # number of agents to be generated
AGENT_TEXT = []                 # information arrays for displaying text of start/end points
AGENTS = []
ANIMATION_DELAY = 400           # delay between each step of the algorithm

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
            cell = grid[row//CELL_LENGTH][col//CELL_LENGTH]
            if cell.is_wall() or cell.is_path():
                cell.make_normal()

# helper fucntion that removes everything from the screen
def clear_screen(grid):
    for row in range(0, HEIGHT, CELL_LENGTH):
        for col in range(0, HEIGHT, CELL_LENGTH):
            grid[row//CELL_LENGTH][col//CELL_LENGTH].make_normal()

# changes the start and end points of agents
def randomize(grid, screen, rows, cols):
    AGENTS.clear()
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
    clear_text = font.render('Clear', True, (255, 255, 255), (32, 42, 68))
    clear_rect = pygame.draw.rect(screen, (32, 42, 68), pygame.Rect(HEIGHT, 0*HEIGHT//4, 12*CELL_LENGTH, 180))
    screen.blit(clear_text, clear_rect)

    rand_text = font.render('Randomize', True, (255, 255, 255), (52, 62, 88))
    rand_rect = pygame.draw.rect(screen, (52, 62, 88), pygame.Rect(HEIGHT, 1*HEIGHT//4, 12*CELL_LENGTH, 180))
    screen.blit(rand_text, rand_rect)

    coop_text = font.render('Coop A*', True, (255, 255, 255), (72, 82, 108))
    coop_rect = pygame.draw.rect(screen, (72, 82, 108), pygame.Rect(HEIGHT, 2*HEIGHT//4, 12*CELL_LENGTH, 180))
    screen.blit(coop_text, coop_rect)

    cbs_text = font.render('CBS', True, (255, 255, 255), (92, 102, 128))
    cbs_rect = pygame.draw.rect(screen, (92, 102, 128), pygame.Rect(HEIGHT, 3*HEIGHT//4, 12*CELL_LENGTH, 180))
    screen.blit(cbs_text, cbs_rect)

# helper function for drawing to the screen
def updateScreen(grid, colors, paths, step, screen):
    done = 0
    for i in range(len(paths)):
        done += updateGrid(grid, colors[i], paths[i], step, screen)
    draw_grid(grid, screen)
    pygame.display.flip()
    pygame.time.delay(ANIMATION_DELAY)
    return done

# updates the grid with the path but does not update the screen
def updateGrid(grid, color, path, step, screen):
    if step >= len(path):
        return 1 # done
    cell = path[step]
    x, y = cell.col, cell.row
    if not grid[y][x].is_start() and not grid[y][x].is_end():
        grid[y][x].make_normal()
        grid[y][x].make_path(color)

    if step > 1:
        prev_cell = path[step - 1]
        x, y = prev_cell.col, prev_cell.row
        if not grid[y][x].is_start() or not grid[y][x].is_end():
            grid[y][x].make_normal()

    return 0 # not done

# sets up agent numbers and cell size
def main_prolouge():
    global NUM_AGENTS
    global SIZE
    global CELL_LENGTH

    size_str = ''
    sizes = ['small', 'medium', 'large']
    
    NUM_AGENTS = int(input("How many agents do you want on screen? "))

    i = 0
    while size_str not in sizes:
        if i > 0:
            print('Incorrect input, please try again.')
        size_str = input("Do you want a small, medium, or large grid? ").lower()
        i += 1

    if size_str == 'small':
        SIZE = 9
    elif size_str == 'medium':
        SIZE = 15
    elif size_str == 'large':
        SIZE = 24

    CELL_LENGTH = HEIGHT // SIZE

    main()

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

                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(0, 180):
                    clear_walls(grid)
                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(180, 360):
                    randomize(grid, screen, SIZE, SIZE)
                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(360, 540):
                    paths = CooperativeAStar(grid, AGENTS)
                    colors = [grid[AGENTS[i][0]][AGENTS[i][1]].color for i in range(0, len(AGENTS), 2)]

                    done = 0
                    step = 0
                    while done != len(paths): # done has to be = to 2 for 2 agents
                        done = 0
                        done = updateScreen(grid, colors, paths, step, screen) # update grid at each time interval
                        step += 1 

                if mouse_pos_x in range(HEIGHT, WIDTH) and mouse_pos_y in range(540, 720):
                    paths = ConflictedBasedSearch(grid, AGENTS)
                    colors = [grid[AGENTS[i][0]][AGENTS[i][1]].color for i in range(0, len(AGENTS), 2)]
                    print('printed paths')
                    for p0, p1 in zip(paths[0], paths[1]):
                        print(p0.pos(), p1.pos())
                              
                    done = 0
                    step = 0
                    while done != len(paths): # done has to be = to 2 for 2 agents
                        done = 0
                        done = updateScreen(grid, colors, paths, step, screen) # update grid at each time interval
                        step += 1 
           
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    draw_wall(grid)

        draw_grid(grid, screen)
        pygame.display.flip()
        clock.tick(60) # 60 fps

    pygame.quit()
    
main_prolouge()