# from search_algo import *


class Position:
    x = 0
    y = 0

    def __init__(self):
        return

    def __init__(self,xx,yy):
        self.x = xx
        self.y = yy
        return

    def print(self):
        print(str(self.x), str(self.y))

    def moveUp(self,array2D,stack):
        if( len(stack) >0 and stack.pop() ==self):
            return -1
        if(self.y>0 and array2D[self.x][self.y  -1 ] =='0' ):
            print('moving up')
            self.y-=1
            return self.y
        return -1
    def moveDown(self,array2D,stack):
        if( len(stack) >0 and stack.pop() ==self):
            return -1
        if(self.y<11 and array2D[self.x][self.y  +1 ] =='0'):
            print('moving down')
            self.y+=1
            return self.y
        return -1
    def moveRight(self,array2D,stack):
        if( len(stack) >0 and stack.pop() ==self):
            return -1
        if (self.x < 11 and array2D[self.x+1][self.y ] =='0'):
            print('moving right')
            self.x += 1
            return self.x
        return -1
    def moveLeft(self,array2D,stack):
        if( len(stack) >0 and  stack.pop() ==self):
            return -1
        if (self.x >0 and array2D[self.x -1 ][self.y] =='0'):
            print('moving left')
            self.x -= 1
            return self.x
        return -1




class Agent:
     pos = Position(0,0 )
     stack = []
     def __init__(self):
         self.pos.x = 11
         self.pos.y = 4
         self.stack.append(Position(self.pos.x,self.pos.y))
     def move(self,array2D):
        if (self.pos.moveRight(array2D,self.stack) > 0 or self.pos.moveLeft(array2D,self.stack) > 0 or self.pos.moveUp(array2D,self.stack) > 0 or self.pos.moveDown(array2D,self.stack) > 0 ):
            self.stack.append(Position(self.pos.x, self.pos.y))
            return self.pos
        else:
            return Position(-1,-1)






