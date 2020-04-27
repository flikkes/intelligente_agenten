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
        if not self.on(x):
            if not self.on(y):
                if self.onTable(y):
                    if not self.__finish:
                        self.__table.remove(y)
                        self.__finish.append(y)
                        self.__finish.append(x)
                        self.__removeFromStart(x)
                        self.__removeFromTable(x)
                if y in self.__finish:
                    self.__finish.append(x)
                    self.__removeFromStart(x)
                    self.__removeFromTable(x)

    def __removeFromTable(self, x):
        if x in self.__table:
            self.__table.remove(x)

    def __removeFromStart(self, x):
        if x in self.__start:
            self.__start.remove(x)
            
            
    def on(self, x):
        if x in __start:
            return __start[-1] == x
        if x in __table:
            return False
        if x in __finish:
            return __finish[-1] == x
        return False
    
    def onTable(self, x):
        return x in __table