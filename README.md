# Multi-Agent Path Planning Visualizer (MAPPV)
Visualize Cooperative A* and Conflict-Based Search with PyGame

Created by Ian Sornson (gis3), Anes Kim (anesk2), and Akaash Kashyap (akash8)

# Link to video presentation

# Documentation

[Original Goals](https://github.com/Sorsmo/MAPP-Visualizer/blob/main/documentation/goals.md)

[Team Contract](https://github.com/Sorsmo/MAPP-Visualizer/blob/main/documentation/contract.md)

[Dev Log](https://github.com/Sorsmo/MAPP-Visualizer/blob/main/documentation/devlog.md)

[Results](https://github.com/Sorsmo/MAPP-Visualizer/blob/main/documentation/results.md)

# Installation & Setup

Clone the repository with `git clone https://github.com/Sorsmo/MAPP-Visualizer.git`

Install PyGame with `pip install pygame` or `pip3 install pygame`

cd into your new directory and run main.py 

Adjust the number of agents / size of grid with the global variables at the top of main.py

# Features

The PyGame visualizer allows the user to draw walls/obstacles on the screen to create intricate scenarios
Buttons on the right side of the screen include options to clear the walls currently on screen, randomize the agent stat and end points, and pick with algorithm to run

The user has access to two different algorithms, Cooperative A* and Conflict-Based Search

Both algorithms utilize A* on an unweighted and undirected graph as the underlying path planning algorithm

# File Breakdown

1. main.py
    - Contains all the PyGame code to visualize our two algorithms
2. cell.py
    - Class for each square in our grid
    - Contains properties to distinguish cells as agents, start and end points, walls, empty space, and set colors
3. ConflictBasedSearch.py
    - Code for the conflict-based search algorithm
4. CooperativeAStar.py
    - Implementation for the Cooperative A* algorithm
