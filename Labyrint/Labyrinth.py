class Labyrinth:
    fields = []
    def __init__(self):
        self.fields = [
            [0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
            [1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
            [1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0],
            [0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0],
            [0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,1,1,3,1,0,0,0,0],
            [1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

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

    def __isInBoundaries(self, x, y):
        if y < 0 or y >= len(self.fields):
            return False
        if x < 0 or x >= len(self.fields[y]):
            return False
        return True
    



