import sys
import Labyrinth
import time

class Agent:
    num = 0 
    x = 0
    y = 0
    labyrinth = None
    def __init__(self, x, y, labyrinth):
        self.num = time.time()*1000
        self.x = x
        self.y = y
        self.labyrinth = labyrinth
        print(str(self.num)+': Created new agent. Exploring now...')
        self.explore()
        
    
    def explore(self):
        walkableSpots = []
        if (self.labyrinth.isFinish(self.x, self.y)):
            print(str(self.num)+': Agent found the exit at x: '+str(self.x)+', y: '+str(self.y))
            sys.exit()
        self.labyrinth.visit(self.x, self.y)
        if (self.labyrinth.isWalkable(self.x-1, self.y)):
            walkableSpots.append({'x': self.x-1, 'y': self.y})
        if (self.labyrinth.isWalkable(self.x, self.y-1)):
            walkableSpots.append({'x': self.x, 'y': self.y-1})
        if (self.labyrinth.isWalkable(self.x+1, self.y)):
            walkableSpots.append({'x': self.x+1, 'y': self.y})
        if (self.labyrinth.isWalkable(self.x, self.y+1)):
            walkableSpots.append({'x': self.x, 'y': self.y+1})
        if (len(walkableSpots)==1):
            self.x = walkableSpots[0]['x']
            self.y = walkableSpots[0]['y']
            self.explore()
        if (len(walkableSpots)>1):
            for num, spot in enumerate(walkableSpots, start = 1):
                agent = Agent(spot['x'], spot['y'], self.labyrinth)
            self.x = walkableSpots[0]['x']
            self.y = walkableSpots[0]['y']
            self.explore()
        if (len(walkableSpots) == 0):
            print(str(self.num)+': Dead end reached, dying now...')

        
    