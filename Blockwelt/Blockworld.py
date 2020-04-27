class Table:

    __start = []
    __table = []
    __finish = []

    def onGround(self, x):
        if self.__start:
            if self.__start[0] == x:
                return True
        if self.__table:
            if x in self.__table:
                return True
        if self.__finish:
            if self.__finish[0] == x:
                return True
        return False
    
    def stack(self, x, y):
        if self.clear(x) and self.clear(y):
            if self.onTable(y):
                if not self.__finish:
                    self.__finish.append(y)
                    self.__finish.append(x)
                    self.__removeFromTable(y)
                    self.__removeFromStart(x)
                    self.__removeFromTable(x)
                    return True
            if y in self.__finish:
                self.__finish.append(x)
                self.__removeFromStart(x)
                self.__removeFromTable(x)
                return True
            if  y in self.__start:
                self.__start.append(x)
                self.__removeFromFinish(x)
                self.__removeFromTable(x)
                return True
        return False

    def __removeFromTable(self, x):
        if x in self.__table:
            self.__table.remove(x)
            return True
        return False

    def __removeFromStart(self, x):
        if x in self.__start:
            self.__start.remove(x)
            return True
        return False

    def __removeFromFinish(self, x):
        if x in self.__finish:
            self.__finish.remove(x)
            return True
        return False            
            
    def clear(self, x):
        if x in self.__start:
            return self.__start[-1] == x
        if x in self.__table:
            return True
        if x in self.__finish:
            return self.__finish[-1] == x
        return False
    
    def onTable(self, x):
        return x in self.__table

    def on(self, x, y):
        if x in self.__start:
            return self.__on(x, y, self.__start)
        if x in self.__finish:
            return self.__on(x, y, self.__finish)
        return False


    def __on(self, x, y, arr):
        xIndex = arr.index(x)
        return arr.index(y) == xIndex-1

    def putDown(self, x):
        if self.clear(x):
            self.__table.append(x)
            self.__removeFromStart(x)
            self.__removeFromFinish(x)
            return True
        return False
