from SolverLogic import Puzzle
from SolverLogic import Solver

# Get initial state from user
board = input("Enter borad:- ")

# Converts user input to 3x3 matrix used by solver algorithm
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


# Converts the 3x3 matrix to string to be written in the text file
def listToString(board):
    state = ""
    for i in range(3):
        for j in range(3):
            state = state + str(board[j][i]) + " "
    return state[:-1]


# Create object of Puzzle which stores gameBoard and its manipulation functions.
puzzle = Puzzle(gameBoard)
# Check if entered test case if solvable.
if puzzle.isSolvable():
    # Create object of solver
    solver = Solver(puzzle)
    # Solve
    solved = solver.solve()
    # Create nodePath.txt
    file1 = open("nodePath.txt", "w")
    for node in solved:
        file1.write(listToString(node.currentBorad.gameBoard) + "\n")
        print(node.action)
    file1.close()
    # Create NodesInfo.txt and Nodes.txt
    file2 = open("Nodes.txt", "w")
    file3 = open("NodesInfo.txt", "w")
    while solver.que:
        node = solver.que.popleft()
        # Check for initial node as it will not have a parent index.
        if node.parent == None:
            file2.write(listToString(node.currentBorad.gameBoard) + "\n")
            file3.write(str(node.index) + " 0\n")
        else:
            file2.write(listToString(node.currentBorad.gameBoard) + "\n")
            file3.write(str(node.index) + " " + str(node.parent.index) + "\n")
    file2.close()
    file3.close()
    print("Files generated.")
else:
    print("Entered game board is not Solvable.")
