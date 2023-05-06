## Leading Question

How can we path plan in a situation where there are multiple agents (people, cars, etc.) and still avoid collisions whilst moving simultaneously?

## Output and correctness of each algorithm

### Cooperative A*:

### Conflict-Based Search:

## The answer to our leading question

Via an underlying path finding algorithm, in this case A*, we can find individual optimal paths for each of our agents and analyze/modify the paths using a "wait" command that can delay the movement of agents. This results in less optimal pathing but ensures no collisions occurs. 