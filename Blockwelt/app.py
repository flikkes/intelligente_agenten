import Agent
import Blockworld
from Agent import Agent
from Blockworld import Table

table = Table(['A', 'C', 'D'], [], ['B'])
agent = Agent(table, ['A', 'C', 'B', 'D'])

print('World Start: '+str(table.start))
print('World Table: '+str(table.table))
print('World Finish: '+str(table.finish))

print('Goal: '+str(agent.goal))

agent.reachGoal()

print('World Start: '+str(table.start))
print('World Table: '+str(table.table))
print('World Finish: '+str(table.finish))

print('Goal: '+str(agent.goal))