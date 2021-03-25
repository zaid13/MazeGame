

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


array2D = readfile()
print(array2D)
