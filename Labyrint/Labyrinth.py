import random
import math


class Labyrinth:
    fields = []
    dimension = {"x": 0, "y": 0}
    startx = 0
    starty = 0
    finished = False

    def __init__(self, x=15, y=15, startx=4, starty=0, finishx=2, finishy=9):
        self.dimension["x"] = x
        self.dimension["y"] = y
        self.startx = startx
        self.starty = starty
        for i in range(y):
            self.fields.append([])
            for j in range(x):
                self.fields[i].append(1)
        mainPath = self.drawRandomPath(startx, starty, finishx, finishy, True)

        randomStart = mainPath[random.randint(1, len(mainPath)-2)]
        randomFinish = {"x": random.randint(
            0, self.dimension["x"]), "y": random.randint(0, self.dimension["y"])}
        while not self.isWall(randomFinish["x"], randomFinish["y"]) and self.getNumberOfWalkableNeighbors(randomFinish["x"], randomFinish["y"]) != 0:
            randomFinish = {"x": random.randint(
                0, self.dimension["x"]), "y": random.randint(0, self.dimension["y"])}
        nextPath = self.drawRandomPath(
            randomStart["x"], randomStart["y"], randomFinish["x"], randomFinish["y"])

    def drawRandomPath(self, startx, starty, finishx, finishy, initial = False):
        cx = startx
        cy = starty
        path = [{"x": cx, "y": cy}]
        print("current: {}, {}; desired: {}, {}".format(cx, cy, finishx, finishy))
        while cx != finishx or cy != finishy:
            
            valid = False
            moves = self.getPossibleMoves(cx, cy)
            backTrack = 0
            while not valid:
                move = moves[random.randint(0, len(moves))-1]
                valid = self.isInsideMaze(
                    move["x"], move["y"]) and move not in path and self.getNumberOfWalkableNeighbors(move["x"], move["y"]) < 2
                if not valid:
                    moves.remove(move)
                if not moves:
                    backTrack += 1
                    backIndex = len(path)-backTrack
                    if backIndex > len(path)-1 or backIndex < 0 and not initial:
                        return path
                    if  backIndex < 0 or not path:
                        return self.drawRandomPath(startx, starty, finishx, finishy, initial)
                    backTrackedPosition = path[backIndex]
                    moves = self.getPossibleMoves(backTrackedPosition["x"], backTrackedPosition["y"])
            cx = move["x"]
            cy = move["y"]
            if cx == startx and cy == starty:
                self.fields[cy][cx] = 2
            elif cx == finishx and cy == finishy and initial:
                self.fields[cy][cx] = 3
            else:
                self.fields[cy][cx] = 0
            print("current: {}, {}; desired: {}, {}".format(cx, cy, finishx, finishy))
            path.append(move)
        return path

    def getPossibleMoves(self, x, y):
        moves = []
        if self.isInsideMaze(x, y):
            if not self.isAtBottomBorder(y):
                moves.append({"x": x, "y": y+1})
            if not self.isAtTopBorder(y):
                moves.append({"x": x, "y": y-1})
            if not self.isAtLeftBorder(x):
                moves.append({"x": x-1, "y": y})
            if not self.isAtRightBorder(x):
                moves.append({"x": x+1, "y": y})
        return moves

    def isInsideMaze(self, x, y):
        return y < self.dimension["y"] and y >= 0 and x < self.dimension["x"] and x >= 0

    def getNumberOfWalkableNeighbors(self, x, y):
        walkableNeighbors = 0
        if not self.isWall(x-1, y):
            walkableNeighbors += 1
        if not self.isWall(x + 1, y):
            walkableNeighbors += 1
        if not self.isWall(x, y-1):
            walkableNeighbors += 1
        if not self.isWall(x, y+1):
            walkableNeighbors += 1
        return walkableNeighbors

    def isAtBottomBorder(self, y):
        return y == self.dimension["y"] - 1

    def isAtTopBorder(self, y):
        return y == 0

    def isAtLeftBorder(self, x):
        return x == 0

    def isAtRightBorder(self, x):
        return x == self.dimension["x"] - 1

    def isWall(self, x, y):
        if y < 0 or y >= len(self.fields):
            return True
        if x < 0 or x >= len(self.fields[y]):
            return True
        if self.fields[y][x] == 1:
            return True
        return False

    def isPath(self, x, y):
        if not self.__isInBoundaries(x, y):
            return False
        return self.fields[y][x] == 0

    def isStart(self, x, y):
        if not self.__isInBoundaries(x, y):
            return False
        return self.fields[y][x] == 2

    def isFinish(self, x, y):
        if not self.__isInBoundaries(x, y):
            return False
        return self.fields[y][x] == 3

    def isVisited(self, x, y):
        if not self.__isInBoundaries(x, y):
            return False
        return self.fields[y][x] == 4

    def visit(self, x, y):
        if not self.__isInBoundaries(x, y):
            return False
        self.fields[y][x] = 4
        return True

    def isWalkable(self, x, y):
        return not self.isVisited(x, y) and not self.isWall(x, y)

    def __isInBoundaries(self, x, y):
        if y < 0 or y >= len(self.fields):
            return False
        if x < 0 or x >= len(self.fields[y]):
            return False
        return True
