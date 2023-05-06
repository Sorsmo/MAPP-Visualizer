## Leading Question

How can we path plan in a situation where there are multiple agents (people, cars, etc.) and still avoid collisions whilst moving simultaneously?

## Output and correctness of each algorithm

### Cooperative A*:
  We finished our implementation of Cooperative A* or CA* using hash tables for reservations so that agents in a specific order would get priority and others behind it would be delayed so that there is no collision. The visualizer was meant to be connected in one big path at the start of the run, and the cells disappear to show the path moving one cell at a time. If a cell at a certain time and position overlap at a certain point, the most recent one will delay itself by one to let the priority cells pass. We use multiple helper functions to find the most optimal path, incorporating the hashes as well.

### Conflict-Based Search:

  For Conflict-Based Search or the CBS algorithm we tested our algorithm using the visualizer we made earlier. The visualizer is an easy indicator to verify if the paths should cross and if they do cross. To double check the crossover we can also print out the points that each agent travels to see if they all equal the same at any point in time.
  
  Unfortunately we were not able to finish the implementation of CBS, the biggest issue we came across was implementing the tree portion of the algorithm. Instead we tried an alternative method that forces one of the agents to wait.

## The answer to our leading question

Via an underlying path finding algorithm, in this case A*, we can find individual optimal paths for each of our agents and analyze/modify the paths using a "wait" command that can delay the movement of agents. This results in less optimal pathing but ensures no collisions occurs. There is also the possibility that we could have the A* find unique paths for each agent, but it creates an even less optimal path. We had issues mainly with our visual aid in terms of showing each agents path by also clearly showing there was no collision if path lengths are close in distance. We ended up using a blinking aid to show the cells moving to its destination individually, one at a time. Otherwise, CA* works to the best of its ability,
