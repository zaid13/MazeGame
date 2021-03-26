# from search_algo import *

import copy


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

    def moveUp(self,array2D):
        if(self.y>0 and array2D[  self.y  -1][ self.x ] =='0' ):
            print('moving up')
            # array2D[self.y - 1][self.x] = 'X'
            self.y-=1
            return self.y
        return -1
    def moveDown(self,array2D):
        if(self.y<11 and array2D[  self.y  +1][self.x ] =='0'):
            print('moving down')
            # array2D[self.y + 1][self.x] = 'X'
            self.y+=1
            return self.y
        return -1
    def moveRight(self,array2D):
        if (self.x < 11 and array2D[  self.y ][self.x+1] =='0'):
            print('moving right')
            # array2D[self.y][self.x + 1] = 'X'
            self.x += 1
            return self.x
        return -1
    def moveLeft(self,array2D):
        if (self.x >0 and array2D[  self.y][self.x -1] =='0'):
            print('moving left')
            # array2D[self.y][self.x - 1] = 'X'
            self.x -= 1
            return self.x
        return -1


class Agent:
     ctr = 0
     pos = Position(0,0 )
     stack = []
     def __init__(self):
         self.pos.x = 11
         self.pos.y = 4
         self.stack.append(Position(self.pos.x,self.pos.y))
         print('initizlizing agent')
     def move(self,array2D):
        self.ctr+=1
        oldpos = copy.deepcopy(self.pos)
        array2D[oldpos.y][oldpos.x] = "X"
        if(Position(1,10) == self.pos):
            self.writeToFile(array2D)
            exit(0)
        if ( self.pos.moveDown(array2D) > 0 or self.pos.moveRight(array2D) > 0 or self.pos.moveLeft(array2D) > 0 or self.pos.moveUp(array2D) > 0  ):
            self.stack.append(Position(oldpos.x, oldpos.y))
            return self.pos
        else:
            return Position(-1,-1)


     def recoverDeadend(self,array):
            self.ctr+=1
            if(len(self.stack) == 0):
                self.writeToFile(array)
                exit(-1)
            len(self.stack)
            self.pos = self.stack.pop()
            if (self.pos.y > 0 and array[self.pos.y - 1][self.pos.x] == '0' or
            self.pos.y < 11 and array[self.pos.y + 1][self.pos.x] == '0' or
            self.pos.x < 11 and array[self.pos.y][self.pos.x + 1] == '0' or
            self.pos.x > 0 and array[self.pos.y][self.pos.x - 1] == '0'):
                print("this node will be used agian")
                print('self.pos')
                self.pos.print()
                self.stack.append(self.pos)
            return


     def writeToFile(self,array):
         with open('listfile.txt', 'w') as filehandle:
             for listitem in array:
                 filehandle.write('%s\n' % listitem)
             filehandle.write('%s\n' % self.ctr)
