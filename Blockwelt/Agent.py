import Blockworld
from Blockworld import Table

class Agent:

    world = None
    goal = {}

    def __init__(self, world, goal):
        self.world = world
        self.goal = goal
    
    def reachGoal(self):
        if (self.world.finish == self.goal) or (self.world.start == self.goal):
            return True
        while not ((self.world.finish == self.goal) or (self.world.start == self.goal)):
            while self.world.start and not self.checkRestOrder(self.world.start):
                self.world.putDown(self.world.start[-1])
            while self.world.finish and not self.checkRestOrder(self.world.finish):
                self.world.putDown(self.world.finish[-1])
            if self.world.start:
                while self.world.table:
                    elem = self.world.table[0]
                    self.world.stack(elem, self.world.start[-1])
                    if not self.checkRestOrder(self.world.start):
                        self.world.putDown(elem)
            elif self.world.finish:
                while self.world.table:
                    elem = self.world.table[0]
                    self.world.stack(elem, self.world.finish[-1])
                    if not self.checkRestOrder(self.world.finish):
                        self.world.putDown(elem)
            else:
                self.world.stack(self.world.table[0], self.__getGroundElementOfGoal())
        
    def checkRestOrder(self, arr):
        for i in range(len(arr)):
            if arr[i] != self.goal[i]:
                return False
        return True

    def __getGroundElementOfGoal(self):
        return self.goal[0]
            
