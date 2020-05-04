class Table:

    start = []
    table = []
    finish = []

    def __init__(self, start, table, finish):
        self.start = start
        self.table = table
        self.finish = finish

    def onGround(self, x):
        if self.start:
            if self.start[0] == x:
                return True
        if self.table:
            if self.table[0] == x:
                return True
        if self.finish:
            if self.finish[0] == x:
                return True
        return False
    
    def stack(self, x, y):
        if self.clear(x) and self.clear(y):
            if self.onTable(y):
                self.table.append(x)
                self.__removeFromStart(x)
                self.__removeFromFinish(x)
                return True
            if y in self.finish:
                self.finish.append(x)
                self.__removeFromStart(x)
                self.__removeFromTable(x)
                return True
            if  y in self.start:
                self.start.append(x)
                self.__removeFromFinish(x)
                self.__removeFromTable(x)
                return True
        return False

    def __removeFromTable(self, x):
        if x in self.table:
            self.table.remove(x)
            return True
        return False

    def __removeFromStart(self, x):
        if x in self.start:
            self.start.remove(x)
            return True
        return False

    def __removeFromFinish(self, x):
        if x in self.finish:
            self.finish.remove(x)
            return True
        return False            
            
    def clear(self, x):
        if self.start:
            if self.start[-1] == x:
                return True
        if self.table:
            if self.table[-1] == x:
                return True
        if self.finish:
            if self.finish[-1] == x:
                return True
        return False
    
    def onTable(self, x):
        return x in self.table

    def on(self, x, y):
        if x in self.start and y in self.start:
            return self.__on(x, y, self.start)
        if x in self.table and y in self.table:
            return self.__on(x, y, self.table)
        if x in self.finish and y in self.finish:
            return self.__on(x, y, self.finish)
        return False


    def __on(self, x, y, arr):
        xIndex = arr.index(x)
        return arr.index(y) == xIndex-1

    def putDown(self, x):
        if self.clear(x):
            self.table.append(x)
            self.__removeFromStart(x)
            self.__removeFromFinish(x)
            return True
        return False
