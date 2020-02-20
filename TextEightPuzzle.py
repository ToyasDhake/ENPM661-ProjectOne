from AStar import Puzzle
from AStar import Solver
import time


board = input("Enter borad:- ")
board = board.replace(" ", "")
board = list(board)

gameBoard = []
count = 0
for _ in range(3):
    temp = []
    for _ in range(3):
        temp.append(int(board[count]))
        count += 1
    gameBoard.append(temp)


def listToString(board):
    state = ""
    for row in board:
        for element in row:
            state = state + str(element) + " "
    return state[:-1]

puzzle = Puzzle(gameBoard)
if puzzle.isSolvable():
    solver = Solver(puzzle)
    start = time.clock()
    solved = solver.solve()
    end = time.clock()
    file1 = open("nodePath.txt", "w")
    for node in solved:
        file1.write(listToString(node.currentBorad.gameBoard) + "\n")
        print(node.action)
    file1.close()
    file2 = open("Nodes.txt", "w")
    file3 = open("NodesInfo.txt", "w")
    while solver.que:
        node = solver.que.popleft()
        if node.parent == None:
            file2.write(listToString(node.currentBorad.gameBoard) + "\n")
            file3.write(str(node.index) + " 0\n")
        else:
            file2.write(listToString(node.currentBorad.gameBoard) + "\n")
            file3.write(str(node.index)+" "+str(node.parent.index)+"\n")
    file2.close()
    file3.close()
    print("Time taken: " + str(end - start) + " seconds.")
else:
    print("Entered game board is not Solvable.")