## Original Goals

1. GUI
    Set up start/end points
    Select number of agents
    Create walls/obstacles
    Pick path planning alogirthm
    Visualize the algorithm(s)
2. Cooperative A*
3. Conflict-Based Search
4. 3D representation of the path planning using x, y, and time axises (only if time permits)

## Dataset Acquisition and Processing
    No dataset

## Algorithms
    Cooperative A*: 
        Academic Reference: 
            https://www.davidsilver.uk/wp-content/uploads/2020/03/coop-path-AIIDE.pdf
            https://www.davidsilver.uk/wp-content/uploads/2020/03/coop-path-AIWisdom.pdf
        Function Inputs: 
            Graph representation of our environment including open spaces, obstacles, etc.
            Number of agents and their respective starting and end points.
            Since this uses A* we will probably include a heuristic such as the Manhattan Distance,
            True Distance, or Consistency.
        Function Outputs:
            N number of paths for N number of agents that will not collide when ran simultaneously.
            Visualized and simulated using PyGame. If time, the 3D representation of how the paths
            overlap, or is this case, don't overlap.
        Function Efficiency:
            The worst-case time complexity of CoopA* is exponential in the number of agents and the 
            size of the search space, since it explores all possible combinations of agent positions
            and actions. However, in practice, the time complexity of CoopA* can be improved by 
            using heuristics to reduce the number of explored states and by pruning the search space
            based on the constraints of the agents. Thus, our goal will be to have a time complexity
            that is less than exponential time.
    
    Conflict-Based Search:
        Academic Reference:
            https://people.engr.tamu.edu/guni/Papers/CBS-AAAI12.pdf
        Function Inputs: 
            Graph representation of our environment including open spaces, obstacles, etc.
            Number of agents and their respective starting and end points.
        Function Outputs:
            N number of paths for N number of agents that will not collide when ran simultaneously 
        Function Efficiency:
            The worst case of the CBS is also exponential, but we can find a best case solution 
            using Conflict Based BackJumping with time complexity of O(b^d) where b is the branching
            factor and d is the depth of the search tree. Thus, our goal will be to have a time  
            complexity less than the exponential time, and closer to the CBJ algorithm.
