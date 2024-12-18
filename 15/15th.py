import math
from collections import deque
import time
import sys


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkAhead(self, map, x, y, direction):

        if map[y][x] == "#":
            return False
        if map[y][x] == ".":
            return True
        
        
        match direction:
            case 0:
                return self.checkAhead(map, x, y-1, direction)
            case 1:
                return self.checkAhead(map, x+1, y, direction)
            case 2:
                return self.checkAhead(map, x, y+1, direction)
            case 3:
                return self.checkAhead(map, x-1, y, direction) 
            
    def checkAhead2(self, map, x, y, direction):

        if map[y][x] == "#":
            return False
        if map[y][x] == ".":
            return True
        if direction == 2:
            pass
        match direction:
            case 0 | 2:
                i = -1 if direction == 0 else 1
                if map[y+i][x] == "]":
                    return (
                            self.checkAhead2(map, x  , y+i, direction) and
                            self.checkAhead2(map, x-1, y+i, direction)
                            )
                elif map[y+i][x] == "[":
                    return (
                            self.checkAhead2(map, x  , y+i, direction) and
                            self.checkAhead2(map, x+1, y+i, direction)
                            )
                else:
                    return self.checkAhead2(map, x  , y+i, direction)
            case 1 | 3:
                i = 1 if direction == 1 else -1
                return self.checkAhead(map, x+i, y, direction)           

    def setAhead(self, map, x, y, direction):                                        

        if map[y][x] == ".":
            map[y][x] = "O"
            return 

        match direction:
            case 0:
                return self.setAhead(map, x, y-1, direction)
            case 1:
                return self.setAhead(map, x+1, y, direction)
            case 2:
                return self.setAhead(map, x, y+1, direction)
            case 3:
                return self.setAhead(map, x-1, y, direction) 
            
    def setAhead2(self, map, newMap, x, y, direction, prev):       
        match direction:
            case 1 | 3:
                if map[y][x] == ".":
                    map[y][x] = "]" if direction == 1 else "["
                    return 

                map[y][x] = "]" if map[y][x] == "[" else "["

                match direction:
                    case 1:
                        self.setAhead2(map, newMap, x+1, y, direction, "")
                    case 3:
                        self.setAhead2(map, newMap, x-1, y, direction, "") 
            case 0 | 2:
                
                i = -1 if direction == 0 else 1
                ls = [{(self.x, self.y)}]

                
                while True:
                    


                    next = map[y+i][x]
                    new_ls = set()
                    for item in ls[-1]:
                        x, y = item
                        next = map[y+i][x]
                        match next:
                            case "]":
                                new_ls.update({(x, y+i), (x-1, y+i)})
                            case "[":
                                new_ls.update({(x, y+i), (x+1, y+i)})
                            case "#":
                                return
                        
                    
                    if len(new_ls) == 0:
                        break
                    ls.append(new_ls)

                for item in ls[::-1]:
                    for x, y in list(item):
                        current = map[y][x]
                        if current == "@":
                            continue
                        map[y+i][x] = current
                        map[y][x] = '.'
                ls = []
                
                next = newMap[y+i][x]
                current = newMap[y][x]

                
        
    def move(self, map, direction):
        map[self.y][self.x] = "."
        match direction:
            case 0:
                self.y -= 1
            case 1:
                self.x += 1
            case 2:
                self.y += 1
            case 3:
                self.x -= 1
        map[self.y][self.x] = "@"

def copyMap(map):
    newMap = []
    for line in map:
        newMap.append(line.copy())
    return newMap

def printBoard(map):
    
    for i, line in enumerate(map):
        string = ""
        for j, char in enumerate(line):
            string += char
        print(string)
    print()

def run1(robot, map, instructions):

    for i, item in enumerate(instructions):
        
        direction = ""

        match item:
            case "^":
                direction = 0
            case ">":
                direction = 1
            case "v":
                direction = 2
            case "<":
                direction = 3

        if robot.checkAhead(map, robot.x, robot.y, direction):

            robot.setAhead(map, robot.x, robot.y, direction)
            robot.move(map, direction)

    total = 0


def run2(robot, map, instructions):
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char == "@":
                robot.x = j
                robot.y = i

    for i, item in enumerate(instructions):
        
        direction = ""

        match item:
            case "^":
                direction = 0
            case ">":
                direction = 1
            case "v":
                direction = 2
            case "<":
                direction = 3
        tf = robot.checkAhead2(map, robot.x, robot.y, direction)
        moving = ""
        match direction:
            case 0:
                moving = "up"
            case 1:
                moving = "right"
            case 2:
                moving = "down"
            case 3:
                moving = "left"

        newMap = copyMap(map)

        if tf:
            robot.setAhead2(map, newMap, robot.x, robot.y, direction, ".")
            robot.move(map, direction)

    total = 0
    for i, line in enumerate(map):
        string = ""
        for j, char in enumerate(line):
            total += 100*i + j if char == "[" else 0

    printBoard(map)
    print(f"Total: {total}")   


def main():
    
    map = []
    instructions = deque()
    with open('submarine.txt', 'r') as file:
        lines = file.readlines()
        isMap = True
        x, y = 0, 0
        for i, line in enumerate(lines):
            if line.isspace():
                isMap = False
                continue
                
            mapls = deque()
            for j, char in enumerate(line.strip()):
                
                if isMap:
                    mapls.append(char)
                    if char == "@":
                      x, y, = j, i  
                else:
                    instructions.append(char)
            if mapls:
                map.append(mapls)

    
    map2 = []
    for line in map:
        mapLine = []
        string = ""
        for char in line:
            if char == "#":
                mapLine.append("#")
                mapLine.append("#")
                string += "##"
            elif char == "O":
                mapLine.append("[")
                mapLine.append("]")
                string += "[]"
            elif char == ".":
                mapLine.append(".")
                mapLine.append(".")
                string += ".."
            elif char == "@":
                mapLine.append("@")
                mapLine.append(".")
                string += "@."
        map2.append(mapLine)
    robot = Robot(x, y)
    run1(robot, map, instructions)
    run2(robot, map2, instructions)


if __name__ == "__main__":
    main()