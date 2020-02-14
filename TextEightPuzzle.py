from itertools import chain, product


class Solver:
    pass


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
        list = [0] * 4
        if row is not 0:
            list[0] = 1
        if row is not 2:
            list[1] = 1
        if col is not 0:
            list[2] = 1
        if col is not 2:
            list[3] = 1
        return list

gameBoard = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
puzzle = Puzzle(gameBoard)
