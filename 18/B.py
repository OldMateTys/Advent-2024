from collections import deque

def check(x, y, dir, map):
    
    match dir:
        case 0:
            if y > 0:
                if map[y-1][x] != "#":
                    return (x, y - 1)
             
        case 1:
            if x < 70:
                if map[y][x+1] != "#":
                    return (x + 1, y)
        case 2:
            if y < 70:
                if map[y+1][x] != "#":
                    return (x, y + 1)        
        case 3:
            if x > 0:
                if map[y][x-1] != "#":
                    return (x - 1, y)
                
def printMap(map, found):

    newMap = [line.copy() for line in map]
    for item in found:
        x, y = item
        newMap[y][x] = "O"
    
    
    for line in newMap:
        string = ""
        for item in line:
            string += item
        print(string)


def run(map, walls, i, lenWalls):
    
    queue = deque([(0, 0)])
    found = {(0, 0)}
    newQueue = deque()
    step = 0
    while True:
        step += 1
        while len(queue) > 0:

            
            
            x, y = queue.popleft()
            
            if x == 70 and y == 70:
                print(f"Progress: {i} / {lenWalls} | {step-1} steps")
                return True

            up    = check(x, y, 0, map)
            down  = check(x, y, 2, map)
            left  = check(x, y, 3, map)
            right = check(x, y, 1, map)
            
            dirs = (up, down, left, right)
            newFound = set()
            newAppend = []
            for dir in dirs:
                if dir is None:
                    continue
                if dir in found:
                    continue
                x, y = dir
                if map[y][x] == "#":
                    continue
                newFound.add(dir)
                newAppend.append(dir)
            newQueue.extend(newAppend)
            found.update(newFound)

        queue = newQueue
        
        newQueue = deque()

        if len(queue) == 0:
            return False

def main():
    
    map = []

    with open('text.txt', 'r') as file:
        
        walls = [(int(y[0]), int(y[1])) for y in [x.strip().split(",") for x in file.readlines()]]
        wallSet = set()

        map = ["."]*71

        
        i = 0


    search = [i for i in range(len(walls))]

    while len(search) > 0:

        if len(search) == 1:
            print(f"Output: {walls[search[0] + 1]}")
            break
        
        arrayLength = len(search)

        left = search[:arrayLength // 2]
        right = search[arrayLength // 2:]

        mid = search[arrayLength // 2]

        newMap = []
        for x in range(len(map)):
            newMap.append(map.copy())

        wallSet = set()
        for i, (x, y) in enumerate(walls):
            wallSet.add((x, y))
            newMap[y][x] = "#"
            if i == mid:
                break
        if run(newMap, wallSet, mid, len(walls)):
            search = right
        else:
            search = left
  
   
main()