from agent import *
from search_algo import *

def readfile():
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    d = '1.txt'
    array2D = []
    f = open(d, "r")
    temp = [line.strip() for line in f.readlines()]
    for i in temp:
        array2D.append(i.split(' '))
    return array2D


inputt = int(input("enter 1 for DFS and anyother for BFS"))
if(inputt==1):
    DFS(readfile(), Agent())
else:
    BFS(readfile(), Agent())