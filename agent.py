# from search_algo import *


class Position:
    x = 0
    y = 0


    def __eq__(self , p2):
        if(self.y == p2.y and self.x == p2.x):
            return True

        return False
    def __init__(self):
        return

    def __init__(self,xx,yy):
        self.x = xx
        self.y = yy
        return

    def print(self):
        print(str(self.x), str(self.y))

    def moveUp(self,array2D,stack):
        # if(  stack[len(stack)-1]==Position( self.x ,self.y -1)):
        #     return -1
        if(self.y>0 and array2D[  self.y  -1][ self.x ] =='0' ):
            print('moving up')
            # array2D[self.y - 1][self.x] = 'X'
            self.y-=1
            return self.y
        return -1
    def moveDown(self,array2D,stack):
        # if(  stack[len(stack) -1 ]==Position( self.x ,self.y +1)):
        #     return -1
        if(self.y<11 and array2D[  self.y  +1][self.x ] =='0'):
            print('moving down')
            # array2D[self.y + 1][self.x] = 'X'
            self.y+=1
            return self.y
        return -1
    def moveRight(self,array2D,stack):
        # if(  stack[len(stack) -1 ] ==Position( self.x+1 ,self.y)):
        #     return -1
        if (self.x < 11 and array2D[  self.y ][self.x+1] =='0'):
            print('moving right')
            # array2D[self.y][self.x + 1] = 'X'
            self.x += 1
            return self.x
        return -1
    def moveLeft(self,array2D,stack):
        # if(   stack[len(stack) -1] ==Position( self.x -1,self.y)):
        #     return -1
        if (self.x >0 and array2D[  self.y][self.x -1] =='0'):
            print('moving left')
            # array2D[self.y][self.x - 1] = 'X'
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

         print('initizlizing agent')
     def move(self,array2D):
        array2D[self.pos.y][self.pos.x] = "X"
        if (self.pos.moveRight(array2D,self.stack) > 0 or self.pos.moveLeft(array2D,self.stack) > 0 or self.pos.moveUp(array2D,self.stack) > 0 or self.pos.moveDown(array2D,self.stack) > 0 ):
            self.stack.append(Position(self.pos.x, self.pos.y))
            return self.pos
        else:
            return Position(-1,-1)