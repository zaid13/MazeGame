from agent import Position

goal_postition = Position(0,10)
deadEnd_postition = Position(-1,-1)

def DFS(array2D,agent):
    while True:
         mov = agent.move(array2D)
         if goal_postition == mov:
             print("GOAL ACHIEVED")
             agent.writeToFile(array2D)
             break
         if (deadEnd_postition == mov):
             print("DEAD END  ACHIEVED")
             agent.recoverDeadend(array2D)
         else:
             mov.print()