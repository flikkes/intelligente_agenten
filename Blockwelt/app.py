import sys
import Agent
import Blockworld
from Agent import Agent
from Blockworld import World

rawWorld = sys.argv[1]
rawGoal = sys.argv[2]
rawWorldSplit = rawWorld.split('-')
rawGoalSplit = rawGoal.split('-')
wA = []
wB = []
wC = []
gA = []
gB = []
gC = []
print(rawWorldSplit)
for elem in rawWorldSplit[0].split(','):
    if (not elem.strip() == ''):
        wA.append(elem)
for elem in rawWorldSplit[1].split(','):
    if (not elem.strip() == ''):
        wB.append(elem)
for elem in rawWorldSplit[2].split(','):
    if (not elem.strip() == ''):
        wC.append(elem)
for elem in rawGoalSplit[0].split(','):
    if (not elem.strip() == ''):
        gA.append(elem)
for elem in rawGoalSplit[1].split(','):
    if (not elem.strip() == ''):    
        gB.append(elem)
for elem in rawGoalSplit[2].split(','):
    if (not elem.strip() == ''):
        gC.append(elem)


world = World(wA, wB, wC)
goal = World(gA, gB, gC)
agent = Agent(world, goal)
print('=========== UNSOLVED ===========')
print('World Start: '+str(world.start))
print('World Table: '+str(world.table))
print('World Finish: '+str(world.finish))

print('Goal Start: '+str(goal.start))
print('Goal Table: '+str(goal.table))
print('Goal Finish: '+str(goal.finish))

agent.fulfillGoal()
print('=========== SOLVED ===========')
print('World Start: '+str(world.start))
print('World Table: '+str(world.table))
print('World Finish: '+str(world.finish))

print('Goal Start: '+str(goal.start))
print('Goal Table: '+str(goal.table))
print('Goal Finish: '+str(goal.finish))