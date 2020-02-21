import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from itertools import product
from SolverLogic import Puzzle
from SolverLogic import Solver

# Get initial state from user
board = input("Enter borad:- ")

# Initialize pygame
pygame.init()
dis = pygame.display.set_mode((900, 900))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)
ticks = 400
clock = pygame.time.Clock()

# Function returns loaction of blank space on the grid
def getLocationOfBlank(gameBoard):
    for i, j in product(range(3), range(3)):
        if gameBoard[i][j] is 0:
            return i, j

# Function takes care of animation of the game board. It receives 2 boards at a time animate transition from one to
# another.
def animate(prevGameBoard, newGameBoard):
    xVel, yVel = 0, 0
    prevX, prevY = getLocationOfBlank(prevGameBoard)
    newX, newY = getLocationOfBlank(newGameBoard)
    if prevX < newX:
        yVel = -1
    elif prevX > newX:
        yVel = 1
    elif prevY < newY:
        xVel = -1
    elif prevY > newY:
        xVel = 1
    for count in range(300):
        dis.fill((35, 23, 9))
        for i, j in product(range(3), range(3)):
            if prevGameBoard[i][j] is not 0:
                if i is newX and j is newY:
                    pygame.draw.rect(dis, (255, 255, 255),
                                     pygame.Rect(j * 300 + 10 + (xVel * count), i * 300 + 10 + (yVel * count), 280,
                                                 280))
                    textsurface = myfont.render(str(prevGameBoard[i][j]), False, (0, 0, 0))
                    dis.blit(textsurface, (j * 300 + 125 + (xVel * count), i * 300 + 125 + (yVel * count)))
                else:
                    pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(j * 300 + 10, i * 300 + 10, 280, 280))
                    textsurface = myfont.render(str(prevGameBoard[i][j]), False, (0, 0, 0))
                    dis.blit(textsurface, (j * 300 + 125, i * 300 + 125))
        pygame.display.flip()
        clock.tick(ticks)


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

# Create object of Puzzle which stores gameBoard and its manipulation functions.
puzzle = Puzzle(gameBoard)
# Check if entered test case if solvable.
if puzzle.isSolvable():
    # Create object of solver
    solver = Solver(puzzle)
    # Solve
    solved = solver.solve()
    # Convert the path to list for animation
    ans = []
    for node in solved:
        ans.append(node.currentBorad.gameBoard)
    # Animate
    for i in range(len(ans) - 1):
        animate(ans[i], ans[i + 1])
else:
    print("Entered game board is not Solvable.")

# Close PyGame window
pygame.quit()
