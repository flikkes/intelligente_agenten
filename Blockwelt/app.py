import Agent
import Blockworld
from Agent import Agent
from Blockworld import World

world = World(['D', 'A', 'C'], [], ['B'])
goal = World(['D', 'A'], [], ['B', 'C'])
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