# Anes
from queue import PriorityQueue
import hashlib

def CooperativeAStar(grid, AGENTS):
    paths = []
    agent_hashes = [set() for _ in AGENTS]

    for i in range(0, len(AGENTS), 2):
        agent_start = grid[AGENTS[i][0]][AGENTS[i][1]]
        agent_end = grid[AGENTS[i + 1][0]][AGENTS[i + 1][1]]
        path = astar(grid, agent_start, agent_end, agent_hashes[i])
        paths.append(path) 
    
    for i in range (1, len(paths) - 1):
        for j in range(len(paths[i])):
            if j < len(paths[i]):
                if paths[i][j] == paths[i][j] and j != 0:
                    lengthen = paths[i][:j] + [paths[i][j]] + paths[i][j:]
                    paths[i] = lengthen
                    break

    return paths

def astar(grid, start, goal, agent_hash):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):
            tentative_g_score = g_score[current] + get_cost(current, neighbor)

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                agent_state = tuple([(cell.col, cell.row) for cell in (neighbor, goal)])
                agent_hash_code = hashlib.md5(str(agent_state).encode()).hexdigest()
                
                if agent_hash_code in agent_hash:
                    continue

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                frontier.put((f_score[neighbor], neighbor))

                # Add the hash code to the agent's hash table
                agent_hash.add(agent_hash_code)

    path = []
    current = goal

    while current != start:
        path.append(current)
        try:
            current = came_from[current]
        except:
            return []

    path.append(start)
    path.reverse()

    return path


# so that one path cannot collide with other
"""def block_path(path, grid, agents):
   colors = grid[agents[0]][agents[1]].color
   for i in range(1, len(path) - 1):
       path[i].make_wall(colors)"""


def heuristic(neighbor, goal):
    x1, y1 = neighbor.col, neighbor.row
    x2, y2 = goal.col, goal.row
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(grid, cell):
    neighbors = []
    x, y = cell.col, cell.row

    if x > 0 and not grid[y][x - 1].is_wall():
        neighbors.append(grid[y][x - 1])
    if x < len(grid[0]) - 1 and not grid[y][x + 1].is_wall():
        neighbors.append(grid[y][x + 1])
    if y > 0 and not grid[y - 1][x].is_wall():
        neighbors.append(grid[y - 1][x])
    if y < len(grid) - 1 and not grid[y + 1][x].is_wall():
        neighbors.append(grid[y + 1][x])

    return neighbors

def get_cost(cell1, cell2):
    if cell1.col == cell2.col or cell1.row == cell2.row:
        return 1    # adjacent cells
    else:
        return 1.4  # diagonal cells
    