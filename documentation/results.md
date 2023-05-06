## Leading Question

How can we path plan in a situation where there are multiple agents (people, cars, etc.) and still avoid collisions whilst moving simultaneously?

## Output and correctness of each algorithm

### Cooperative A*:

### Conflict-Based Search:

  For Conflict-Based Search or the CBS algorithm we tested our algorithm using the visualizer we made earlier. The visualizer is an easy indicator to verify if the paths should cross and if they do cross. To double check the crossover we can also print out the points that each agent travels to see if they all equal the same at any point in time.
  
  Unfortunately we were not able to finish the implementation of CBS, the biggest issue we came across was implementing the tree portion of the algorithm. Instead we tried an alternative method that forces one of the agents to wait.

## The answer to our leading question

Via an underlying path finding algorithm, in this case A*, we can find individual optimal paths for each of our agents and analyze/modify the paths using a "wait" command that can delay the movement of agents. This results in less optimal pathing but ensures no collisions occurs. 
