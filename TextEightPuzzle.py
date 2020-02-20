from AStar import Puzzle
from AStar import Solver

gameBoard = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
puzzle = Puzzle(gameBoard)
solver = Solver(puzzle)
solved = solver.solve()
steps = 0
for node in solved:
    print(node.action)
    print(node.currentBorad.gameBoard)
    steps += 1
