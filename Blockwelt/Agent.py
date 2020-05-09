import Blockworld
from Blockworld import World

class Agent:

    world = None
    goal = None

    def __init__(self, world, goal):
        self.world = world
        self.goal = goal

    def fulfillGroundGoal(self):
        x = self.getInitialBlock()
        while x != 'GND':
            nextBlock = self.getBlockUnder(x)
            if self.world.pickup(x):
                ## TODO check here if x on ground or on other position and react accordingly
                while not self.world.onground(x):
                    stackBackOn = self.getClearBlockFromOtherStack(x)
                    self.world.stack(x, stackBackOn)
                    blockToMoveAway = self.getClearBlockFromOtherStack(x)
                    blockToMoveTo = self.getClearBlockFromOtherStack(x, blockToMoveAway)
                    self.world.pickup(blockToMoveAway)
                    self.world.stack(blockToMoveAway, blockToMoveTo)
                    self.world.pickup(x)
                    self.world.putdown(x)
                if self.goal.onground(x):
                    x = nextBlock
                else:
                    self.world.pickup(x)
                    clearBlock = self.getClearBlockFromOtherStack(x)
                    if clearBlock == 'GND':
                        self.world.putdown(x)
                    else: 
                        self.world.stack(x, clearBlock)
                    x = nextBlock
                    
    def getInitialBlock(self):
        if self.world.start:
            for x in self.world.start:
                if self.world.clear(x):
                    return x
        if self.world.table:
            for x in self.world.table:
                if self.world.clear(x):
                    return x
        if self.world.finish:
            for x in self.world.finish:
                if self.world.clear(x):
                    return x


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
