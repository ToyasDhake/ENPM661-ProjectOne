from itertools import chain, product
from collections import deque
from copy import deepcopy
import numpy as np


# Node class contains current puzzle state, parent, index and score
class Node:
    def __init__(self, currentBorad, index, parent=None, action=None):
        self.currentBorad = currentBorad
        self.parent = parent
        self.action = action
        self.index = index
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0
        self.f = self.g + currentBorad.score()

    # Returns the path from initial state to current state.
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    # Returns current available moves
    def actions(self):
        if self.action == None:
            return self.currentBorad.availbleMoves()
        else:
            return self.currentBorad.availbleMoves(self.action)

# Solver class solve the puzzle
class Solver:
    def __init__(self, gameBoard):
        self.start = gameBoard

    # Solves the puzzle and returns path from initial state to goal state.
    def solve(self):
        count = 1
        queue = deque()
        self.que = deque()
        queue.append(Node(self.start, count))
        self.que.append(Node(self.start, count))
        count += 1
        seen = set()
        seen.add(queue[0].currentBorad)
        while queue:
            queue = deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.currentBorad.score() == 0:
                self.que = deque(sorted(list(self.que), key=lambda node: node.index))
                return node.path()

            for action in node.actions():
                child = Node(node.currentBorad.move(action), count, node, action)

                if child.currentBorad not in seen:
                    self.que.append(Node(node.currentBorad.move(action), count, node, action))
                    count += 1
                    queue.appendleft(child)
                    seen.add(child.currentBorad)


# Puzzle class keeps track of current state of gameBoard and all gameBoard related activities such as finding
# possible moves, performing actions, calculating score and finding the location of blank space.
class Puzzle:
    def __init__(self, gameBoard):
        self.gameBoard = gameBoard

    # Checks is the gameBoard is Solvable.
    def isSolvable(self):
        count = 0
        array = np.array(self.gameBoard).flatten()
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    if array[j] != 0:
                        count += 1
        if count % 2 is 0:
            return True
        else:
            return False

    # Returns the location of black space on gameBorad
    def getLocationOfBlank(self, gameBoard):
        for i, j in product(range(3), range(3)):
            if gameBoard[i][j] is 0:
                return i, j

    # Returns score of current state. It is the summation of distance of blocks from where they are supposed to be.
    def score(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.gameBoard[i][j] != 0:
                    x, y = divmod(self.gameBoard[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    # Returns all possible moves.
    def availbleMoves(self, removeCh="A"):
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
        # Remove the action taken by parent so as to not end up same as parent.
        if removeCh != "A":
            if removeCh == "U":
                list.remove("D")
            elif removeCh == "D":
                list.remove("U")
            elif removeCh == "R":
                list.remove("L")
            elif removeCh == "L":
                list.remove("R")
        return list

    # Perform the action on gameBoard.
    def move(self, val):
        row, col = self.getLocationOfBlank(self.gameBoard)
        newGameBoard = deepcopy(self)
        if val is 'U':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row - 1][col] = newGameBoard.gameBoard[row - 1][
                                                                                         col], \
                                                                                     newGameBoard.gameBoard[row][col]
        elif val is 'D':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row + 1][col] = newGameBoard.gameBoard[row + 1][
                                                                                         col], \
                                                                                     newGameBoard.gameBoard[row][col]
        elif val is 'L':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row][col - 1] = newGameBoard.gameBoard[row][
                                                                                         col - 1], \
                                                                                     newGameBoard.gameBoard[row][col]
        elif val is 'R':
            newGameBoard.gameBoard[row][col], newGameBoard.gameBoard[row][col + 1] = newGameBoard.gameBoard[row][
                                                                                         col + 1], \
                                                                                     newGameBoard.gameBoard[row][col]
        return newGameBoard
