class Table:

    __start = []
    __work = []
    __finish = []

    def onTable(x):
        if __start:
            if __start[0] == x:
                return True
        if __work:
            if __work[0] == x:
                return True
        if __finish:
            if __finish[0] == x:
                return True
        return False
        