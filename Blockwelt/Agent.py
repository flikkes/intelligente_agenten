import Blockworld
from Blockworld import World

class Agent:

    world = None
    goal = None

    def __init__(self, world, goal):
        self.world = world
        self.goal = goal

    def fulfillGoal(self):
        if self.matchesGoal():
            return True
        self.putAllOnStart()
        badCache = []
        lastGoodBlock = 'GND'
        lastTrashBlock = 'GND'
        while self.world.start and not self.partiallyMatchesGoal(self.world.start):
            print('test1')
            if self.matchesGoal():
                return True
            x = self.getClearBlockOfStack(self.world.start)
            self.raiseBlock(x)
            if self.goal.onground(x) and self.world.putdown(x):
                if lastGoodBlock != 'GND':
                    lastTrashBlock = x
                else:
                    lastGoodBlock = x
            elif self.goal.on(x, lastGoodBlock):
                self.world.stack(x, lastGoodBlock)
                lastGoodBlock = x
            else:
                if lastTrashBlock == 'GND':
                    self.world.putdown(x)
                else:
                    self.world.stack(x, lastTrashBlock)
                lastTrashBlock = x
        if self.matchesGoal():
                return True
        while not self.matchesGoal():
            print('test2')
            if lastTrashBlock in self.world.table:
                lastTrashBlock = 'GND'
                while self.world.table and not self.partiallyMatchesGoal(self.world.table):
                    print('test3')
                    if self.matchesGoal():
                        return True
                    x = self.getClearBlockOfStack(self.world.table)
                    self.raiseBlock(x)
                    if self.goal.onground(x):
                        self.world.putdown(x)
                        lastGoodBlock = x
                    elif self.goal.on(x, lastGoodBlock):
                        self.world.stack(x, lastGoodBlock)
                        lastGoodBlock = x
                    elif self.goal.on(x, self.getClearBlockFromOtherStack(x, lastGoodBlock)):
                        self.world.stack(x, self.getClearBlockFromOtherStack(x, lastGoodBlock))
                        lastGoodBlock = x
                    else:
                        if lastTrashBlock == 'GND':
                            self.world.putdown(x)
                            break
                        else:
                            self.world.stack(x, lastTrashBlock)
                        lastTrashBlock = x
            else:
                lastTrashBlock = 'GND'
                while self.world.finish:
                    print('test4')
                    if self.matchesGoal():
                        return True
                    x = self.getClearBlockOfStack(self.world.finish)
                    self.raiseBlock(x)
                    if self.goal.onground(x):
                        print('test5')
                        self.world.putdown(x)
                        lastGoodBlock = x
                    elif self.goal.on(x, lastGoodBlock):
                        self.world.stack(x, lastGoodBlock)
                        lastGoodBlock = x
                    else:
                        if lastTrashBlock == 'GND':
                            self.world.putdown(x)
                        else:
                            self.world.stack(x, lastTrashBlock)
                        lastTrashBlock = x
            self.swapWithUnderlying(lastTrashBlock)
        return True
            
    def swapWithUnderlying(self, x):
        moveTo = self.getClearBlockFromOtherStack(x, None)
        underX = self.getBlockUnder(x)
        if underX == 'GND':
            return
        self.raiseBlock(x)
        self.world.stack(x, moveTo)
        moveTo = self.getClearBlockFromOtherStack(x, underX)
        self.raiseBlock(underX)
        self.world.stack(underX, moveTo)
        moveTo = self.getClearBlockFromOtherStack(x, underX)
        self.raiseBlock(x)
        self.world.stack(x, moveTo)
        self.raiseBlock(underX)
        self.world.stack(underX, x)
        return True
        

    def matchesGoal(self):
        if self.goal.start == self.world.start:
            if self.goal.table == self.world.table:
                if self.goal.finish == self.world.finish:
                    return True
            if self.goal.table == self.world.finish:
                if self.goal.finish == self.world.table:
                    return True
        if self.goal.start == self.world.table:
            if self.goal.table == self.world.start:
                if self.goal.finish == self.world.finish:
                    return True
            if self.goal.table == self.world.finish:
                if self.goal.finish == self.world.start:
                    return True
        if self.goal.start == self.world.finish:
            if self.goal.table == self.world.start:
                if self.goal.finish == self.world.table:
                    return True
            if self.goal.table == self.world.table:
                if self.goal.finish == self.world.start:
                    return True
        return False
    
    def partiallyMatchesGoal(self, part):
        return part == self.goal.start[:len(part)] or part == self.goal.table[:len(part)] or part == self.goal.finish[:len(part)]
    
    def putAllOnStart(self):
        clearBlock = self.getClearBlockOfStack(self.world.start)
        while self.world.table:
            for x in self.world.table:
                if self.raiseBlock(x):
                    if clearBlock == 'GND':
                        self.world.putdown(x)
                    else:
                        self.world.stack(x, clearBlock)
                    clearBlock = x
        while self.world.finish:
            for x in self.world.finish:
                if self.raiseBlock(x):
                    if clearBlock == 'GND':
                        self.world.putdown(x)
                    else:
                        self.world.stack(x, clearBlock)
                    clearBlock = x

    def raiseBlock(self, x):
        if not self.world.clear(x):
            return False
        underX = self.getBlockUnder(x)
        if underX != 'GND':
            self.world.unstack(x, underX)
        else:
            self.world.pickup(x)
        return True
        


    def getClearBlockOfStack(self, stack):
        if stack:
            for x in stack:
                if self.world.clear(x):
                    return x
        return 'GND'


    def getClearBlockFromOtherStack(self, x1, x2):
        xCheck1 = x1
        xCheck2 = x1
        if not x2 == None and not x2 == '':
            xCheck2 = x2
        if not xCheck1 in self.world.start and not xCheck2 in self.world.start :
            if not self.world.start:
                return 'GND'
            for block in self.world.start:
                if self.world.clear(block):
                    return block
        if not xCheck1 in self.world.table and not xCheck2 in self.world.table:
            if not self.world.table:
                return 'GND'
            for block in self.world.table:
                if self.world.clear(block):
                    return block
        if not xCheck1 in self.world.finish and not xCheck2 in self.world.finish:
            if not self.world.finish:
                return 'GND'
            for block in self.world.finish:
                if self.world.clear(block):
                    return block
        return 'ERR'

    def getBlockUnder(self, x):
        if x in self.world.start:
            for block in self.world.start:
                if block != x and self.world.on(x, block):
                    return block
        if x in self.world.table:
            for block in self.world.table:
                if block != x and self.world.on(x, block):
                    return block
        if x in self.world.finish:
            for block in self.world.finish:
                if block != x and self.world.on(x, block):
                    return block
        return 'GND'
