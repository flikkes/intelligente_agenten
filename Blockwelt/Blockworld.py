class World:

    start = []
    table = []
    finish = []
    hand = None

    def __init__(self, start, table, finish):
        self.start = start
        self.table = table
        self.finish = finish

    def onground(self, x):
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
    
    def holds(self, x):
        return self.hand == x
    
    def stack(self, x, y):
        if self.holds(x) and self.clear(y):
            if y in self.table:
                self.table.append(x)
                self.hand = None
                return True
            if y in self.finish:
                self.finish.append(x)
                self.hand = None
                return True
            if  y in self.start:
                self.start.append(x)
                self.hand = None
                return True
        return False

    def unstack(self, x, y):
        if self.clear(x) and self.on(x, y) and self.handempty():
            self.hand = x
            self.__removeFromStart(x)
            self.__removeFromTable(x)
            self.__removeFromFinish(x)
            return True
        return False


    def handempty(self):
        return self.hand == None

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

    def putdown(self, x):
        if self.holds(x):
            if not self.start:
                self.start.append(x)
                self.hand = None
                return True
            if not self.table:
                self.table.append(x)
                self.hand = None
                return True
            if not self.finish:
                self.finish.append(x)
                self.hand = None
                return True
        return False

    def pickup(self, x):
        if self.handempty():
            if len(self.start) == 1 and self.start[0] == x:
                self.hand = x
                self.__removeFromStart(x)
                return True
            if len(self.table) == 1 and self.table[0] == x:
                self.hand = x
                self.__removeFromTable(x)
                return True
            if len(self.finish) == 1 and self.finish[0] == x:
                self.hand = x
                self.__removeFromFinish(x)
                return True
        return False
