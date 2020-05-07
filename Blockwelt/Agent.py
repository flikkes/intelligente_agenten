import Blockworld
from Blockworld import World

class Agent:

    world = None
    goal = None

    def __init__(self, world, goal):
        self.world = world
        self.goal = goal

    def fulfillGroundGoal(self):
        for x in self.world.start:
            if self.goal.onground(x):
                if self.world.onground(x):
                    break
                if self.world.clear(x):
                    if not self.world.putdown(x):
                        self.freeGroundFor(x)


    def freeGroundFor(self, x):
        if not x in self.world.start:
            return True                
        

        return True
            
