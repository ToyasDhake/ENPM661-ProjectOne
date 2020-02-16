from itertools import chain, product
from collections import deque
from copy import deepcopy


class Node:
    def __init__(self, currentBorad, parent=None, action=None):
        self.currentBorad = currentBorad
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0
        self.f = self.g + currentBorad.score()

    @property
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def actions(self):
        return self.currentBorad.availbleMoves()


class Solver:
    def __init__(self, gameBoard):
        self.start = gameBoard

    def solve(self):
        queue = deque()
        queue.append(Node(self.start))
        seen = set()
        seen.add(queue[0].currentBorad)
        while queue:
            queue = deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.currentBorad.score() == 0:
                return node.path

            for action in node.actions:
                child = Node(node.currentBorad.move(action), node, action)

                if child.currentBorad not in seen:
                    queue.appendleft(child)
                    seen.add(child.currentBorad)


class Puzzle:
    def __init__(self, gameBoard):
        self.gameBoard = gameBoard

    def getLocationOfBlank(self, gameBoard):
        for i, j in product(range(3), range(3)):
            if gameBoard[i][j] is 0:
                return i, j

    def printBorad(self):
        for row in self.gameBoard:
            print(row)
        print("xxxxxxxxx")

    def checkIfSolvable(self):
        counter = 0
        newList = list(chain.from_iterable(self.gameBoard))
        for i in range(9):
            for j in range(9):
                if i < j:
                    if newList[i] > newList[j]:
                        if newList[j] is not 0:
                            counter += 1

        if counter % 2 is 0:
            return True
        else:
            return False

    def score(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.gameBoard[i][j] != 0:
                    x, y = divmod(self.gameBoard[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def availbleMoves(self):
        row, col = self.getLocationOfBlank(self.gameBoard)
        list = []
        if row is not 0:
            list.append("U")
        if row is not 2:
            list.append("D")
        if col is not 0:
            list.append("L")
        if col is not 2:
            list.append("R")
        return list

    def move(self, val):
        row, col = self.getLocationOfBlank(self.gameBoard)
        newGameBoard = deepcopy(self)
        if val is 'U':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row - 1][col] = newGameBoard.gameBoard[row - 1][col], newGameBoard.gameBoard[row][col]
        elif val is 'D':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row + 1][col] = newGameBoard.gameBoard[row + 1][col], newGameBoard.gameBoard[row][col]
        elif val is 'L':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row][col - 1] = newGameBoard.gameBoard[row][col- 1], newGameBoard.gameBoard[row][col]
        elif val is 'R':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row][col + 1] = newGameBoard.gameBoard[row][col + 1], newGameBoard.gameBoard[row][col]
        return newGameBoard



gameBoard = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
puzzle = Puzzle(gameBoard)
solver = Solver(puzzle)
solved = solver.solve()
steps = 0
for node in solved:
    print(node.action)
    print(node.currentBorad.gameBoard)
    steps += 1
