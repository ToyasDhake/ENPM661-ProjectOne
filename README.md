# ENPM661-ProjectOne: Biased BFS for 8-Puzzle Problem

## Overview

8 Puzzle problem is a puzzle game made of 3x3 grid consisting of 8 blocks numbered from 1 to 8 and one empty space.
Blocks can be slided into the empty space, do so we can manipulate the oriantation of the blocks. Goal is to get a specific
orientaion of blocks as shown in the figure.

![](Solved.png)

There are 3 files
- TextEightPuzzle.py
- GraphicalEightPuzzle.py
- SolverLogic.py
 
SolverLogic.py is the file which has implementatioon of 8 Puzzle problem solver.

TextEightPuzzle.py uses the SolverLogic.py to solve the problem and create required text files as output.

GraphicalEightPuzzle.py uses the SolverLogic.py to solve the problem and creates animation for solution 
from given state to goal state for visualization purpose.

## Logic

The algorithms takes in initial state as input and give out the path took to reach the goal node.
For this it creates all possible moves for any given states and checks if goal state is reached. If not then it again 
creates all possible nodes for each child node. To avoid getting stuck in loop 2 things are being tracked-
- A Set is maintained that holds all the explored nodes and each time a child is create it checks if the node is previously visited.
- While calculating all possible move the reverse of last performed move is not considered i.e. if a state is reached by performing the "Up" move
then for that perticular move the "Down" actioon will not be considered for creating child as it would result in parent of the node.

BFS takes a lot of time to excute so it is needed to be optimized in order to reduce the run time. Here, the biased part comes into picture. Every time 
a child is created its score is calculated based on where it stands compared to goal state. And child with better score is given priority.

## Demo Steps

Text base-

```
python TextEightPuzzle.py
0 1 2 3 4 5 6 7 8
```

Graphics base-

```
python GraphicalEightPuzzle.py
0 1 2 3 4 5 6 7 8
```

## Dependencies

Text base-

-  Numpy

Graphics base-

- Numpy
- PyGame

## Result

Text base-

Three files are genrated-

- nodePath.txt- Contains the path form initial state to goal state.

- Nodes.txt- Contains all the explored nodes.

- NodesInfo.txt- Contain index of the node and its parent.

Graphics base-

![](result.gif)