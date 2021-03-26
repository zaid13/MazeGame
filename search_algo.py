from agent import Position

goal_postition = Position(0,10)
deadEnd_postition = Position(-1,-1)

def DFS(array2D,agent):
    while True:
         mov = agent.moveDfs(array2D)
         if goal_postition == mov:
             print("GOAL ACHIEVED")
             agent.writeToFileDfs(array2D)
             break
         if (deadEnd_postition == mov):
             print("DEAD END  ACHIEVED")
             agent.recoverDeadendDfs(array2D)
         else:
             mov.print()
def BFS(array2D,agent):
    while True:
         mov = agent.moveBfs(array2D)
         if goal_postition == mov:
             print("GOAL ACHIEVED")
             agent.writeToFileBfs(array2D)
             break
         if (deadEnd_postition == mov):
             print("DEAD END  ACHIEVED")
             agent.recoverDeadendBfs(array2D)
         else:
             mov.print()

