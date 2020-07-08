import sys
import os
import Labyrinth
import time
import threading

class Agent:
    num = 0 
    x = 0
    y = 0
    labyrinth = None
    callback = None
    def __init__(self, x, y, labyrinth, callback):
        self.num = time.time()*1000
        self.x = x
        self.y = y
        self.labyrinth = labyrinth
        self.callback = callback
        print(str(self.num)+': Created new agent. Exploring...')
        t = threading.Thread(target=self.explore)
        t.start()

    def explore(self):
        self.callback()
        if self.labyrinth.finished or self.labyrinth.isVisited(self.x, self.y):
            sys.exit()
        walkableSpots = []
        if (self.labyrinth.isFinish(self.x, self.y)):
            print(str(self.num)+': Agent found the exit at x: '+str(self.x)+', y: '+str(self.y))
            self.labyrinth.finished = True
            sys.exit()
        self.labyrinth.visit(self.x, self.y)
        print('{}: Visiting {} {}'.format(str(self.num), self.x, self.y))
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
            t = threading.Thread(target=self.explore)
            t.start()
        if (len(walkableSpots)>1):
            for num, spot in enumerate(walkableSpots, start = 1):
                agent = Agent(spot['x'], spot['y'], self.labyrinth, self.callback)
            self.x = walkableSpots[0]['x']
            self.y = walkableSpots[0]['y']
            t = threading.Thread(target=self.explore)
            t.start()
        if (len(walkableSpots) == 0):
            print(str(self.num)+': Dead end reached, dying...')
            sys.exit()

        
    